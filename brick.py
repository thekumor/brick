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
from utility.database import Database

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class Client(discord.Client):
	def __init__(self):
		intents=discord.Intents.default()
		intents.message_content = True
		super().__init__(intents=intents)

		self.tree = app_commands.CommandTree(self)

	async def on_ready(self):
		print(f'Logged in as {self.user} (ID: {self.user.id})')
		print('------')

		db = Database()
		db.Create(self)

	async def setup_hook(self):
		self.tree.add_command(ping.ping)
		self.tree.add_command(register.register)
		self.tree.add_command(chars.chars)
		await self.tree.sync()
		

client = Client()
client.run(TOKEN)