# ================================================================
#
#	Creates economy utility.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

from utility.database import BrickDatabase

def CreateEconomyTable():
	BrickDatabase.Do("""
	CREATE TABLE IF NOT EXISTS economy(
		id INTEGER PRIMARY KEY AUTO_INCREMENT,
		user_id INTEGER,
		money INTEGER,
	)
	""")