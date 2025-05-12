# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.
#External Library
import os
import sqlite3
import queue
#Local File
from utils.paths_manager import PathsManager

class ConnectionPool:
    def __init__(self, db_path, name, max_connections=10):
        absolute_path_directory = PathsManager.get_subdirectory_path(db_path)
        if not os.path.isdir(absolute_path_directory):
            os.mkdir(absolute_path_directory)
        self.filename = PathsManager.get_filename(db_path, name, "db")
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                pass
        self.db_path = self.filename
        self.max_connections = max_connections
        self._pool = queue.Queue(maxsize=max_connections)
        self._lock = threading.Lock()
        self._create_connections()

    def _create_connections(self):
        for _ in range(self.max_connections):
            try:
                conn = sqlite3.connect(self.db_path, check_same_thread=False)
                self._pool.put(conn)
            except sqlite3.Error as e:
                print(f"Error creating connection: {e}")

    def get_connection(self):
        return self._pool.get()

    def release_connection(self, conn):
        self._pool.put(conn)

    def execute(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            conn.rollback()
            raise
        finally:
            cursor.close()
            self.release_connection(conn)
            return cursor.rowcount

    def fetchone(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching one: {e}")
            raise
        finally:
            cursor.close()
            self.release_connection(conn)

    def fetchall(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching all: {e}")
            raise
        finally:
            cursor.close()
            self.release_connection(conn)

    def close_pool(self):
        while not self._pool.empty():
            conn = self._pool.get()
            conn.close()
