from mcdreforged.api.all import *
import json
import material_list_helper.constants as constants

def commandUnfinish(scr, context):
	if scr.get_permission_level() < constants.min_permission_level_for_unfinish:
		scr.reply(constants.no_permission_message)
		pass
	data = json.load(open(constants.list_path + context["file_name"] + ".json", "r") )
	for i in data:
		if i["name"] == context["material_name"]:
			i["finished"] = 0
	with open(constants.list_path + context["file_name"] + ".json", "w") as f:
		f.write(json.dumps(data) )
	scr.reply("已更改")