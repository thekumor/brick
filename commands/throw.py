# ===============================================================
#
#	Throws a brick at someone.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands, Permissions
import discord
import utility.database

async def Throw(interaction: discord.Interaction, target: discord.Member):
	await interaction.response.send_message(f"{interaction.user.mention} threw a brick at {target.mention}!")

register = app_commands.Command(name = "throw", description = "Throws a brick at someone.", callback = Throw)