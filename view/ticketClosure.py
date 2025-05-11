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