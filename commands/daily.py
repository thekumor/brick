# ================================================================
#
#	Gives user money (given they didn't get it that day).
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

from discord import app_commands
import utility.database

async def AskForDaily(interaction):
	oldCount = utility.database.BrickDatabase.GetValue(interaction.guild, "economy", "discord_id", interaction.user.id, "money") or 0

	daily = 20
	newCount = oldCount + daily

	utility.database.BrickDatabase.SetValue(interaction.guild, "economy", "discord_id", interaction.user.id, "money", newCount)

	await interaction.response.send_message(f"You received your daily of {daily}€! You now have {newCount}. 💶", ephemeral = False)

daily = app_commands.Command(name="daily", description="Gives you money (per day).", callback = AskForDaily)