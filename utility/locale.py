# ================================================================
#
#	Handles language's JSON values.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# ================================================================

import json

Language = None
def CreateGlobalLanguage():
	global Language

	with open("locale.json") as loc:
		Language = json.load(loc)

def Locale(name, lang, fallback = "heh"):
	if Language[name] is not None:
		return Language[name][lang]
	
	return fallback