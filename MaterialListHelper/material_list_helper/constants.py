# many constants are defined here

import os

color_char = "§" # Minecraft color char
black = color_char + "0"
blue = color_char + "1"
green = color_char + "2"
light_green = color_char + "3"
red = color_char + "4"
purple = color_char + "5"
yellow = color_char + "6"
white = color_char + "7"
grey = color_char + "8"
light_blue = color_char + "9"
light_red = color_char + "C"
light_purple = color_char + "D"
light_yellow = color_char + "E"
light_white = color_char + "F"

message_on_load = "MaterialListHelper is going to start..." # a message showed when load
message_on_register_commands = "Register commands..." # also
message_on_register_help_message = "Register help messages..." # also
help_message = "输入!!mlh获得帮助, 或者访问 https://github.com/skimitmc/MaterialListHelper4MCDR 阅读README.md" # a message showed when !!help
reset_message = "已重置" # a message showed when !!mlh <file_name> reset
add_message = "已添加"

basic_change_permission_level = 1 # permission level
basic_query_permission_level = 0 # also
min_permission_level_for_show = basic_query_permission_level # also
min_permission_level_for_finish = basic_change_permission_level # also
min_permission_level_for_unfinish = basic_change_permission_level # also
min_permission_level_for_reset = basic_change_permission_level # also
min_permission_level_for_help = basic_query_permission_level # also
min_permission_level_for_list = basic_query_permission_level # also  
min_permission_level_for_add = 3 # also
min_permission_level_for_tpi = basic_change_permission_level # also
no_permission_message = red + "你没有权限qwq"

list_path =  os.path.dirname(os.path.abspath(__file__) ) + "\\material_list_helper\\material_list\\" # where the json files