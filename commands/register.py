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
import os

async def RegisterUsers(interaction):
	path = "/var/brick/databases"

	posts = sqlite3.connect(os.path.join(path, str(interaction.guild.id) + ".db"))
	cursor = posts.cursor()

	for member in interaction.guild.members:
		cursor.execute(
			"SELECT 1 FROM users WHERE discord_id = ?",
			(member.id,)
		)
		exists = cursor.fetchone()

		if not exists:
			cursor.execute(
				"INSERT INTO users(discord_id, char_count) VALUES(?, ?)",
				(member.id, 0)
				)
		
	posts.commit()
	posts.close()

	await interaction.response.send_message("Registered all users successfully", ephemeral = True)

register = app_commands.Command(name="register", description="Registers everybody.", callback = RegisterUsers)