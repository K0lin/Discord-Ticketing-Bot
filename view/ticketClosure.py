# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import discord
from discord import ui
#Local file
from utils.database import *
from utils.config_manager import *
from view.ticketMessageLog import *

class TicketClosure(discord.ui.View):
    def __init__(self, database: Database = None, configManager: ConfigManager = None):
        super().__init__(timeout=None)
        self.database = database
        self.configManager = configManager
    
    @discord.ui.button(label="Close", style=discord.ButtonStyle.danger, custom_id="persistent:ticketClose")
    async def ticketClose(self, interaction: discord.Interaction, button: discord.ui.Button):
        find = False
        for role in self.configManager.getTicketEnableClosingRoleId():
            if interaction.guild.get_role(role) in interaction.user.roles:
                find = not find
                await interaction.response.send_modal(TicketClosureFinal(configManager=self.configManager, database=self.database,title="Ticket closure", ticketChannel = interaction.channel, ticketNumber = interaction.channel.name, closedBy=interaction.user.id, guild=interaction.guild))
                break       
        if not find:
            await interaction.response.send_message("You can't close the ticket", ephemeral=True)

    @discord.ui.button(label="Add/Remove user", style=discord.ButtonStyle.secondary, custom_id="persistent:addRemoveUser")
    async def addRemoveUser(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Check if user has permission to add users
            find = False
            for role in self.configManager.getTicketEnableClosingRoleId():
                if interaction.guild.get_role(role) in interaction.user.roles:
                    find = True
                    # Get list of eligible members (excluding bots, current user, and users already in ticket)
                    eligible_members = [
                        m for m in interaction.guild.members 
                        if not m.bot and  # Exclude bots
                        #not interaction.channel.permissions_for(m).view_channel and 
                        m.id != interaction.user.id  # Exclude command user
                    ]
                    
                    if not eligible_members:
                        await interaction.response.send_message(
                            "No eligible users to add to the ticket.", 
                            ephemeral=True
                        )
                        return
                    
                    # Create and send the user select view
                    await interaction.response.send_message(
                        "Select users to add to the ticket:", 
                        view=UserSelectView(eligible_members, interaction, self.configManager, self.database), 
                        ephemeral=True
                    )
                    break
                    
            if not find:
                await interaction.response.send_message(
                    "You don't have permission to add o remove users to tickets.", 
                    ephemeral=True
                )
                
        except discord.Forbidden:
            await interaction.response.send_message(
                "I don't have permission to modify ticket permissions.", 
                ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"An error occurred: {str(e)}", 
                ephemeral=True
            )       
class TicketClosureFinal(ui.Modal):
    def __init__(self, configManager: ConfigManager = None, database: Database= None, title: str = None, ticketChannel= None, ticketNumber= None, closedBy= None, guild= None):
        super().__init__(timeout=None,title=title)
        self.ticketChannel=ticketChannel
        self.ticketNumber=ticketNumber
        self.closedBy = closedBy
        self.guild = guild
        self.database=database
        self.configManager = configManager

        self.reason = ui.TextInput(
            label="Ticket closure",
            placeholder="Reason...",
            min_length=10,
            max_length=500,
            style=discord.TextStyle.paragraph,
            custom_id="reasonTicketClosure",
            required=True
        )
        self.add_item(self.reason)
    
    async def on_submit(self, interaction: discord.Interaction):
        id =  int(self.ticketNumber.split("-")[3])
        self.database.updateTicketClosure(self.closedBy,self.reason.value,id)
        await self.ticketChannel.delete()

        #logging
        if self.configManager.getConsoleLogEnabled():
            user = self.guild.get_member(int(self.closedBy))
            print(f"[Ticket Closed] Ticket #{id} closed by {user.name} ({user.id}) — Reason: {self.reason.value}")

        ticketDetail = self.database.ticketInfo(id)
        embed = discord.Embed()
        embed.set_author(name=f"{self.ticketChannel}")
        embed.add_field(name=":id: Ticket ID",
                        value=f"{id}",
                        inline=True)
        embed.add_field(name=":open_file_folder: Opened By",
                        value=f"{self.guild.get_member(int(ticketDetail[1])).mention}",
                        inline=True)
        embed.add_field(name=":closed_lock_with_key: Closed By",
                        value=f"{self.guild.get_member(int(ticketDetail[2])).mention}",
                        inline=True)
        embed.add_field(name=f":timer: {self.configManager.getTimezone()} Closing Time ",
                        value=f"{ticketDetail[6]}",
                        inline=False)
        embed.add_field(name=":ledger: Reason",
                        value=f"{ticketDetail[5]}",
                        inline=False)
        channel = self.guild.get_channel(self.configManager.getTicketLogChannelId())
        await channel.send(embed=embed, view = TicketMessageLog(database=self.database, configManager=self.configManager))
        await interaction.response.defer(ephemeral=True)

class UserSelectView(discord.ui.View):
    def __init__(self, users: list, interaction: discord.Interaction = None, configManager: ConfigManager = None, database: Database = None):
        super().__init__(timeout=None)
        
        self.configManager = configManager
        self.database = database
        # Get users who can already view the channel
        if interaction != None:
            self.channel = interaction.channel
            self.current_users = [
                member for member in interaction.channel.members 
                if interaction.channel.permissions_for(member).view_channel and 
                not member.bot and 
                member in users
            ]
        else:
            self.channel = None
            self.current_users = []
        
        
        # Create the select menu without default_values
        self.select = ui.UserSelect(
            placeholder="Choose the users to add...",
            min_values=1,
            max_values=25,
            custom_id="selectUsers"
        )
        

        self.select.callback = self.select_callback
        self.add_item(self.select)

    async def select_callback(self, interaction: discord.Interaction):
        try:
            # Check if any selected user fails the requirements
            invalid_selection = any(
                user for user in self.select.values
                if (
                    user.bot or  # Check if user is a bot
                    any(interaction.guild.get_role(role_id) in user.roles  # Check if user has any of the restricted roles
                        for role_id in self.configManager.getTicketEnableClosingRoleId()) or
                    user.id == int(self.database.ticketInfo(int(interaction.channel.name.split("-")[3]))[1])  or# Check specific user ID
                    user.id == interaction.guild.owner_id 
                )
            )

            if not invalid_selection:
                # Remove permissions from users who were deselected
                for user in self.current_users:
                    if user in self.select.values and not user.bot:
                        await self.channel.set_permissions(user, overwrite=None)
                        await self.channel.set_permissions(user, read_messages=None)

                # Add permissions for newly selected users
                for user in self.select.values:
                    if user not in self.current_users:
                        await self.channel.set_permissions(user,
                            view_channel=True,
                            send_messages=True,
                            read_message_history=True
                        )
                    
                # Create response message
                users_added = ", ".join(user.mention for user in self.select.values)
                await interaction.response.send_message(
                    f"Updated ticket permissions. Current users: {users_added}",
                    ephemeral=True
                )
            else:
                 await interaction.response.send_message(
                    f"One of these selected users cannot be selected, redo the selection.",
                    ephemeral=True
                )
            
        except discord.Forbidden:
            await interaction.response.send_message(
                "I don't have permission to modify channel permissions.",
                ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"An error occurred while updating permissions: {str(e)}",
                ephemeral=True
            )
