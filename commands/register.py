# ================================================================
#
#	Registers every user on the server for database (omits bots).
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

from discord import app_commands
import sqlite3

def RegisterUsers():
	path = "/var/brick/databases"

	posts = sqlite3.connect(path + "brick.db")
	cursor = posts.cursor()

	cursor.execute("CREATE TABLE IF NOT EXISTS users(" \
	"id INTEGER PRIMARY KEY AUTOINCREMENT," \
	"discord_id INTEGER," \
	"char_count INTEGER);")
	posts.commit()

	posts.close()

register = app_commands.Command(name='register', description='Registers everybody.', callback = lambda interaction: interaction.response.send_message('Pong!'))