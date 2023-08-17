# Author: Hong Sheng Liu
# Date: 2023-05-28
# Version: 1.0
import pandas as pd
from nltk.tokenize import word_tokenize
from senticnet.senticnet import SenticNet

# 读取Excel文件
df = pd.read_excel('D:\MachineLearning\IsRumor\output.xlsx')

# 获取文本列数据
text_list = df['文本'].tolist()

def get_emotion_word_count(text):
    # 使用nltk的word_tokenize函数将文本分词
    words = word_tokenize(text)
    # 使用SenticNet计算单词的情感值
    sn = SenticNet()
    emotion_word_count = 0
    for word in words:
        try:
            polarity_value = sn.polarity_value(word)
        except KeyError:
            # 如果出现KeyError异常，将情感极性值设置为0
            polarity_value = 0
        # 如果情感极性值不为0，则认为这是一个情感词
        if polarity_value != 0:
            emotion_word_count += 1
    return emotion_word_count
# 新建一个空的DataFrame用于保存情感词数量
result_df = pd.DataFrame()

# 循环遍历文本列表，计算每个文本的情感词数量
for text in text_list:
    emotion_word_count = get_emotion_word_count(text)
    # 将情感词数量添加到一个DataFrame中
    result_df = result_df._append({'情感词数量': emotion_word_count}, ignore_index=True)

# 将结果保存到Excel文件中
df['情感词数量'] = result_df['情感词数量']
df.to_excel('D:\MachineLearning\IsRumor\output.xlsx', index=False)
