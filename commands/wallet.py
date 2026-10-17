# ===============================================================
#
#	Tells user how much money they have.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands
import utility.database

async def GetMoney(interaction):
	count = utility.database.BrickDatabase.GetValue(interaction.guild, "economy", "discord_id", interaction.user.id, "money") or 0
	await interaction.response.send_message(f"Your money: { count }", ephemeral = True)

wallet = app_commands.Command(name = "wallet", description = "Tells how much money you have.", callback = GetMoney)