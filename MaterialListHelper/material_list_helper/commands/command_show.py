from mcdreforged.api.all import *
import material_list_helper.constants as constants
import json

def commandShow(scr, context):
	if scr.get_permission_level() < constants.min_permission_level_for_show:
		scr.reply(constants.no_permission_message)
		pass
	data = json.load(open(constants.list_path + context["file_name"] + ".json", "r") )
	for i in data:
		rep = ""
		if i["finished"] == 1:
			rep = rep + "【已完成】" + constants.grey
		else:
			rep = rep + "【未完成】" + constants.green
		rep = rep + "[" + i["name"] + "]: " + str(i["amount"] ) + " | " + constants.light_blue + getMCNumStr(i["amount"], 64) + "| " + constants.yellow + "投身于此的玩家: "
		if len(i["preparing_players"]) == 0:
			rep = rep + "无"
		else:
			for player in i["preparing_players"]:
				rep = rep + player + " "
		scr.reply(rep)

# from a interger to a string base by Minecraft number
def getMCNumStr(num, per_group):
	ret = ""
	if int(num / (27 * per_group) ) > 0:
		ret = ret + str(int(num / (27 * per_group) ) ) + "盒 "
	if int( (num % (27 * per_group) ) / per_group) > 0:
		ret = ret + str( int( (num % (27 * per_group) ) / per_group) ) + "组 "
	if num % 64 > 0:
		ret = ret + str(int(num % 64) ) + "个 "
	return ret