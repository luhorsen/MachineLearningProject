# Author: Hong Sheng Liu
# Date: 2023-05-28
# Version: 3.0
import pandas as pd
from snownlp import SnowNLP

# 读取Excel文件
df = pd.read_excel('D:\MachineLearning\IsRumor\output.xlsx')

# 获取文本列数据
text_list = df['文本'].tolist()
##改进方法，v2版本计算的情感词大大超出我的预期
def count_Sentiment_words(text):
    s = SnowNLP(text)
    pos, neg = 0, 0
   # for sentence in s.sentences:
    words=s.words
    for word in words:
        if SnowNLP(word).sentiments > 0.8:
            pos += 1
        elif SnowNLP(word).sentiments < 0.2:
            neg += 1
    return pos+neg


# 新建一个空的DataFrame用于保存情感词数量
result_df = pd.DataFrame()

# 循环遍历文本列表，计算每个文本的情感词数量
for text in text_list:
    # 使用count_emotion_words函数计算每个文本的情感值
    sen_words_num = count_Sentiment_words(text)
    # 将情感值添加到一个DataFrame中
    result_df = result_df._append({'情感词数量': sen_words_num}, ignore_index=True)

# 将结果保存到Excel文件中
df['情感词数量'] = result_df['情感词数量']
df.to_excel('D:\MachineLearning\IsRumor\output1.xlsx', index=False)