import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# 读取JSON文件
with open('E:\\rumordetection\PHEME\PHEME_veracity.tar\PHEME_veracity\\all-rnr-annotated-threads\charliehebdo-all-rnr-threads\dataset.json') as f:
    data = json.load(f)

# 提取特征和标签列表
features_list = []
labels = []
for item in data:
    features_list.append(item['feature'])
    labels.append(item['label'])

# 转换为DataFrame
df = pd.DataFrame(features_list)

# 转换标签为数值
df['label'] = pd.to_numeric(labels)

# 计算特征与标签的相关系数
correlation_matrix = df.corr()['label']

# 创建带有关联度的DataFrame
correlation_df = pd.DataFrame({'Feature-Label Correlation': correlation_matrix})
print(correlation_df)
# 可视化相关系数
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_df, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Feature-Label Correlation')
plt.show()