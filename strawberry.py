import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class Client(discord.Client):
	async def on_ready(self):
		print(f'Logged in as {self.user} (ID: {self.user.id})')
		print('------')

	async def on_message(self, message):
		if message.author == self.user:
			return

		if message.content.startswith('!hello'):
			await message.channel.send('Hello!')
	
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)