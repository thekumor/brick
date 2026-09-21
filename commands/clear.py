# ===============================================================
#
#	Clears everyone's character count on the server.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands, Permissions
import utility.database

async def ClearUsers(interaction):
	utility.database.BrickDatabase.SetValues(interaction.guild, "users", "", "", {"char_count"}, {0})

	await interaction.response.send_message(f"Cleared all users successfully.", ephemeral = False)

clear = app_commands.Command(name = "clear", description = "Clears everyone's character count on the server.", callback = ClearUsers)
clear.default_permissions = Permissions(administrator = True)