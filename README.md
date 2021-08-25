## Material List Helper (for MCDR) 材料列表共享  
Mateial List Helper (简称 MLH) 是一个可以全服共享由投影([Litematica mod](https://www.curseforge.com/minecraft/mc-mods/litematica))导出的材料列表文件(.csv)，方便多名玩家共同准备材料的MCDR插件。  
目前版本v0.0.1，功能尚且不全，Bug尚且多多，请凑合着用:(  
### 食用方法  
#### 食用准备  
1. 将`MaterialListHelper.py`文件放到你的MCDR的指定插件目录下。
2. 在同一个目录下建立文件夹`\material_list_helper\material_list`
3. 使用投影导出材料列表文件 (选择导出.csv文件)，然后将这个文件放到上述目录中，并且重命名成一个简短的名字
  
#### 食用指令  
1. `!!mlh help`: 查看帮助  
2. `!!m lh list`: 查看可用的材料列表文件列表  
3. `!!mlh <file_name> reset`: 重置指定材料列表 (file_name中不含后缀.csv)  
4. `!!mlh <file_name> show`: 显示指定材料列表  
5. `!!mlh <file_name> finish <material_name>`: 将指定材料列表中的指定材料标为已完成，比方说`!!mlh test finish 黑曜石`
