# ===============================================================
#
#	Translates a message.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

from discord import app_commands, Permissions
import discord
from translate import Translator

async def Translate(interaction: discord.Interaction, id: str):
    translator = Translator(to_lang="pl")
    text = await interaction.fetch_message(id)
    translation = translator.translate(text)
    await interaction.response.send_message(translation)

translateMessage = app_commands.Command(name = "translate_message", description = "Translates a message.", callback = Translate)