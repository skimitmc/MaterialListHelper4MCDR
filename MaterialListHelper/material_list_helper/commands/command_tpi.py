from mcdreforged.api.all import *
import json
import material_list_helper.constants as constants

def commandTpi(scr, context):
	if scr.get_permission_level() < constants.min_permission_level_for_tpi:
		scr.reply(constants.no_permission_message)
		pass
	Player = ""
	if scr.is_console:
		Player = "The Console"
	else:
		Player = scr.player
	data = json.load(open(constants.list_path + context["file_name"] + ".json", "r") )
	for i in data:
		if i["name"] == context["material_name"]:
			if Player in i["preparing_players"]:
				continue
			i["preparing_players"].append(Player)
	with open(constants.list_path + context["file_name"] + ".json", "w") as f:
		f.write(json.dumps(data) )
	scr.reply("已更改")