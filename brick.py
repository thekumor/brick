# ===============================================================
#
#	Logs the bot. Listens for events.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import json

from commands import ping, register, chars, leaderboard, daily, throw, members
import utility.database
import utility.locale

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

class Client(discord.Client):
	def __init__(self):
		intents = discord.Intents.default()
		intents.message_content = True
		intents.members = True
		super().__init__(intents = intents)

		self.tree = app_commands.CommandTree(self)

		utility.database.CreateGlobalDatabase()
		utility.locale.CreateGlobalLanguage()

		with open("settings.json") as settings:
			self.Settings = json.load(settings)

	async def on_ready(self):
		utility.database.BrickDatabase.Create(self)

	async def setup_hook(self):
		self.tree.add_command(ping.ping)
		self.tree.add_command(register.register)
		self.tree.add_command(chars.chars)
		self.tree.add_command(leaderboard.leaderboard)
		self.tree.add_command(daily.daily)
		self.tree.add_command(throw.throw)
		self.tree.add_command(members.members)

		await self.tree.sync()

	async def on_message(self, message):
		if message.author.bot:
			return
		
		# --------------------------------------------------------
		#	#Section: Character stats
		# --------------------------------------------------------
		oldValue = utility.database.BrickDatabase.GetValue(message.guild, "users", "discord_id", message.author.id, "char_count") or 0
		newValue = oldValue + len(message.clean_content)

		utility.database.BrickDatabase.SetValue(message.guild, "users", "discord_id", message.author.id, "char_count", newValue)

		# --------------------------------------------------------
		#       #Section: Message logging
		# --------------------------------------------------------
		guildSettings = self.Settings[str(message.guild.id)]

		if guildSettings is not None:
			channel = guildSettings["LogChannel"]
			if channel is not None:
				link = message.jump_url
				serverLanguage = guildSettings["Language"]

				embed = discord.Embed(title = utility.locale.Locale("locale_message", serverLanguage), description = "", color = 0xffffff)
				embed.add_field(name = utility.locale.Locale("locale_content", serverLanguage), value = message.content, inline = False)
				embed.add_field(name = utility.locale.Locale("locale_channel", serverLanguage), value = message.channel.name, inline = False)
				embed.add_field(name = utility.locale.Locale("locale_link", serverLanguage), value = "[here](" + link + ")", inline = False)
				embed.set_author(name = message.author.name, icon_url = message.author.avatar.url)
				embed.timestamp = message.created_at
				channelObj = await self.fetch_channel(str(channel))
				if channelObj is not None:
					await channelObj.send(embed = embed)


client = Client()
client.run(TOKEN)