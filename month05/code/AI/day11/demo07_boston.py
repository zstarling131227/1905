"""
demo07_boston.py 预测波士顿房屋价格
"""
import sklearn.metrics as sm  # sklearn.metrics提供了计算模型误差的几个常用算法
import sklearn.tree as st
import sklearn.datasets as sd
import sklearn.utils as su

# 加载波士顿地区房价数据集（字典类型）
boston = sd.load_boston()
# print(boston,sep="")
for i in boston:
    print(i)
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)
# |CRIM|ZN|INDUS|CHAS|NOX|RM|AGE|DIS|RAD|TAX|PTRATIO|B|LSTAT|
# 犯罪率|住宅用地比例|商业用地比例|是否靠河|空气质量|房间数|年限|距中心区距离|路网密度|房产税|师生比|黑人比例|低地位人口比例|

# 打乱原始数据集的输入和输出   random_state：随机种子，随机种子相同时，shuffle随机打乱的结果也相同
x, y = su.shuffle(boston.data, boston.target, random_state=7)
# print(x, y)
# 划分训练集和测试集 8:2
train_size = int(len(x) * 0.8)
train_x, text_x, train_y, text_y = x[:train_size], x[:train_size], y[:train_size], y[:train_size]

# 构建决策树模型 使用训练集训练
modle = st.DecisionTreeRegressor(max_depth=4)
# 使用测试集测试。输出r2_score
modle.fit(train_x, train_y)
pred_y = modle.predict(text_x)
re = sm.r2_score(text_y, pred_y)
print(re)
