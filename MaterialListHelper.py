import os
import csv
from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'material_list_helper',
    'version': '0.0.3',
    'name': 'MaterialListHelper',
    'description': 'A plugin to help the players collect materials for a project together',
    'author': 'yggdyy_',
    'link': 'https://github.com/skimitmc/MaterialListHelper4MCDR',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}

current_path = os.path.dirname(os.path.abspath(__file__)) # the path this py file in
material_file_path = current_path + "\\material_list_helper\\material_list\\" # the path that the material list file (.csv) should be in
color_char = "§"

# the listener will work when this plugin reload of load
def on_load(server, prev):
    server.logger.info("MaterialListHelper is now goig to start...")

    server.logger.info("Register commands...")    
    server.register_command(
        Literal("!!mlh").
        runs(command_help).
        then(
            Literal("help").
            runs(command_help)
        ).
        then(
            Literal("list").
            runs(command_list)
        ).
        then(
            Text("file_name").
            then(
                Literal("show").
                runs(command_show)
            ).
            then(
                Literal("finish").
                then(
                    Text("material_name").
                    runs(command_finish)
                )
            ).
            then(
                Literal("reset").
                runs(command_reset)
            )
        )
    )

    server.logger.info("Register help message...")
    server.register_help_message("!!mlh", "输入!!mlh获得帮助, 或者访问 https://github.com/skimitmc/MaterialListHelper4MCDR 阅读README.md")

# command !!mlh <file_name> show
def command_show(scr, context):
    file_path = material_file_path + context["file_name"] + ".csv"
    material_list = getMaterialList(file_path)
    for i in material_list:
        if i[2] == "True": # this type of material has been collected
            ch = "【已完成】" + color_char + "8"
            scr.reply(ch + "[" + i[0] + "]: " + i[1] + " | " + color_char + "7标记者: " + i[3])
        else:
            ch = "【未完成】" + color_char + "2"
            scr.reply(ch + "[" + i[0] + "]: " + i[1] + color_char + "7 [" + getMCNum(int(i[1]), 64) + "]")

# command !!mlh <file_name> finish <material_name>
def command_finish(scr, context):
    if scr.get_permission_level() < 1:
        scr.reply("权限不足, 请联系服务器管理人员")
        pass
    file_path = material_file_path + context["file_name"] + ".csv"
    rows = [row for row in csv.reader(open(file_path, "r"))]
    for i in rows:
        if(len(i) < 4 or i[0] == "Item"):
            continue
        if(i[0] == context["material_name"]):
            i[2] = "True"
            if scr.is_player:
                i[3] = scr.player
            else:
                i[3] = "The Console"
    with open(file_path, "w") as csv_file:
        new_material_list = csv.writer(csv_file)
        for i in rows:
            if(len(i) < 4 or i[0] == "Item"):
                continue
            new_material_list.writerow(i)
    scr.reply("修改已完成")

# command !!mlh <file_name> reset
def command_reset(scr, context):
    if scr.get_permission_level() < 1:
        scr.reply("权限不足, 请联系服务器管理人员")
        pass
    file_path = material_file_path + context["file_name"] + ".csv"
    rows = [row for row in csv.reader(open(file_path, "r"))]
    for i in rows:
        if(len(i) < 4 or i[0] == "Item"):
            continue
        i[2] = "False"
        i[3] = ""
    with open(file_path, "w") as csv_file:
        new_material_list = csv.writer(csv_file)
        for i in rows:
            if(len(i) < 4 or i[0] == "Item"):
                continue
            new_material_list.writerow(i)
    scr.reply("已重置")
    
# command !!mlh help or !!mlh
def command_help(scr, context):
    scr.reply("--------------Material List Helper 材料列表共享 【帮助】--------------")
    scr.reply("|插件功能：读取指定目录下的材料列表文件(投影导出的.csv文件), 进行全服共享|")
    scr.reply("|方便多人收集材料。                                                  |")
    scr.reply("|提醒：本插件目前处于测试阶段，功能不全，拥有大量Bug :(                 |")
    scr.reply("|命令帮助：                                                         |")
    scr.reply("| !!mhl 或 !!mhl help: 显示这些帮助信息                              |")
    scr.reply("| !!mhl list: 显示可以查看的材料列表文件的列表                        |")
    scr.reply("| !!mhl <file_name> show: 显示指定的材料列表 (file_name不含文件后缀)  |")
    scr.reply("| !!mhl <file_name> finish <material_name>: 表示指定列表中的指定材料已|")
    scr.reply("| 收集完成 (material_name应当于show指令中显示的材料名称相同)           |")
    scr.reply("| !!mhl <file_name> reset: 重置指定列表                              |")
    scr.reply("#####################################################################")

# command !!mlh list
def command_list(scr, context):
    material_list = getMaterialFileList()
    scr.reply("共找到 " + str(len(material_list) ) + " 个文件")
    for i in material_list:
        scr.reply(i)

# Get the file list under the path ~/meterial_list_helper/material_list
def getMaterialFileList(): 
    material_file_list = os.listdir(material_file_path)
    return material_file_list

# material_list is a csv file (.csv)
# Get the list which likes [["", "", "True"/"False"], ["", "", "True"/"False"], ...]
def getMaterialList(material_list_file):
    material_list = [row for row in csv.reader(open(material_list_file, "r"))]
    ret = []
    for i in material_list:
        if len(i) < 4 or i[0] == "Item":
            continue
        ret.append( [i[0], i[1], i[2], i[3]] )
    return ret

def getMCNum(num, per_group):
    ret = str(int(num / (27 * per_group) ) ) + "盒 " + str(int(num % (27 * per_group) / per_group) ) + "组 " + str(int(num % per_group) ) + "个"
    return ret