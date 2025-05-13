# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import discord
import io
#Local file
from utils.database import *
from utils.config_manager import *
from main import language


class TicketMessageLog(discord.ui.View):
    def __init__(self, database: Database = None, configManager: ConfigManager = None):
        super().__init__(timeout=None)
        self.database = database
        self.configManager = configManager
    
    @discord.ui.button(label="See messages 🔎", style=discord.ButtonStyle.primary, custom_id="persistent:ticketLoggedMessage")
    async def ticketLoggedMessage(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.configManager.getDownloadLog():
            bindMessage =  await  interaction.channel.fetch_message(interaction.message.id)
            ticketId =  int(bindMessage.embeds[0].author.name.split("-")[3])
            logMessages = self.database.getTicketMessage(ticketId)
            file_content = ""
            #logging
            if self.configManager.getConsoleLogEnabled():
                print(
                    f"[Ticket Log Requested] Ticket #{ticketId} log requested by {interaction.user.name} ({interaction.user.id})")
            if(logMessages!=[]):
                for message in logMessages:
                    user = await interaction.client.fetch_user(message[0])
                    file_content = file_content + f"({message[2]}) {user.name}: {message[1]}\n"
                    file = io.BytesIO(file_content.encode('utf-8'))
                    file.seek(0)

                message = language.translate("ticket_message_log.file.found")
                await interaction.response.send_message(message, file=discord.File(file, f"{bindMessage.embeds[0].author.name}.txt"), ephemeral=True)
            else:
                message = language.translate("ticket_message_log.no_messages_logged")
                await interaction.response.send_message(message, ephemeral=True)
        else:
            message = language.translate("ticket_message_log.disabled_function")
            await interaction.response.send_message(message, ephemeral=True)