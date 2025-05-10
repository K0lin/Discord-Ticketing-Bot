# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import discord
#Local file
from utils.config_manager import *

class EmbeddedList:
    def __init__(self, configManager: ConfigManager):
        self.configManager = configManager
    
    def ticketCreation(self):
        embed = discord.Embed(
            title=f"{self.configManager.getTicketCreationTitle()}",
            description=f"{self.configManager.getTicketCreationDescription()}",
            colour=discord.Colour.from_str(self.configManager.getTicketCreationEmbedColor()) 
        )
        embed.set_author(name=f"{self.configManager.getTicketCreationAuthor()}")
        return embed
    
    def ticketClosure(self):
        embed = discord.Embed(
            title=f"{self.configManager.getTicketClosureTitle()}",
            description=f"{self.configManager.getTicketClosureDescription()}",
            colour=discord.Colour.from_str(self.configManager.getTicketClosureEmbedColor()) 
        )
        if self.configManager.getMessagesLog:
            embed.set_footer(text="All messages you send here will be recorded.")
        embed.set_author(name=f"{self.configManager.getTicketClosureAuthor()}")
        return embed