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
import utility.database

async def GetChars(interaction):
	count = utility.database.BrickDatabase.GetValue(interaction.guild, "users", "char_count", "discord_id", interaction.user.id) or 0
	await interaction.response.send_message(f"Your character count: {count}", ephemeral = True)

chars = app_commands.Command(name="chars", description="Tells how many characters you've typed.", callback = GetChars)