from mcdreforged.api.all import *
import material_list_helper.csv_to_json as ctj
import material_list_helper.constants as constants

def commandAdd(scr, context):
	if scr.get_permission_level() < constants.min_permission_level_for_add:
		scr.reply(constants.no_permission_message)
		pass
	ctj.csvToJson(open(context["path"], "r"), constants.list_path + context["file_name"] + ".json")
	scr.reply(constants.add_message)