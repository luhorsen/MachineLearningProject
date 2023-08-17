# Author: Hong Sheng Liu
# Date: 2023-08-16
# Version: 1.0
import json


def merge_json_datasets(file1, file2, output_file):
    # 读取第一个JSON文件
    with open(file1, 'r') as f:
        dataset1 = json.load(f)

    # 读取第二个JSON文件
    with open(file2, 'r') as f:
        dataset2 = json.load(f)

    # 合并两个数据集
    merged_dataset = dataset1 + dataset2
    print(len(dataset1))
    print(len(dataset2))
    print(len(merged_dataset))
    # 写入合并后的JSON文件
    with open(output_file, 'w') as f:
        json.dump(merged_dataset, f)


# 使用示例
file1 = 'E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\dataset_nonroumour.json'
file2 = 'E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\dataset_roumor.json'
output_file = 'E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\dataset.json'
merge_json_datasets(file1, file2, output_file)