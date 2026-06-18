# ================================================================
#
#	Creates databases for all servers the bot is in.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

import sqlite3
import os

class Database:
    def __init__(self):
        self.path = "/var/brick"

    def Create(self, bot):
        # #Section: folder creation
        dir = os.path.join(self.path, "databases")

        if not os.path.exists(dir):
            os.mkdir(dir)

        # #Section: database creation

        for guild in bot.guilds:
            dbPath = os.path.join(self.path, f"{guild.id}.db")
            conn = sqlite3.connect(dbPath)
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                discord_id INTEGER,
                char_count INTEGER
            )
            """)

            conn.commit()
            conn.close()
        
        # #EndSection