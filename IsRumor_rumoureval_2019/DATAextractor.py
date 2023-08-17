# Author: Hong Sheng Liu
# Date: 2023-08-15
# Version: 1.0
import json
import os
import Extractor
def extract_features(json_folder, output_file):
    extracted_features = []
    extractor = Extractor.DataExtractor(json_folder)
    len=extractor.File_Length
    for index in range(len):
        if extractor.Read_Label(index)!=2:
            processed_item = {
                'feature': {
                    "Length_Characters":extractor.Get_Length_of_Characters(index),
                    "Length_Words":extractor.Get_Number_of_Words(index),
                    'Fraction_Of_Uppercase_Letters':extractor.Fraction_Of_Uppercase_Letters(index),
                    "Number_Of_Urls":extractor.extract_url_count(index),
                    'Is_Retweet':extractor.Is_retweet(index),
                    'Sentiment_Pos_Words':extractor.Extract_PosWords(index),
                    'Sentiment_Neg_Words':extractor.Extract_PosWords(index),
                    'User_Registration_Age':extractor.Get_Registration_Age(index),
                    'Number_Of_Followers':extractor.Get_Number_Of_Followers(index),
                    'Number_Of_Friends':extractor.Get_Number_Of_Friends(index),
                    'Is_Verfied':extractor.Is_Verified(index),
                    'Has_Description':extractor.Has_Description(index),
                },
                'label':extractor.Read_Label(index)
                # ...
            }
        extracted_features.append(processed_item)
        with open(output_file, 'w', encoding='utf8') as output_json:
            json.dump(extracted_features, output_json)
json_folder = 'E:\\rumordetection\RUMOUREVAL2019\\rumoureval2019.tar\\rumoureval-2019-test-data\\twitter-en-test-data\\output.json'
output_file = 'E:\\rumordetection\RUMOUREVAL2019\\dataset.json'

extract_features(json_folder, output_file)