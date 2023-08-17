# Author: Hong Sheng Liu
# Date: 2023-07-23
# Version: 1.0
import os
import json
folder_path ='E:\\rumordetection\RUMOUREVAL2019\\rumoureval2019.tar\\rumoureval-2019-test-data\\twitter-en-test-data'
output_file ='E:\\rumordetection\RUMOUREVAL2019\\rumoureval2019.tar\\rumoureval-2019-test-data\\twitter-en-test-data\output.json'
with open('E:\\rumordetection\RUMOUREVAL2019\\rumoureval2019.tar\\final-eval-key.json', "r") as file:
    json_label = json.load(file)
# 遍历文件夹
json_data = []
for folder_name in os.listdir(folder_path):
    folder_dir = os.path.join(folder_path, folder_name)
    contents = os.listdir(folder_dir)
    for item in contents:
        item_path = os.path.join(folder_dir, item)
        folder_number = str(item)
        source_tweets_dir =os.path.join(item_path,'source-tweet')
        file_path=os.path.join(source_tweets_dir,folder_number+'.json')
        with open(file_path, "r") as file:
            json_content = json.load(file)
        # 添加label字段
        label=json_label['subtaskbenglish'][folder_number]
        json_content["label"] = label
        json_data.append(json_content)
# 将数据写入新的json文件
with open(output_file, "w") as file:
    json.dump(json_data, file)
