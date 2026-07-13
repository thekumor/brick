# ===============================================================
#
#	Displays how many people are on the server.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands

members = app_commands.Command(name = "members", description = "Displays how many people are on the server.", callback = lambda interaction: interaction.response.send_message(f"Member count: {interaction.guild.member_count}"))