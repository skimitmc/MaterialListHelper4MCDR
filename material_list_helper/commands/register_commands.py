import material_list_helper.constants as constants
import material_list_helper.commands.command_finish as command_finish
import material_list_helper.commands.command_help as command_help
import material_list_helper.commands.command_list as command_list
import material_list_helper.commands.command_reset as command_reset
import material_list_helper.commands.command_show as command_show
import material_list_helper.commands.command_unfinish as command_unfinish
import material_list_helper.commands.command_add as command_add
import material_list_helper.commands.command_tpi as command_tpi
from mcdreforged.api.all import *

def registerCommands(server, prev):
	server.register_command(
		Literal("!!mlh").
		runs(command_help.commandHelp).
		then(
			Literal("help").
			runs(command_help.commandHelp)
		).
		then(
			Literal("list").
			runs(command_list.commandList)
		).
		then(
			Text("file_name").
			then(
				Literal("show").
				runs(command_show.commandShow)
			).
			then(
				Literal("finish").
				then(
					Text("material_name").
					runs(command_finish.commandFinish)
				)
			).
			then(
				Literal("unfinish").
				then(
					Text("material_name").
					runs(command_unfinish.commandUnfinish)
				)
			).
			then(
				Literal("tpi").
				then(
					Text("material_name").
					runs(command_tpi.commandTpi)
				)
			).
			then(
				Literal("reset").
				runs(command_reset.commandReset)
			)
		).
		then(
			Literal("add").
			then(
				Text("path").
				then(
					Text("file_name").
					runs(command_add.commandAdd)
				)
			)
		)
	)