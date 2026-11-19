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

async def TranslateMessage(interaction: discord.Interaction, id: str, language: str):
	translator = Translator(to_lang=language)
	message = await interaction.channel.fetch_message(id)
	text = message.content
	translation = translator.translate(text)
	await interaction.response.send_message(translation)

translateMessage = app_commands.Command(name = "translate_msg", description = "Translates a message.", callback = TranslateMessage)