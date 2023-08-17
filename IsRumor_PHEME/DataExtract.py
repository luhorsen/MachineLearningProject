# Author: Hong Sheng Liu
# Date: 2023-07-21
# Version: 1.0
import json
import os
import Extractor
def extract_features(json_folder, output_file):
    extracted_features = []
    extractor = Extractor.DataExtractor(json_folder)
    len=extractor.File_Length
    for index in range(len):
        processed_item = {
            'feature': {
                'Length_of_Characters':extractor.Get_Length_of_Characters(index),
                'Number_of_Words':extractor.Get_Number_of_Words(index),
                'Fraction_Of_Uppercase_Letters': extractor.Fraction_Of_Uppercase_Letters(index),
                'Sentiment_Score':extractor.Count_Sentiment_Score(index),
                "Number_Of_Urls": extractor.extract_url_count(index),
                'User_Registration_Age': extractor.Get_Registration_Age(index),
                'Number_Of_Followers': extractor.Get_Number_Of_Followers(index),
                'Is_Verfied': extractor.Is_Verified(index),
                'Statuses_Count':extractor.Get_Statuses_Count(index),
                'Number_Of_Poswords':extractor.Extract_PosWords(index),
                'Number_Of_Negwords':extractor.Extract_NegWords(index),
                'Number_Of_Friends':extractor.Get_Number_Of_Friends(index),
                'Contains_MultiMark':extractor.Ifcontains_MultiMark(index),
                'Has_personal_pronoun_1st':extractor.personal_pronoun_1st(index),
                'Has_personal_pronoun_2st':extractor.personal_pronoun_2st(index),
                'Has_personal_pronoun_3st':extractor.personal_pronoun_3st(index),

            },
            'label':"0",
            # ...
        }
        extracted_features.append(processed_item)
        with open(output_file, 'w', encoding='utf8') as output_json:
            json.dump(extracted_features, output_json)
json_folder = 'E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\\output_nonroumour.json'
output_file = 'E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\\dataset_nonroumour.json'

extract_features(json_folder, output_file)