from mcdreforged.api.all import *

def commandHelp(scr, context):
	scr.reply("""
--------------Material List Helper 材料列表共享 【帮助】--------------
|插件功能：读取指定目录下的材料列表文件(投影导出的.csv文件), 进行全服共享|
|方便多人收集材料。                                                  |
|提醒：本插件目前处于测试阶段，功能不全，拥有大量Bug :(                 |
|命令帮助：                                                         |
| !!mlh 或 !!mlh help: 显示这些帮助信息                              |
| !!mlh list: 显示可以查看的材料列表文件的列表                        |
| !!mlh <file_name> show: 显示指定的材料列表 (file_name不含文件后缀)  |
| !!mlh <file_name> finish <material_name>: 表示指定列表中的指定材料已|
| 收集完成 (material_name应当于show指令中显示的材料名称相同)           |
| !!mlh <file_name> unfinish <material_name>: 表示收集未完成         |
| !!mlh <file_name> reset: 重置指定列表                              |
| !!mlh <file_name> tpi <material>: 表示你参加这一项材料的收集        |
| !!mlh add <path> <file_name>: 从指定绝对目录(不能含有空格)导入csv文件|
| 并且保存为指定的名称, 如 !!mlh E:\\HwF\\qwq.csv qwq                 |
#####################################################################
	""")