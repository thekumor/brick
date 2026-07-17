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
	settings = Settings[interaction.guild.id]
	translation = utility.locale.Locale("locale_throw", settings["locale_throw"]) if settings is not None else "heh"

	await interaction.response.send_message(f"{interaction.user.mention} {translation} {target.mention}!")

throw = app_commands.Command(name = "throw", description = "Throws a brick at someone.", callback = Throw)