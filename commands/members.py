# ===============================================================
#
#	Displays how many people are on the server.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands
import discord

async def Display(interaction: discord.Interaction, target: discord.Member):
	await interaction.response.send_message(f"Member count: { interaction.guild.members.count }")

members = app_commands.Command(name = "members", description = "Displays how many people are on the server.", callback = Display)