# ================================================================
#
#	Creates databases for all servers the bot is in.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ================================================================

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
	
	def GetRows(self):
		return self.cursor.fetchall()


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
			);
			""", True)

			connection.Do("""
			CREATE TABLE IF NOT EXISTS economy(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				discord_id INTEGER,
				money INTEGER,
				last_daily BIGINT
			);
			""", True)

	def SetValue(self, guild, table, column, expected, key, value):
		connection = self.GetConnection(guild)

		if connection is not None:
			connection.Do(f"UPDATE {table} SET {key} = {value} WHERE {column} = {expected}", True)

	def SetValues(self, guild, table, column, expected, keys, values):
		connection = self.GetConnection(guild)

		if connection is not None:
			format = ""
			for i in enumerate(values):
				format += keys[i] + " = " + values[i] + ", "

			connection.Do(f"UPDATE {table} SET {format} WHERE {column} = {expected}", True)

	def NewEntry(self, guild, table, keys, values):
		connection = self.GetConnection(guild)

		if connection is not None:
			formatValues = "".join(str(x) + ", " for x in values)[:-2]
			formatKeys = "".join(str(x) + ", " for x in keys)[:-2]

			connection.Do(f"""
			INSERT INTO {table}({formatKeys}) VALUES({formatValues});
			 """, True)

	def GetValue(self, guild, table, column, expected, key):
		connection = self.GetConnection(guild)

		if connection is not None:
			connection.Do(f"SELECT {key} FROM {table} WHERE {column} = {expected};")

			row = connection.GetRow()

			if row is None:
				return None
			
			return row[0]
		
		return None
	
	def GetValues(self, guild, table, column, expected, keys):
		connection = self.GetConnection(guild)

		if connection is not None:
			formatKeys = "".join(str(x) + ", " for x in keys)[:-2]

			connection.Do(f"SELECT {formatKeys} FROM {table} WHERE {column} = {expected};")

			rows = connection.GetRows()
			return rows
		
		return None
	
	def GetValuesByOrder(self, guild, table, columns, orderColumn):
		connection = self.GetConnection(guild)

		if connection is not None:
			formatColumns = "".join(str(x) + ", " for x in columns)[:-2]

			connection.Do(f"SELECT {formatColumns} FROM {table} ORDER BY {orderColumn} DESC;")

			rows = connection.GetRows()
			return rows
		
		return None
	
	def IncrementValue(self, guild, table, column, expected, key):
		value = self.GetValue(guild, table, column, expected, key)

		if value is not None:
			self.SetValue(guild, table, column, key, int(value) + 1)

BrickDatabase = None
def CreateGlobalDatabase():
	global BrickDatabase
	BrickDatabase = Database()