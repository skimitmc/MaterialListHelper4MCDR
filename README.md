## Material List Helper (for [MCDR](https://github.com/Fallen-Breath/MCDReforged)) 材料列表共享  
Mateial List Helper (简称 MLH) 是一个可以全服共享由投影([Litematica mod](https://www.curseforge.com/minecraft/mc-mods/litematica))导出的材料列表文件(.csv)，方便多名玩家共同准备材料的[MCDR](https://github.com/Fallen-Breath/MCDReforged)插件。  
目前版本v0.1.1，功能尚且不全，Bug尚且多多，请凑合着用:(      
#### 食用指令  
1. `!!mlh help`: 查看帮助  
2. `!!mlh list`: 查看可用的材料列表文件列表  
3. `!!mlh <file_name> reset`: 重置指定材料列表 (file_name中不含后缀) 
4. `!!mlh <file_name> show`: 显示指定材料列表 (除了十进制的数量之外，还会显示已MC中的单位计算的数量，暂时无法处理一组不是64个的物品)  
5. `!!mlh <file_name> finish <material_name>`: 将指定材料列表中的指定材料标为已完成，比方说`!!mlh test finish 黑曜石`
6. `!!mlh <file_name> unfinish <material_name>`: 将指定材料列表中的指定材料标记为未完成  
7. `!!mlh <file_name> tpi <material_name>`: 表示你参加指定材料列表中指定材料的准备  
8. `!!mlh add <path> <file_name>`: 从指定的绝对路径`<path>`指向的csv导入材料列表，导入后的名称为`<file_name>`。比方说 `!!mlh add E:\HWF\qwq.csv qwq`，然后你可以用 `!!mlh show qwq`来查看
- **注意，由于某种原因，路径中不能含有空格**
- **务必将csv文件转换到服务器运行的系统的默认编码**
