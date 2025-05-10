# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import os, json

class ConfigManager:
    def __init__(self, config):
        self.config = self._readJSON(config) 

    def getBotToken(self):
        return self.config.get("BOT_TOKEN")
    
    def getBotStatus(self):
        return self.config.get("BOT_STATUS")
    
    def getDatabaseName(self):
        return self.config.get("DATABASE_NAME")
    
    def getMessagesLog(self):
        return self.config.get("MESSAGES_LOG")

    def getTicketChoiceButton(self):
        return self.config.get("TICKET_CHOICE_BUTTON")

    def getTicketCreationChannelId(self):
        return self.config.get("TICKET_CREATION_CHANNEL_ID")

    def getRefreshTicketCreationMessage(self):
        return self.config.get("REFRESH_CREATION_MESSAGE")
    
    def getTicketCreationEmbedColor(self):
        return self.config.get("TICKET_CREATION_EMBED_COLOR")
    
    def getTicketCreationAuthor(self):
        return self.config.get("TICKET_CREATION_AUTHOR")
    
    def getTicketCreationTitle(self):
        return self.config.get("TICKET_CREATION_TITLE")
    
    def getTicketCreationDescription(self):
        return self.config.get("TICKET_CREATION_DESCRIPTION")
    
    def getTicketCategoryId(self):
        return self.config.get("TICKET_CATEGORY_ID")
    
    def getTimezone(self):
        return self.config.get("TIMEZONE")
    
    def getTicketClosureEmbedColor(self):
        return self.config.get("TICKET_CLOSURE_EMBED_COLOR")
    
    def getTicketClosureAuthor(self):
        return self.config.get("TICKET_CLOSURE_AUTHOR")
    
    def getTicketClosureTitle(self):
        return self.config.get("TICKET_CLOSURE_TITLE")
    
    def getTicketClosureDescription(self):
        return self.config.get("TICKET_CLOSURE_DESCRIPTION")
    
    def getTicketLogChannelId(self):
        return self.config.get("TICKET_LOG_CHANNEL_ID")
    
    def getTicketEnableClosingRoleId(self):
        return self.config.get("TICKET_ENABLE_CLOSING_ROLE_ID")
    
    def getDownloadLog(self):
        return self.config.get("DOWNLOAD_LOG")

    def _readJSON(self, file_name) -> dict:
        path=os.path.dirname(os.path.dirname((__file__)))
        print("Config loaded: " + path +"/" + file_name + ".json")
        if not os.path.exists(path +"/" + file_name + ".json"):
            return {}

        with open(path +"/" + file_name + ".json", "r") as jsonFile:
            return json.load(jsonFile)