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
import utility.locale

async def Throw(interaction: discord.Interaction, target: discord.Member):
	language = interaction.client.Settings[str(interaction.guild.id)]
	translation = utility.locale.Locale("locale_throw", language)

	await interaction.response.send_message(f"{interaction.user.mention} {translation} {target.mention}!")

throw = app_commands.Command(name = "throw", description = "Throws a brick at someone.", callback = Throw)