# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import sqlite3
from datetime import datetime
import pytz

class Database:
    def __init__(self, name, timezone: pytz.timezone):
        self.con = sqlite3.connect(f"ticketing/{name}.db")
        self.con.execute("CREATE TABLE IF NOT EXISTS ticket(id INTEGER NOT NULL, createdBy TEXT NOT NULL, closedBy TEXT, creationDate TEXT NOT NULL, creationMotivation TEXT, closeMotivation TEXT, closeData TEXT, PRIMARY KEY('id' AUTOINCREMENT))")
        self.con.commit()
        self.con.execute("CREATE TABLE IF NOT EXISTS message(id INTEGER NOT NULL, ticketId TEXT NOT NULL, user TEXT NOT NULL, message TEXT NOT NULL, date TEXT, PRIMARY KEY('id' AUTOINCREMENT)) ")
        self.con.commit()
        self.timezone = timezone

    def getTicketId(self):
        exe = self.con.execute(f"SELECT count(*) FROM ticket")
        row = exe.fetchone()
        if row is None:
            return 0
        return int(row[0])
    
    def createNewTicket(self, id, createdBy, motivation):
        self.con.execute(f"INSERT INTO ticket(id, createdBy, creationDate, creationMotivation) VALUES (?, ?, ?, ?)", (id, createdBy, datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S"), motivation))
        self.con.commit()

    def updateTicketClosure(self, closedBy, motivation, id):
        self.con.execute(f"UPDATE ticket SET closedBy = ?, closeMotivation = ?, closeData = ? WHERE id = ?", (closedBy, motivation, datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S"), str(id)))
        self.con.commit()

    def ticketInfo(self, id):
        exe = self.con.execute(f"SELECT * FROM ticket WHERE id={id}")
        row = exe.fetchone()
        if row is None:
            return 0
        return row

    def insertTicketMessage(self, ticketId, user, message):
        self.con.execute(f"INSERT INTO message(ticketId, user, message, date) VALUES (?, ?, ?, ?)", (ticketId, user, message, datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S")))
        self.con.commit()

    def getTicketMessage(self, ticketId):
        exe = self.con.execute(f"SELECT user, message, date FROM message WHERE ticketId = {ticketId} ORDER BY ticketId ASC")
        row = exe.fetchall()
        if row is None:
            return 0
        return row