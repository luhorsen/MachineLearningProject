# Author: Hong Sheng Liu
# Date: 2023-07-15
# Version: 1.0
import os
import json

# 设置文件夹路径和新的json文件名
folder_path = "E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\\rumours"
output_file = "E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\output.json"

# 遍历文件夹
json_data = []
for folder_name in os.listdir(folder_path):
    if not folder_name.isdigit():
        continue

    folder_dir = os.path.join(folder_path, folder_name)
    source_tweets_dir = os.path.join(folder_dir, "source-tweets")

    # 遍历source-tweets文件夹
    for filename in os.listdir(source_tweets_dir):
        if not filename.startswith(folder_name) or not filename.endswith(".json"):
            continue

        file_path = os.path.join(source_tweets_dir, filename)

        # 读取json数据
        with open(file_path, "r") as file:
            json_content = json.load(file)

        # 添加label字段
        json_content["label"] = 1

        # 添加到列表中
        json_data.append(json_content)

# 将数据写入新的json文件
with open(output_file, "w") as file:
    json.dump(json_data, file)

