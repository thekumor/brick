# ================================================================
#
#	Creates databases for all servers the bot is in.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

import sqlite3
import os

class Connection:
	def __init__(self, guildId, path):
		self.guildId = guildId
		self.connection = sqlite3.connect(path)
		self.cursor = self.Cursor()

	def __del__(self):
		self.connection.close()
		self.cursor.close()

	def Cursor(self):
		return self.connection.cursor()

	def Do(self, cmd, commit = False):
		self.cursor.execute(cmd)

		if commit:
			self.connection.commit()

	def GetRow(self):
		return self.cursor.fetchone()


class Database:
	def __init__(self):
		self.connections = []
		self.path = "/var/brick"

	def GetFolderPath(self):
		return os.path.join(self.path, "databases")

	def GetPath(self, guild):
		return os.path.join(self.GetFolderPath(), f"{guild.id}.db")

	def GetConnection(self, guild):
		for connection in self.connections:
			if connection.guildId == guild.id:
				return connection
			
		return None

	def Create(self, bot):
		dir = self.GetFolderPath()

		if not os.path.exists(dir):
			os.mkdir(dir)

		for guild in bot.guilds:
			connection = Connection(guild.id, self.GetPath(guild))
			self.connections.append(connection)

			connection.Do("""
			CREATE TABLE IF NOT EXISTS users (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				discord_id INTEGER,
				char_count INTEGER
			)
			""", True)

	def SetValue(self, guild, table, id, key, value):
		connection = self.GetConnection(guild)

		if connection is not None:
			connection.Do(f"UPDATE {table} SET {key} = {value} WHERE id = {id}", True)

	def GetValue(self, guild, table, id, key):
		connection = self.GetConnection(guild)

		if connection is not None:
			connection.Do(f"SELECT {key} FROM {table} WHERE id = {id}")

			row = connection.GetOne()

			if row is None:
				return None

			return row[0]
		
		return None
	
	def IncrementValue(self, guild, table, id, key):
		value = self.GetValue(self, guild, table, id, key)

		if value is not None:
			self.SetValue(self, guild, table, id, key, int(value) + 1)