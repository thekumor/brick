# ================================================================
#
#	Tells the user how many characters they've typed.
#
#	#Module: Stats
#	#Component: Message counter
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

from discord import app_commands
import sqlite3
import os

async def GetChars(interaction):
	path = "/var/brick/databases"

	posts = sqlite3.connect(os.path.join(path, str(interaction.guild.id) + ".db"))
	cursor = posts.cursor()

	cursor.execute(
		"SELECT 1 FROM users WHERE discord_id = ?",
		(interaction.user.id,)
	)
	exists = cursor.fetchone()

	count = 0

	if exists:
		cursor.execute(
			"SELECT char_count FROM users WHERE discord_id = ?",
			(interaction.user.id,)
		)
		chars = cursor.fetchone()

		if chars is None:
			count = 0
		else:
			count = chars[0]

	posts.close()

	await interaction.response.send_message(f"Your character count: {count}", ephemeral = True)

chars = app_commands.Command(name="chars", description="Tells how many characters you've typed.", callback = GetChars)