# ===============================================================
#
#	Runs an AI response.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands, Permissions
import discord

async def AI(interaction: discord.Interaction, what: str):
	await interaction.response.send_message(f"Test: {str}!")

ai = app_commands.Command(name = "ai", description = "Runs an AI response.", callback = AI)