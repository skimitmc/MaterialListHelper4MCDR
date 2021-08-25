from mcdreforged.api.all import *
import material_list_helper.constants as constants
import json

def commandReset(scr, context):
	if scr.get_permission_level() < constants.min_permission_level_for_reset:
		scr.reply(constants.red + constants.no_permission_message)
		pass
	data = json.load(open(constants.list_path + context["file_name"] + ".json", "r") )
	for i in data:
		i["finished"] = 0
		i["preparing_players"] = []
	with open(constants.list_path + context["file_name"] + ".json", "w") as f:
		f.write(json.dumps(data))
	scr.reply(constants.reset_message)