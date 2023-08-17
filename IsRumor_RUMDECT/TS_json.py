from sklearn.datasets import load_iris

# 加载莺尾花数据集
iris = load_iris()

# 获取特征矩阵
X = iris.data

# 获取标签矩阵
y = iris.target

print(X)
print(y[:9])