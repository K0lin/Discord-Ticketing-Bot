# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
from discord.ext import commands
import discord
import pytz
#Local file
from utils.config_manager import *
from utils.database import *
from utils.embed import *
from view.ticketCreation import *
from view.ticketClosure import *
from view.ticketMessageLog import *
from utils.localization import Translator

#Class configuration
configManager = ConfigManager("config")
timezone = pytz.timezone(configManager.getTimezone())
database = Database(configManager.getDatabaseLocation(), configManager.getDatabaseName(), timezone)
embed = EmbeddedList(configManager=configManager)
language_code = configManager.getLanguageCode()
language = Translator(language_code)
#Bot configuration
bot = commands.Bot(command_prefix="", intents=discord.Intents.all())

@bot.event
async def on_ready():
    #Setup view
    bot.add_view(TicketCreation(database=database, configManager=configManager, embed=embed))
    bot.add_view(TicketClosure(database=database, configManager=configManager))
    bot.add_view(TicketClosureFinal())
    bot.add_view(TicketMessageLog(database=database, configManager=configManager))
    #Bot status
    await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=configManager.getBotStatus()
            )
        )

    #logging
    if configManager.getConsoleLogEnabled():
        print(
            f"[Bot Ready] Bot has connected to Discord and is now online with status '{configManager.getBotStatus()}'")

    if configManager.getRefreshTicketCreationMessage():
        channel = bot.get_channel(configManager.getTicketCreationChannelId())
        await channel.purge(limit=1)
        await channel.send(embed=embed.ticketCreation(), view=TicketCreation(configManager=configManager, database=database, embed=embed))

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    #Ticket message saving
    if configManager.getMessagesLog():
        if str(message.channel.category.id) == str(configManager.getTicketCategoryId()):
            ticketId = int(message.channel.name.split("-")[3]) 
            database.insertTicketMessage(ticketId,message.author.id,message.content)

    # Log first 50 chars for brevity
    if configManager.getConsoleLogEnabled():
        print(
            f"[Ticket Message Saved] Message saved to ticket #{ticketId} by {message.author.name} ({message.author.id}): {message.content[:50]}...")


#Bot start
bot.run(configManager.getBotToken())