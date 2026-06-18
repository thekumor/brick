# ================================================================
#
#	Saves amount of user messages to database.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

import sqlite3

path = "/var/brick/"

posts = sqlite3.connect(path + "brick.db")
cursor = posts.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(" \
"id INTEGER PRIMARY KEY AUTOINCREMENT," \
"discord_id INTEGER," \
"char_count INTEGER);")
posts.commit()