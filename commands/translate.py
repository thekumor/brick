# ===============================================================
#
#	Translates text.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands, Permissions
import discord
from translate import Translator

async def Translate(interaction: discord.Interaction, text: str):
    translator = Translator(to_lang="pl")
    translation = translator.translate(text)
    await interaction.response.send_message(translation)

translate = app_commands.Command(name = "translate", description = "Translates text.", callback = Translate)