# ===============================================================
#
#	Gives user money (given they didn't get it that day).
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

import utility.database
from discord import app_commands
import time

async def AskForDaily(interaction):
	values = utility.database.BrickDatabase.GetValues(interaction.guild, "economy", "discord_id", interaction.user.id, ["money", "last_daily"])
	
	if len(values) == 0:
		await interaction.response.send_message(f"Something went wrong :(", ephemeral = True)
		return

	oldCount = values[0]
	lastDaily = values[1]

	timestamp = time.localtime(lastDaily)
	today = int(time.localtime())

	isSameDay = (
		timestamp.tm_year == today.tm_year and
		timestamp.tm_yday == today.tm_yday
	)

	if isSameDay:
		await interaction.response.send_message(f"You have already received your daily! 🚫", ephemeral = True)
		return

	daily = 20
	newCount = oldCount + daily

	utility.database.BrickDatabase.SetValues(interaction.guild, "economy", "discord_id", interaction.user.id, ["money", "last_daily"], [newCount, time])

	await interaction.response.send_message(f"You received your daily of { daily }€! You now have { newCount }. 💶", ephemeral = False)

daily = app_commands.Command(name = "daily", description = "Gives you money (per day).", callback = AskForDaily)