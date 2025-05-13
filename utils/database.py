# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import os
import sqlite3
from datetime import datetime
import pytz
#Local File
from utils.paths_manager import PathsManager
from utils.connectionPool import ConnectionPool


class Database:
    def __init__(self, directory, name, timezone: pytz.timezone):        
        self.db_pool = ConnectionPool(directory, name)
        self.timezone = timezone
        self.db_pool.execute("CREATE TABLE IF NOT EXISTS ticket(id INTEGER NOT NULL, createdBy TEXT NOT NULL, closedBy TEXT, creationDate TEXT NOT NULL, creationMotivation TEXT, closeMotivation TEXT, closeData TEXT, PRIMARY KEY('id' AUTOINCREMENT))")
        self.db_pool.execute("CREATE TABLE IF NOT EXISTS message(id INTEGER NOT NULL, ticketId TEXT NOT NULL, user TEXT NOT NULL, message TEXT NOT NULL, date TEXT, PRIMARY KEY('id' AUTOINCREMENT))")

    def getTicketId(self):
        row = self.db_pool.fetchone(f"SELECT count(*) FROM ticket")
        if row is None:
            return 0
        return int(row[0])
    
    def createNewTicket(self, id, createdBy, motivation):
        self.db_pool.execute(f"INSERT INTO ticket(id, createdBy, creationDate, creationMotivation) VALUES (?, ?, ?, ?)", (id, createdBy, datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S"), motivation))

    def updateTicketClosure(self, closedBy, motivation, id):
        self.db_pool.execute(f"UPDATE ticket SET closedBy = ?, closeMotivation = ?, closeData = ? WHERE id = ?", (closedBy, motivation, datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S"), str(id)))

    def ticketInfo(self, id):
        row = self.db_pool.fetchone(f"SELECT * FROM ticket WHERE id={id}")
        if row is None:
            return 0
        return row

    def insertTicketMessage(self, ticketId, user, message):
        self.db_pool.execute(f"INSERT INTO message(ticketId, user, message, date) VALUES (?, ?, ?, ?)", (ticketId, user, message, datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S")))

    def getTicketMessage(self, ticketId):
        row = self.db_pool.fetchall(f"SELECT user, message, date FROM message WHERE ticketId = {ticketId} ORDER BY ticketId ASC")
        if row is None:
            return 0
        return row
