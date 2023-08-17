# Author: Hong Sheng Liu
# Date: 2023-06-29
# Version: 2.0

import os
import re
import json

result_data = []

# Open the txt file and read the data line by line
with open(r'E:\Rumor\weibo\rumdect\Weibo.txt', 'r') as txt_file:
    for line in txt_file:
        # Regularly match each row to find the required information
        match_obj = re.findall(r'eid:(\d+)\s+label:(\d+)', line)
        if match_obj:
            eid = match_obj[0][0]
            label = match_obj[0][1]
            # Save results in a list
            result_data.append(label)
# 打开JSON文件
with open('E:\Rumor\weibo\\rumdect\output_SVMRBF.json', 'r') as file:
    data = json.load(file)
# 遍历每个项目，并为其添加label键
    for i in range(0,len(data)):
        label = result_data[i]
        data[i]['label'] = label

# 保存修改后的JSON数据到文件
with open('E:\Rumor\weibo\\rumdect\output_SVMRBF2.json', 'w') as file:
    json.dump(data, file, indent=2)