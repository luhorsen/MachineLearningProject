# Author: Hong Sheng Liu
# Date: 2023-05-28
# Version: 2.0
import pandas as pd
from snownlp import SnowNLP

# 读取Excel文件
df = pd.read_excel('D:\MachineLearning\IsRumor\output.xlsx')

# 获取文本列数据
text_list = df['文本'].tolist()
def count_Sentiment_words(text):
    # 使用SnowNLP的sentences方法将文本切分成多个句子
    sentences = SnowNLP(text).sentences
    # 计算每个句子的情感值，并将情感词相加得到总情感词数
    emotion_word_count = sum(len([w for w in SnowNLP(s).words if SnowNLP(w).sentiments]) for s in sentences)
    return emotion_word_count


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
df.to_excel('D:\MachineLearning\IsRumor\output.xlsx', index=False)