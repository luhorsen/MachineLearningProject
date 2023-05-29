import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# 从Excel文件中读取数据
data = pd.read_excel('D:\MachineLearning\IsRumor\output1.xlsx')
X = data[['粉丝数', 'URL 数量', '情感词数量']]
y = data['label']

# 数据归一化
scaler = StandardScaler()
X_norm = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2, random_state=42)

# 训练SVM模型
clf = SVC()
clf.fit(X_train, y_train)

# 评估模型分数
score = clf.score(X_test, y_test)
print("模型评分：", score)