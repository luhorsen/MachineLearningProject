import json
import re
from snownlp import SnowNLP

class DataExtractor:
    def __init__(self, json_file_path):
        with open(json_file_path,encoding='utf8') as json_file:
            self.data = json.load(json_file)

    def extract_Number_of_Senwords(self):
        text = self.data[0]['text']
        s = SnowNLP(text)
        pos, neg = 0, 0
        words = s.words
        for word in words:
            if SnowNLP(word).sentiments > 0.8:
                pos += 1
            elif SnowNLP(word).sentiments < 0.2:
                neg += 1
        return pos + neg

    def extract_Number_of_URL(self):
        text = self.data[0]['text']
        url_pattern = re.compile(r'(https?://\S+)')
        # Find URLs in Text Columns
        matches = re.findall(url_pattern, str(text))
        # return the number of URLs
        return len(matches)
    def extract_Number_of_Comment(self):
        return self.data[0]['comments_count']
    def extract_User_Type(self):
        if self.data[0]['verified_type']!=-1:
            return 1
        else:
            return 0
    def extract_RegisAge(self):
        now_timestamp=self.data[0]['t']
        created_at_timestamp=self.data[0]['user_created_at']
        days_since_created = int((now_timestamp - created_at_timestamp) / 86400)  # 计算相差的天数
        return days_since_created
    def extract_Number_of_Followers(self):
        return self.data[0]['followers_count']
    def extract_Number_of_posts(self):
        return self.data[0]['statuses_count']
    def extract_Number_of_reposts(self):
        return self.data[0]['reposts_count']
    def extract_Number_of_Followees(self):
        return self.data[0]['friends_count']
    '''def extract_Isreposted(self):
        if self[0]['parent'] is not None:
            return 1
        else:
            return 0'''

    def extract_Has_Picture(self):
        value = self.data[0].get('picture', None)
        if value is not None:
            return 1
        else:
            return 0

    def extract_Userhas_Description(self):
        value = self.data[0].get('user_description', None)
        if value is not None:
            return 1
        else:
            return 0
    def extract_Gender(self):
        if self.data[0]['gender']=='m':
            return 1
        else:
            return 0

    def extract_RegisTime(self):
        return  self.data[0]['user_created_at']


    def extract_Number_of_posts(self):
        return self.data[0]['statuses_count']
    def read_label(self):


