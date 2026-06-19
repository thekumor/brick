# ================================================================
#
#	Logs the bot.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

import discord
from discord import app_commands
import os
from dotenv import load_dotenv

from commands import ping, register, chars
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
		print(f"Logged in as {self.user} (ID: {self.user.id})")
		print("------")
		
		utility.database.BrickDatabase.Create(self)

	async def setup_hook(self):
		self.tree.add_command(ping.ping)
		self.tree.add_command(register.register)
		self.tree.add_command(chars.chars)
		await self.tree.sync()

	async def on_message(self, message):
		if message.author.bot:
			return

client = Client()
client.run(TOKEN)