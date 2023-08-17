# Author: Hong Sheng Liu
# Date: 2023-07-04
# Version: 1.0
import json
import os
import DataExtractor
def extract_features(json_folder, output_file):
    extracted_features = []
    i=0
    # 遍历文件夹中的所有JSON文件
    for file_name in os.listdir(json_folder):
        if file_name.endswith('.json'):
            file_path = os.path.join(json_folder, file_name)
            extractor=DataExtractor.DataExtractor(file_path)
            # 提取每个JSON文件的第一个数据
            if extractor.data and len(extractor.data) >= 1:
                first_item = extractor.data[0]
                # 对键和值进行重命名处理
                # 将下面的代码替换为你对键和值的具体处理逻辑
                try:
                    Number_of_Senwords=extractor.extract_Number_of_Senwords()
                except:
                    Number_of_Senwords=0
                Number_of_URL=extractor.extract_Number_of_URL()
                if Number_of_URL==0:
                    Has_URL=0
                else:
                    Has_URL=1
                processed_item = {
                    'feature':{
                        'Has_Picture':extractor.extract_Has_Picture(),
                        'Number_of_Senwords': Number_of_Senwords,
                        'Has_URL': Has_URL,
                        'Number_of_Comment': extractor.extract_Number_of_Comment(),
                        'User_Type':extractor.extract_User_Type(),
                        'TimeSpan':extractor.extract_RegisAge(),
                        'Number_of_Followers': extractor.extract_Number_of_Followers(),
                        'Number_of_posts': extractor.extract_Number_of_posts(),
                        'Number_of_reposts':extractor.extract_Number_of_reposts(),
                        'Number_of_Followees':extractor.extract_Number_of_Followees(),
                        'Isverified':extractor.extract_User_Type(),
                        'Has_Description':extractor.extract_Userhas_Description(),
                        'User_Gender':extractor.extract_Gender(),
                        'RegisTime':extractor.extract_RegisTime()
                    }

                    # ...
                }
                extracted_features.append(processed_item)
    # 写入提取后的数据到新的JSON文件中
    with open(output_file, 'w',encoding='utf8') as output_json:
        json.dump(extracted_features, output_json)


json_folder = 'E:\Rumor\weibo\\rumdect\Weibo'
output_file = 'E:\Rumor\weibo\\rumdect\output_SVMRBF.json'

extract_features(json_folder, output_file)