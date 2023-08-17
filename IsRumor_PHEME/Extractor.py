import json
import re
import string
from datetime import datetime
from senticnet.senticnet import SenticNet
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class DataExtractor:
    File_Length=0
    def __init__(self, json_file_path):
        with open(json_file_path,encoding='utf8') as json_file:
            self.data = json.load(json_file)
            self.File_Length=len(self.data)


    def Get_Length_of_Characters(self,index):
        txt=self.data[index]['text']
        ##Filter out URLs
        cleaned_text = re.sub(r'http\S+', '', txt)
        # 去除文本中的非字母字符
        cleaned_text = re.sub(r'[^a-zA-Z]', '', cleaned_text)
        # 计算字母数量
        letter_count = len(cleaned_text)
        return letter_count
    def Get_Number_of_Words(self,index):
        txt = self.data[index]['text']
        ##Filter out URLs
        cleaned_text = re.sub(r'http\S+', '', txt)
        cleaned_text = re.sub(r'[^a-zA-Z ]', '', cleaned_text)
        # 切分文本为单词列表
        words = cleaned_text.split()
        # 计算单词数量
        word_count = len(words)
        return word_count
    def Ifcontains_QuMark(self,index):
        txt = self.data[index]['text']
        cleaned_text = re.sub(r'http\S+', '', txt)
        if '?' or '？' in cleaned_text:
            return 1
        else:
            return 0

    def Ifcontains_ExclamationMark(self,index):
        txt = self.data[index]['text']
        cleaned_text = re.sub(r'http\S+', '', txt)
        if '!' or '！' in cleaned_text:
            return 1
        else:
            return 0
    def Ifcontains_MultiMark(self,index):
        txt = self.data[index]['text']
        cleaned_text = re.sub(r'http\S+', '', txt)
        pattern = r"[?!]{2,}"
        matches = re.findall(pattern, cleaned_text)
        # 如果匹配到多个问号或感叹号，则返回True；否则返回False
        if matches:
            return 1
        else:
            return 0
    def Ifcontains_Smile(self,index):
        txt = self.data[index]['text']
        if ":-)" in txt or ";-)" in txt:
            return 1
        else:
            return 0

    def Ifcontains_Frowning(self, index):
        txt = self.data[index]['text']
        if ":-(" in txt or ";-(" in txt:
            return 1
        else:
            return 0

    def personal_pronoun_1st(self, index):
        txt = self.data[index]['text']
        first_person_pronouns = ["i", "me", "my", "we", "us", "our"]
        text = txt.lower()  # 将文本转换为小写，以匹配不区分大小写
        texts = text.split()
        for pronoun in first_person_pronouns:
            if pronoun in texts:
                return 1
        return 0

    def personal_pronoun_2st(self, index):
        txt = self.data[index]['text']
        second_person_pronouns = ["you", "your", "yours"]
        text = txt.lower()  # 将文本转换为小写，以匹配不区分大小写
        texts = text.split()
        for pronoun in second_person_pronouns:
            if pronoun in texts:
                return 1
        return 0

    def personal_pronoun_3st(self, index):
        txt = self.data[index]['text']
        third_person_pronouns = ["he", "she", "it", "him", "her", "his", "hers", "they", "them", "their", "theirs"]
        text = txt.lower()  # 将文本转换为小写，以匹配不区分大小写
        texts = text.split()
        for pronoun in third_person_pronouns:
            if pronoun in texts:
                print(text)
                print(pronoun)
                return 1

        return 0
    def Fraction_Of_Uppercase_Letters(self,index):
        txt = self.data[index]['text']
        total_chars = len(txt)
        uppercase_chars = sum(1 for char in txt if char.isupper())
        return uppercase_chars / total_chars if total_chars > 0 else 0

    def extract_url_count(self,index):
        tweet = self.data[index]['text']
        url_pattern = re.compile(r'(https?://\S+)')
        # Find URLs in Text
        matches = re.findall(url_pattern, str(tweet))
        # return the number of URLs
        return len(matches)
    def If_contains_User_Mention(self,index):
        txt = self.data[index]['text']
        if '@'in txt:
            return 1
        else:
            return 0
    def Has_Hashtag(self,index):
        txt = self.data[index]['text']
        if '#' in txt:
            tweet_words = txt.split()
            for word in tweet_words:
                if word.startswith('#'):
                    return 1
        return 0
    def Has_Stock_Symbol(self,index):
        txt = self.data[index]['text']
        if '$' in txt:
            tweet_words = txt.split()
            for word in tweet_words:
                if word.startswith('$'):
                    return 1
        return 0
    def Is_retweet(self,index):
        if self.data[index]['retweeted'] is False:
            return 0
        else:
            return 1
    def Extract_Day_Of_Week(self,index):
        created_at = self.data[index]['created_at']
        # 将日期字符串转换为datetime对象
        date_object = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
        # 提取星期几的数字（0表示星期一，6表示星期天）
        day_of_week = date_object.weekday()
        return day_of_week
    def Extract_PosWords(self,index):
        txt = self.data[index]['text']
        ##Filter out URLs
        cleaned_text = re.sub(r'http\S+', '', txt)
        cleaned_text = re.sub(r'[^a-zA-Z ]', '', cleaned_text)
        sn = SenticNet()
        tokens = word_tokenize(cleaned_text.lower())
        # 将文本转换为小写并分词
        stop_words = stopwords.words('english') + list(string.punctuation)
        filtered_tokens = [token for token in tokens if token not in stop_words]
        pos = []
        for token in filtered_tokens:
            try:
                polarity_value = sn.polarity_value(token)
            except KeyError:
                # 如果出现KeyError异常，将情感极性值设置为0
                polarity_value = 0
            # 如果情感极性值不为0，则认为这是一个情感词
            if type(polarity_value) is str and float(polarity_value) > 0:
                pos.append(token)
        positive_word_count = len(pos)
        return positive_word_count

    def Extract_NegWords(self,index):
        txt = self.data[index]['text']
        ##Filter out URLs
        cleaned_text = re.sub(r'http\S+', '', txt)
        cleaned_text = re.sub(r'[^a-zA-Z ]', '', cleaned_text)
        sn = SenticNet()
        tokens = word_tokenize(cleaned_text.lower())
        # 将文本转换为小写并分词
        stop_words = stopwords.words('english') + list(string.punctuation)
        filtered_tokens = [token for token in tokens if token not in stop_words]
        neg = []
        for token in filtered_tokens:
            try:
                polarity_value = sn.polarity_value(token)
            except KeyError:
                # 如果出现KeyError异常，将情感极性值设置为0
                polarity_value = 0
            # 如果情感极性值不为0，则认为这是一个情感词
            if type(polarity_value) is str and float(polarity_value) < 0:
                neg.append(token)
        negative_word_count = len(neg)
        return negative_word_count
    def Count_Sentiment_Score(self,index):
        txt = self.data[index]['text']
        ##Filter out URLs
        cleaned_text = re.sub(r'http\S+', '', txt)
        cleaned_text = re.sub(r'[^a-zA-Z ]', '', cleaned_text)
        sn = SenticNet()
        tokens = word_tokenize(cleaned_text.lower())
        # 将文本转换为小写并分词
        stop_words = stopwords.words('english') + list(string.punctuation)
        filtered_tokens = [token for token in tokens if token not in stop_words]
        words_score = []
        for token in filtered_tokens:
            try:
                polarity_value = sn.polarity_value(token)
            except KeyError:
                # 如果出现KeyError异常，将情感极性值设置为0
                polarity_value = 0
            # 如果情感极性值不为0，则认为这是一个情感词
            if type(polarity_value) is str and float(polarity_value) < -0.5:
                words_score.append(-1)
            elif type(polarity_value) is str and float(polarity_value) > 0.8:
                words_score.append(1)
            elif type(polarity_value) is str and float(polarity_value) > 0 and float(polarity_value) <= 0.8:
                words_score.append(0.5)
            elif type(polarity_value) is str and float(polarity_value) < 0 and float(polarity_value) >= -0.5:
                words_score.append(-0.5)
        score = sum(words_score)
        return score
    def Get_Registration_Age(self,index):
        created_at_user =self.data[index]['user']['created_at']
        created_at_post =self.data[index]['created_at']
        date_format="%a %b %d %H:%M:%S %z %Y"
        user_created_datetime = datetime.strptime(created_at_user, date_format)
        post_created_datetime = datetime.strptime(created_at_post, date_format)
        # 计算天数差
        days_difference = (post_created_datetime - user_created_datetime).days
        return days_difference
    def Get_Statuses_Count(self,index):
        return self.data[index]['user']['statuses_count']
    def Get_Number_Of_Followers(self,index):
        return self.data[index]['user']['followers_count']
    def Get_Number_Of_Friends(self,index):
        return self.data[index]['user']['friends_count']
    def Is_Verified(self,index):
        if self.data[index]['user']['verified'] is False:
            return 0
        elif self.data[index]['user']['verified'] is True:
            return 1
    def Has_Description(self,index):
        if self.data[index]['user']['description'] is not None or self.data[index]['user']['description']!='...':
            return 1
        else:
            return 0

