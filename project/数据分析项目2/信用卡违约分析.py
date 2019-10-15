import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings

from matplotlib.font_manager import FontProperties

font = FontProperties(fname="/usr/share/fonts/windows-fonts/songti/SIMSUN.TTC")

warnings.filterwarnings("ignore")
data = pd.read_csv('UCI_Credit_Card.txt', sep=",")
print(data.head(5))
print(data.tail(5))

"""
   ID  LIMIT_BAL  SEX  ...  PAY_AMT5  PAY_AMT6  default.payment.next.month
0   1    20000.0    2  ...       0.0       0.0                           1
1   2   120000.0    2  ...       0.0    2000.0                           1
2   3    90000.0    2  ...    1000.0    5000.0                           0
3   4    50000.0    2  ...    1069.0    1000.0                           0
4   5    50000.0    1  ...     689.0     679.0                           0

[5 rows x 25 columns]
          ID  LIMIT_BAL  SEX  ...  PAY_AMT5  PAY_AMT6  default.payment.next.month
29995  29996   220000.0    1  ...    5000.0    1000.0                           0
29996  29997   150000.0    1  ...       0.0       0.0                           0
29997  29998    30000.0    1  ...    2000.0    3100.0                           1
29998  29999    80000.0    1  ...   52964.0    1804.0                           1
29999  30000    50000.0    1  ...    1000.0    1000.0                           1

[5 rows x 25 columns]
"""

"""
数据集各变量定义

    ID:客户 ID
    LIMIT_BAL: 可透支金额
    SEX: 性别，男：1，女：2
    EDUCATION: 教育程度，研究生：1，本科：2，高中：3，其它：4
    MARRIAGE: 婚姻状况，已婚：1，单身：2，其它：3
    AGE: 年龄
    PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6: 2005年9月、8月、7月、6月、5月、4月客户还款情况
    BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6: 2005年9月、8月、7月、6月、5月、4月客户每月账单金额
    PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6:2005年9月、8月、7月、6月、5月、4月客户每月还款金额
    default.payment.next.month: 下月是否违约，违约：1，守约：0
"""

print(data.columns)

"""
Index(['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
       'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
       'default.payment.next.month'],
      dtype='object')
"""
# 数据集中无缺失数据
print(data.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30000 entries, 0 to 29999
Data columns (total 25 columns):
ID                            30000 non-null int64
LIMIT_BAL                     30000 non-null float64
SEX                           30000 non-null int64
EDUCATION                     30000 non-null int64
MARRIAGE                      30000 non-null int64
AGE                           30000 non-null int64
PAY_0                         30000 non-null int64
PAY_2                         30000 non-null int64
PAY_3                         30000 non-null int64
PAY_4                         30000 non-null int64
PAY_5                         30000 non-null int64
PAY_6                         30000 non-null int64
BILL_AMT1                     30000 non-null float64
BILL_AMT2                     30000 non-null float64
BILL_AMT3                     30000 non-null float64
BILL_AMT4                     30000 non-null float64
BILL_AMT5                     30000 non-null float64
BILL_AMT6                     30000 non-null float64
PAY_AMT1                      30000 non-null float64
PAY_AMT2                      30000 non-null float64
PAY_AMT3                      30000 non-null float64
PAY_AMT4                      30000 non-null float64
PAY_AMT5                      30000 non-null float64
PAY_AMT6                      30000 non-null float64
default.payment.next.month    30000 non-null int64
dtypes: float64(13), int64(12)
memory usage: 5.7 MB
"""

# 数据集中无重复数据
print(data.duplicated().sum())  # 0

# 将分类变量转换为 category
features = ['SEX', 'EDUCATION', 'MARRIAGE', 'default.payment.next.month', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5',
            'PAY_6']
for feature in features:
    data.loc[:, feature] = data[feature].astype("category")
print(data.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30000 entries, 0 to 29999
Data columns (total 25 columns):
ID                            30000 non-null int64
LIMIT_BAL                     30000 non-null float64
SEX                           30000 non-null category
EDUCATION                     30000 non-null category
MARRIAGE                      30000 non-null category
AGE                           30000 non-null int64
PAY_0                         30000 non-null category
PAY_2                         30000 non-null category
PAY_3                         30000 non-null category
PAY_4                         30000 non-null category
PAY_5                         30000 non-null category
PAY_6                         30000 non-null category
BILL_AMT1                     30000 non-null float64
BILL_AMT2                     30000 non-null float64
BILL_AMT3                     30000 non-null float64
BILL_AMT4                     30000 non-null float64
BILL_AMT5                     30000 non-null float64
BILL_AMT6                     30000 non-null float64
PAY_AMT1                      30000 non-null float64
PAY_AMT2                      30000 non-null float64
PAY_AMT3                      30000 non-null float64
PAY_AMT4                      30000 non-null float64
PAY_AMT5                      30000 non-null float64
PAY_AMT6                      30000 non-null float64
default.payment.next.month    30000 non-null category
dtypes: category(10), float64(13), int64(2)
memory usage: 3.7 MB
None
"""

print(data.describe(include="all"))

"""
                  ID       LIMIT_BAL  ...       PAY_AMT6  default.payment.next.month
count   30000.000000    30000.000000  ...   30000.000000                     30000.0
unique           NaN             NaN  ...            NaN                         2.0
top              NaN             NaN  ...            NaN                         0.0
freq             NaN             NaN  ...            NaN                     23364.0
mean    15000.500000   167484.322667  ...    5215.502567                         NaN
std      8660.398374   129747.661567  ...   17777.465775                         NaN
min         1.000000    10000.000000  ...       0.000000                         NaN
25%      7500.750000    50000.000000  ...     117.750000                         NaN
50%     15000.500000   140000.000000  ...    1500.000000                         NaN
75%     22500.250000   240000.000000  ...    4000.000000                         NaN
max     30000.000000  1000000.000000  ...  528666.000000                         NaN

[11 rows x 25 columns]

"""

# 数据可视化分析
"""
countplot 故名思意，是“计数图”的意思，可将它认为一种应用到分类变量的直方图，也可认为它是用以比较类别间计数差，调用 count 函数的 barplot；

countplot 参数和 barplot 基本差不多，可以对比着记忆，有一点不同的是 countplot 中不能同时输入 x 和 y ，且 countplot 没有误差棒。
"""
fig, ax = plt.subplots(figsize=(10, 5))
# plt.bar(x=[0,1],y="default.payment.next.month",height=100)
sns.countplot(x='default.payment.next.month', hue='SEX', data=data, ax=ax)
ax.set_xlabel("违约人数")
ax.set_xlabel('违约情况')
ax.set_ylabel('人数')
ax.set_title('按性别区分的违约情况')

fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(x='default.payment.next.month', hue='EDUCATION', data=data, ax=ax)
ax.set_xlabel('违约情况')
ax.set_ylabel('人数')
ax.set_title('按教育程度区分的违约情况')

fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(x='default.payment.next.month', hue='MARRIAGE', data=data, ax=ax)
ax.set_xlabel('违约情况')
ax.set_ylabel('人数')
ax.set_title('按教育程度区分的违约情况')
plt.show()

"""
distplot

displot()集合了matplotlib的hist()与核函数估计kdeplot的功能，增加了rugplot分布观测条显示与利用scipy库fit拟合参数分布的新颖用途。具体用法如下：
"""

fig, ax = plt.subplots(figsize=(10, 5))
sns.distplot(data.loc[data['default.payment.next.month'] == 0, 'LIMIT_BAL'], hist=False, color='r',
             kde_kws={"shade": True, "label": "守约"}, ax=ax)
sns.distplot(data.loc[data['default.payment.next.month'] == 1, 'LIMIT_BAL'], hist=False, color='b',
             kde_kws={"shade": True, "label": "违约"}, ax=ax)
ax.set_title('不同违约情况的可透支额度分布')
ax.set_xlabel('可透支额度')
ax.set_ylabel('频率')

fig, ax = plt.subplots(figsize=(10, 5))
sns.distplot(data.loc[data['default.payment.next.month'] == 0, 'AGE'], hist=False, color='r',
             kde_kws={"shade": True, "label": "守约"}, ax=ax)
sns.distplot(data.loc[data['default.payment.next.month'] == 1, 'AGE'], hist=False, color='b',
             kde_kws={"shade": True, "label": "违约"}, ax=ax)
ax.set_title('不同违约情况的年龄分布')
ax.set_xlabel('年龄')
ax.set_ylabel('频率')

fig, ax = plt.subplots(2, 3, figsize=(20, 10))
for i, pay in enumerate(['PAY_0', 'PAY_2', 'PAY_3']):
    sns.countplot(x='default.payment.next.month', hue=pay, data=data, ax=ax[0][i])
    ax[0][i].set_xlabel('违约情况')
    ax[0][i].set_ylabel('人数')
    ax[0][i].set_title('按9月还款情况区分的违约情况')
for i, pay in enumerate(['PAY_4', 'PAY_5', 'PAY_6']):
    sns.countplot(x='default.payment.next.month', hue=pay, data=data, ax=ax[1][i])
    ax[1][i].set_xlabel('违约情况')
    ax[1][i].set_ylabel('人数')
    ax[1][i].set_title('按月还款情况区分的违约情况')

fig, ax = plt.subplots(2, 3, figsize=(20, 10))
for i, BILL in enumerate(['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3']):
    sns.distplot(data.loc[data['default.payment.next.month'] == 0, BILL], hist=False, color='r',
                 kde_kws={"shade": True, "label": "守约"}, ax=ax[0][i])
    sns.distplot(data.loc[data['default.payment.next.month'] == 1, BILL], hist=False, color='b',
                 kde_kws={"shade": True, "label": "违约"}, ax=ax[0][i])
    ax[0][i].set_title('不同违约情况的账单金额分布')
    ax[0][i].set_xlabel('账单金额')
    ax[0][i].set_ylabel('频率')
for i, BILL in enumerate(['BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']):
    sns.distplot(data.loc[data['default.payment.next.month'] == 0, BILL], hist=False, color='r',
                 kde_kws={'shade': True, "label": "守约"}, ax=ax[1][i])
    sns.distplot(data.loc[data['default.payment.next.month'] == 1, BILL], hist=False, color='b',
                 kde_kws={"shade": True, "label": "违约"}, ax=ax[1][i])
    ax[1][i].set_title('不同违约情况的账单金额分布')
    ax[1][i].set_xlabel('账单金额')
    ax[1][i].set_ylabel('频率')

fig, ax = plt.subplots(2, 3, figsize=(20, 10))
for i, PAY in enumerate(['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3']):
    sns.distplot(data.loc[data['default.payment.next.month'] == 0, PAY], hist=False, color='r',
                 kde_kws={"shade": True, "label": "守约"}, ax=ax[0][i])
    sns.distplot(data.loc[data['default.payment.next.month'] == 1, PAY], hist=False, color='b',
                 kde_kws={"shade": True, "label": "违约"}, ax=ax[0][i])
    ax[0][i].set_title('不同违约情况的还款金额分布')
    ax[0][i].set_xlabel('账单金额')
    ax[0][i].set_ylabel('频率')
for i, PAY in enumerate(['PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']):
    sns.distplot(data.loc[data['default.payment.next.month'] == 0, PAY], hist=False, color='r',
                 kde_kws={'shade': True, "label": "守约"}, ax=ax[1][i])
    sns.distplot(data.loc[data['default.payment.next.month'] == 1, PAY], hist=False, color='b',
                 kde_kws={"shade": True, "label": "违约"}, ax=ax[1][i])
    ax[1][i].set_title('不同违约情况的还款金额分布')
    ax[1][i].set_xlabel('账单金额')
    ax[1][i].set_ylabel('频率')

index = np.random.randint(0, 30000, 100)
sample_data = data.loc[
    index, ['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6', 'default.payment.next.month']]
print(sample_data.head())

"""
  PAY_AMT1  PAY_AMT2  ...  PAY_AMT6  default.payment.next.month
16157    2000.0       4.0  ...       0.0                           1
8058     2782.0    2761.0  ...    2568.0                           0
3387     1188.0       0.0  ...       0.0                           0
9307     1500.0    1500.0  ...     900.0                           1
16141       0.0    3400.0  ...    3100.0                           0

[5 rows x 7 columns]
"""

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
for i in sample_data.iterrows():
    dd = pd.DataFrame(i[1])
    if dd.loc['default.payment.next.month', :].values == 1:
        dd.drop('default.payment.next.month', axis=0, inplace=True)
        ax1.plot(dd.index, dd.values)
    else:
        dd.drop('default.payment.next.month', axis=0, inplace=True)
        ax2.plot(dd.index, dd.values)
ax1.set_title('违约用户还款金额变动')
ax2.set_title('守约用户还款金额变动')
plt.ylim(0, 20000)

# 不同的受教育程度、性别、婚姻状况、账单金额在是否守约方面未见明显区分，不同年龄、还款金额以及每月还款金额变动在是否守约方面区分明显。

data['default.payment.next.month'] = data.loc[:, 'default.payment.next.month'].astype('int')

data[['default.payment.next.month', 'SEX']].groupby(['SEX'], as_index=False).mean()
# 女性用户违约率比男性用户低约16%,差异显著。

data[['default.payment.next.month', 'MARRIAGE']].groupby(['MARRIAGE'], as_index=False).mean()
# MARRIAGE 字段为 0 无对应释义，需删除。单身用户的违约率比已婚和其它用户低约10%～20%。差异显著。

data[['default.payment.next.month', 'EDUCATION']].groupby(['EDUCATION'], as_index=False).mean()
# EDUCATION 字段 0，5，6 无对应释义。可能需要删除。其它学历的用户违约率低，研究生 - 本科生 - 高中生 违约率随着学历的降低而升高。

data[(data['EDUCATION'] == 0) | (data['EDUCATION'] == 5) | (data['EDUCATION'] == 6)]['ID'].count()
# EDUCATION 字段无对应释义样本数为345，占总样本比率约1%。删除。

data.drop(data[(data['EDUCATION'] == 0) | (data['EDUCATION'] == 5) | (data['EDUCATION'] == 6)].index, axis=0,
          inplace=True)
data[(data['EDUCATION'] == 0) | (data['EDUCATION'] == 5) | (data['EDUCATION'] == 6)]['ID'].count()  # 0

data.drop(data[data['MARRIAGE'] == 0].index, axis=0, inplace=True)

# 选择 LIMIT_BAL,EDUCTAION,MARRIAGE,SEX,AGE,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6 进行数据建模

model_data = data.drop(columns=['ID', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'])
print(model_data.head(3))

columns = model_data.columns.tolist()
columns.remove('default.payment.next.month')
results_var = 'default.payment.next.month'
x = model_data[columns].values
y = model_data[results_var].values

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

"""
1.Pipeline中的steps

　　Pipeline的最后一步是一个“estimator”（sklearn中实现的各种机器学习算法实例，或者实现了estimator必须包含的方法的自定义类实例），之前的每一步都是“transformer”（必须实现fit和transform方法，比如MinMaxScaler、PCA、one-hot）。在Pipeline调用fit方法时，Pipeline中的每一步依次进行fit操作。

"""
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

"""
GridSearchCV
class sklearn.model_selection.GridSearchCV(
	estimator, param_grid, scoring=None, 
	fit_params=None, n_jobs=1, iid=True,
 	refit=True, cv=None, verbose=0,
 	pre_dispatch='2*n_jobs', error_score='raise', return_train_score=True)
————————————————
版权声明：本文为CSDN博主「Kyrie_Irving」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Kyrie_Irving/article/details/90023615
其中cv可以是整数或者交叉验证生成器或一个可迭代器，cv参数对应的输入列举如下：
None：默认参数，函数会使用默认的3折交叉验证
整数k：k折交叉验证。对于分类任务，使用StratifiedKFold（类别平衡，每类的训练集占比一样多，具体可以查看官方文档）。对于其他任务，使用KFold
estimator：所使用的分类器，或者pipeline
param_grid：值为字典或者列表，即需要最优化的参数的取值
scoring：准确度评价标准，默认None,这时需要使用score函数；或者如 scoring=‘roc_auc’，根据所选模型不同，评价准则不同。字符串（函数名），或是可调用对象，需要其函数签名形如：scorer(estimator, X, y)；如果是None，则使用estimator的误差估计函数。

n_jobs：并行数，int：个数,-1：跟CPU核数一致, 1:默认值。
pre_dispatch：指定总共分发的并行任务数。当n_jobs大于1时，数据将在每个运行点进行复制，这可能导致OOM，而设置pre_dispatch参数，则可以预先划分总共的job数量，使数据最多被复制pre_dispatch次
iid：默认True,为True时，默认为各个样本fold概率分布一致，误差估计为所有样本之和，而非各个fold的平均。
refit：默认为True,程序将会以交叉验证训练集得到的最佳参数，重新对所有可用的训练集与开发集进行，作为最终用于性能评估的最佳模型参数。即在搜索参数结束后，用最佳参数结果再次fit一遍全部数据集。
verbose：日志冗长度，int：冗长度，0：不输出训练过程，1：偶尔输出，>1：对每个子模型都输出。

4.属性
best_estimator_：效果最好的分类器

best_score_：成员提供优化过程期间观察到的最好的评分

best_params_：描述了已取得最佳结果的参数的组合

best_index_：对应于最佳候选参数设置的索引(cv_results_数组的索引)。
"""

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=1)

classifiers = [
    SVC(random_state=1, kernel='rbf'),
    DecisionTreeClassifier(random_state=1, criterion='gini'),
    RandomForestClassifier(random_state=1, criterion='gini'),
    KNeighborsClassifier(metric='minkowski')
]

classifier_names = [
    'svc',
    'decisiontreeclassifier',
    'randomforestclassifier',
    'kneighborsclassifier',
]

classifier_param_grid = [
    {'svc__C': [1], 'svc__gamma': [0.01]},
    {'decisiontreeclassifier__max_depth': [6, 9, 11]},
    {'randomforestclassifier__n_estimators': [3, 5, 6]},
    {'kneighborsclassifier__n_neighbors': [4, 6, 8]},
]


def GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, param_grid, score='accuracy'):
    response = {}
    gridsearch = GridSearchCV(estimator=pipeline, param_grid=param_grid, scoring=score)
    # 寻找最优的参数 和最优的准确率分数
    # 训练
    search = gridsearch.fit(train_x, train_y)
    # best_params_：描述了已取得最佳结果的参数的组合
    print("GridSearch最优参数：", search.best_params_)
    # best_score_：成员提供优化过程期间观察到的最好的评分
    print("GridSearch最优分数： %0.4lf" % search.best_score_)
    # 用找到的最佳参数调用预估器。(直接预测每个样本属于哪一个类别)
    # predict_log_proda(X): 用找到的最佳参数调用预估器。（得到每个测试集样本在每一个类别的得分取log情况）
    #
    # predict_proba(X): 用找到的最佳参数调用预估器。（得到每个测试集样本在每一个类别的得分情况）
    predict_y = gridsearch.predict(test_x)

    print("准确率 %0.4lf" % accuracy_score(test_y, predict_y))
    response['predict_y'] = predict_y
    response['accuracy_score'] = accuracy_score(test_y, predict_y)
    return response


for model, model_name, model_param_grid in zip(classifiers, classifier_names, classifier_param_grid):
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        (model_name, model)
    ])
    result = GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, model_param_grid, score='accuracy')

"""
GridSearch最优参数： {'svc__C': 1, 'svc__gamma': 0.01}
GridSearch最优分数： 0.8102
准确率 0.8160
GridSearch最优参数： {'decisiontreeclassifier__max_depth': 6}
GridSearch最优分数： 0.8112
准确率 0.8227
GridSearch最优参数： {'randomforestclassifier__n_estimators': 6}
GridSearch最优分数： 0.7951
准确率 0.8018
GridSearch最优参数： {'kneighborsclassifier__n_neighbors': 8}
GridSearch最优分数： 0.8029
准确率 0.8089
"""
