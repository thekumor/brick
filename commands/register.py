# ================================================================
#
#	Registers every user on the server for database (omits bots).
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

from discord import app_commands, Permissions
import utility.database

async def RegisterUsers(interaction):
	amount = 0

	for member in interaction.guild.members:
		if member.bot:
			continue
		
		added = False

		if utility.database.BrickDatabase.GetValue(interaction.guild, "users", "discord_id", member.id, "*") is None:
			utility.database.BrickDatabase.NewEntry(interaction.guild, "users", ["discord_id", "char_count"], [member.id, 0])
			added = True

		if utility.database.BrickDatabase.GetValue(interaction.guild, "economy", "discord_id", member.id, "*") is None:
			utility.database.BrickDatabase.NewEntry(interaction.guild, "economy", ["discord_id", "money"], [member.id, 0])
			added = True

		if added:
			amount += 1

	await interaction.response.send_message(f"Registered all {amount} users successfully.", ephemeral = True)

register = app_commands.Command(name="register", description="Registers everybody.", callback = RegisterUsers)
register.default_permissions = Permissions(administrator = True)