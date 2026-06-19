# ================================================================
#
#	Shows user leaderboard for a particular server.
#
#	#Module: Stats
#	#Component: Leaderboard
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

from discord import app_commands
import utility.database

async def ShowLeaderboard(interaction):
	charCounts = utility.database.BrickDatabase.GetValues(interaction.guild, "users", ["discord_id", "char_count"], "char_count") or []

	i = 1
	lines = []
	for tuple in charCounts:
		userId = tuple[0]
		charCount = tuple[1]

		member = interaction.guild.get_member(userId)

		if member is not None:
			lines.append("### #" + str(i) + ": " + member.name + " - " + str(charCount) + "\n")
			i += 1

		if i > 20:
			break

	leaderboardMessageString = "".join(lines)
	leaderboardMessageString = f"# === {interaction.guild.name} Leaderboard ===\n" + leaderboardMessageString

	await interaction.response.send_message(leaderboardMessageString, ephemeral = False)

leaderboard = app_commands.Command(name="leaderboard", description="Shows user leaderboard.", callback = ShowLeaderboard)