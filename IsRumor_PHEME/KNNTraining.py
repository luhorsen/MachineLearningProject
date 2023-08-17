# Author: Hong Sheng Liu
# Date: 2023-06-30
# Version: 1.0
import json

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, Normalizer

# 从JSON文件中读取数据
with open('E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\dataset.json', 'r') as file:
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
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 创建逻辑回归模型
model = KNeighborsClassifier(n_neighbors=2)
model.fit(X_train, y_train)
# 在测试集上进行预测
y_pred = model.predict(X_test)

print(y_test,y_pred)
# 计算评估指标
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# 打印评估指标
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:",f1)
