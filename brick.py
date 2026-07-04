# ===============================================================
#
#	Logs the bot.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ===============================================================

import discord
from discord import app_commands
import os
from dotenv import load_dotenv

from commands import ping, register, chars, leaderboard, daily, throw
import utility.database

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

	async def on_ready(self):
		utility.database.BrickDatabase.Create(self)

	async def setup_hook(self):
		self.tree.add_command(ping.ping)
		self.tree.add_command(register.register)
		self.tree.add_command(chars.chars)
		self.tree.add_command(leaderboard.leaderboard)
		self.tree.add_command(daily.daily)
		self.tree.add_command(throw.throw)

		await self.tree.sync()

	async def on_message(self, message):
		if message.author.bot:
			return
		
		oldValue = utility.database.BrickDatabase.GetValue(message.guild, "users", "discord_id", message.author.id, "char_count") or 0
		newValue = oldValue + len(message.clean_content)

		utility.database.BrickDatabase.SetValue(message.guild, "users", "discord_id", message.author.id, "char_count", newValue)

client = Client()
client.run(TOKEN)