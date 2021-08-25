from mcdreforged.api.all import *
import material_list_helper.constants as constants
import os

def commandList(scr, context):
	material_list = os.listdir(constants.list_path)
	cnt = 0
	for i in material_list:
		if i.endswith(".json"):
			cnt += 1
			scr.reply(i)
	scr.reply("共找到 " + str(cnt) + " 个材料列表")