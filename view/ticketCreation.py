# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import discord
from discord.ui import Button
#Local file
from utils.config_manager import *
from utils.database import *
from utils.embed import *
from view.ticketClosure import * 
from main import language

class TicketCreation(discord.ui.View):
    def __init__(self, configManager: ConfigManager = None, database: Database = None, embed: EmbeddedList = None):
        super().__init__(timeout=None)
        self.configManager = configManager
        self.database = database
        self.embed = embed
        for buttonDetails in configManager.getTicketChoiceButton():
            for name, style in buttonDetails.items():
                button = Button(
                    label=f"{name}", 
                    style=getattr(discord.ButtonStyle, style),
                    custom_id=f"persistent:ticketCreation{name}"
                )
                button.callback = self.make_callback(name)
                self.add_item(button)

    def make_callback(self, category):
        async def callback(interaction: discord.Interaction):
            id = int(self.database.getTicketId())+1
            channel =  await interaction.guild.create_text_channel(
                name=f"{category}-ticket-{interaction.user.name}-{id}",
                category=interaction.guild.get_channel(self.configManager.getTicketCategoryId())
            )
            await channel.edit(sync_permissions=True)
            current_overwrites = channel.overwrites
            current_overwrites[interaction.user] = discord.PermissionOverwrite(read_messages=True)
            await channel.edit(overwrites=current_overwrites)
            await channel.send(embed=self.embed.ticketClosure(), view=TicketClosure(database=self.database, configManager=self.configManager))
            self.database.createNewTicket(id, interaction.user.id, "category")
            message = language.translate("ticket_creation.opened_to_channel",category=category,channel_mention=channel.mention)
            await interaction.response.send_message(message, ephemeral=True)

            #logging
            if self.configManager.getConsoleLogEnabled():
                print(f"[Ticket Created] User {interaction.user.name} (ID: {interaction.user.id}) opened a '{category}' ticket: {channel.name}")
        return callback
