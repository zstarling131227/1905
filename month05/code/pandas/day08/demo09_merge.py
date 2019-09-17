"""
demo09_merge.py 合并
"""

import pandas as pd

left = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'class_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]})
right = pd.DataFrame(
    {'class_id': [1, 2, 3, 5],
     'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
print("=================左表=======================")
print(left)
print("=================右表=======================")
print(right)
print("================内连接======================")
# 只保留左表和右表都存在的元素
# 合并两个DataFrame
# rs = pd.merge(left, right) # 默认为内连接
rs = pd.merge(left, right, how='inner')
print(rs)
print("================右连接======================")
# 只保留右表都存在的元素
# 合并两个DataFrame
rs = pd.merge(left, right, how='right')
print(rs)
print("================左连接======================")
# 只保留左表都存在的元素
# 合并两个DataFrame
rs = pd.merge(left, right, how='left')
print(rs)
