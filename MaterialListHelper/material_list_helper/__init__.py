import material_list_helper.commands.register_commands as register_commands
import material_list_helper.constants
from mcdreforged.api.all import *

def on_load(server, prev):
	server.logger.info(constants.message_on_load)

	server.logger.info(constants.message_on_register_commands)
	register_commands.registerCommands(server, prev)

	server.logger.info(constants.message_on_register_help_message)
	server.register_help_message("!!mlh", constants.help_message)