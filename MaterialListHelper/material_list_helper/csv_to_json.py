import csv
import json
import os

# this plugin need a json like [{"name": "...", "amount": xx, "finished": 1 or 0, "preparing_players": ["player1", "player2", ...]}, ...]

# make the csv_file to a json file in the path
# for example, csvToJson(open("D:\HWFAKIOI\HWF.csv", "r"), "D:\HWFAKIOI\HWF.json")
# this can only be used when the csv file is new to the plugin
def csvToJson(csv_file, file_path):
	data = []
	rows = [row for row in csv.reader(csv_file) ]
	for row in rows:
		if(len(row) < 4 or row[0] == "Item"):
			continue
		new_dict = {
			"name": row[0], 
			"amount": int(row[1]), 
			"finished": 0, 
			"preparing_players": []
		}
		data.append(new_dict)
	with open(file_path, "w") as f:
		f.write(json.dumps(data) )

# csvToJson(open("E:\\MCDReforged-master\\plugins\\material_list_helper\\material_list\\farm.csv", "r"), "E:\\MCDReforged-master\\plugins\\material_list_helper\\material_list\\farm.json")
# a test line :)