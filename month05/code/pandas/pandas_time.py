from datetime import datetime
import pandas as pd

date = datetime(2018, 9, 9, 23, 9, 43)
print(date, type(date))

# 时间点Timestamp
td1 = pd.Timestamp.now()  # 获取当前时间
print(td1, type(td1))
td = pd.Timestamp('2019-10-07 16:50:30')  # 创建任意时间点
td = td.tz_localize('Asia/Shanghai')  # 转换为指定时区的当前时间
print(td, type(td))
# 时间间隔Timestamp对象有属性[week, day, hour, minute, second, microsecond, nanosecond,……]
print(td.day)
print(td.microsecond)
print(td.microsecond)

print("-"*100)
# 时间段period
# print(pd.tseries.frequencies._period_code_map.keys())
# B D H T S L U N Q A W C ……
td = pd.Period.now(freq='B')
print(td, type(td))
print(td.start_time, type(td.start_time))
print(td.end_time)

print("-"*100)
# 时间间隔Timedelta allowed keywords are [weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds]
td = pd.Timedelta(weeks=4, days=4, seconds=90)
print(td, type(td))
# 时间间隔Timedelta 对象有属性days,seconds,microseconds,nanoseconds
print(td.days)
print(td.microseconds)
print(td.seconds)
print(td.nanoseconds)

print("-"*100)
# 三者的转换
# Timestamp-->Period   ：to_period
a = pd.Timestamp.now().to_period('H')
print(a, type(a))
# Timestamp-->Timedelta   ：+，-运算
a = pd.Timestamp.now() - pd.Timestamp('2019-10-7 17:13:00')
print(a, type(a))
# Timedelta+Timestamp-->Timestamp   ：+，-运算
a = pd.Timestamp('2018-10-1')
a = a + pd.Timedelta('3 days 00:01:30')
# a = pd.Timedelta('32 days 00:01:30') + pd.Timedelta('3 days 00:01:30')
print(a, type(a))

print("-"*100)
# strftime
import time

t = (2019, 10, 8, 18, 0, 28, 1, 48, 0)
t1 = time.mktime(t)  # mktime返回用秒数来表示时间的浮点数（参数为结构化的时间或者完整的9位元组元素）
print(t1)
print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(t1)))  # gmtime将一个时间戳转换为UTC时区（0时区）的struct_time，
print(time.strftime('%b %d %Y %H:%M:%S'))  # 返回以可读字符串表示的当地时间
print(time.strptime("30 Nov 00", "%d %b %y"))  # 根据指定的格式把一个时间字符串解析为时间元组
print(time.gmtime())
print(time.gmtime(t1))
