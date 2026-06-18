# ================================================================
#
#	Creates a ping/pong command.
#
#	#License: GPL-2.0-only
#	#Authors: The Kumor
#
# =================================================================

from discord import app_commands

ping = app_commands.Command(name="ping", description="Pings the bot.", callback = lambda interaction: interaction.response.send_message("Pong!"))