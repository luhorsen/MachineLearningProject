import json

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Normalizer

with open('E:\\rumordetection\RUMOUREVAL2019\dataset1.json', 'r') as file:
    data = json.load(file)

# 解析json数据并创建特征和标签列表
features = []
labels = []

for entry in data:
    feature = entry['feature']
    label = int(entry['label'])
    features.append(feature)
    labels.append(label)

# 创建数据集
dataset = pd.DataFrame(features)
dataset['label'] = labels
X = dataset.drop('label', axis=1)
y = dataset['label']
scaler = Normalizer()
X_scaled = scaler.fit_transform(X)
y= np.array(y)
# 准备数据集，假设您的特征数据保存在X变量中，目标变量保存在y变量中
X =X_scaled  # 特征数据
print(len(X))

# 定义一个列表，用于保存每次使用八个特征后的accuracy_scores评分
scores = []
print(X[0])
# 迭代验证特征
for i in range(len(X[0])):
    # 选择当前特征以及其之前个特征作为训练集特征
    selected_features = X[:, 0:i + 1]

    # 将特征数据划分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(selected_features, y, test_size=0.2, random_state=42)

    # 训练模型
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 预测测试集结果
    y_pred = model.predict(X_test)

    # 计算accuracy_scores评分并保存到列表中
    score = accuracy_score(y_test, y_pred)
    scores.append(score)

    print(f"特征 {i + 1}: accuracy_scores评分 = {score}")

