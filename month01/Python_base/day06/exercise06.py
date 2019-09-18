"""
day06 作业（有问题）
1. 三合一
2. 当天练习独立完成
6.阅读python入门到实践第６章
"""
"""
3. 将1970年到2050年中的闰年，存入列表．
"""
list01=[]
for i in range(1996,2019):
    if i%4==0 and i %100!=0 or i %400==0:
        # print("%d是闰年"%i)
        list01.append(i)
print(list01)
list01=[i for i in range(1970,2051) if i%4==0 and i %100!=0 or i %400==0]
print(list01)
"""
4. 存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
  　北京：
        景区：故宫,天安门,天坛.
        美食: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头.
"""
#
# dict01 = {
#     "北京":
#         {
#             "景区": ["故宫", "天安门", "天坛"],
#             "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]
#         },
#     "四川":
#         {
#             "景区": ["九寨沟", "峨眉山", "春熙路"],
#             "美食": ["火锅", "串串香", "兔头"]
#         }
# }
#
# # 需求:获取四川的所有美食
# print(dict01["四川"]["美食"])
# # 需求:获取所有城市
#
# for key in dict01:
#     print(key)
#
# # 需求：所有城市的景区
# # print(dict01["四川"]["景区"])
# # print(dict01["北京"]["景区"])
# # print(dict01["xxx"]["景区"])
#
# list02 = []
# # 遍历大字典，获取的是地区
# for key in dict01:
#     # 遍历景区列表
#     for item in dict01[key]["景区"]:
#         # 地区+景区
#         list02.append(key + ":" + item)
#
# print(list02)

######自己做
# dict_city={}
# while True:
#     city = input("请输入城市名称：")
#     if city =="":
#         break
#     view=input("请输入景区名称：")
#     food=input("请输入景区美食：")
#     dict_city[city]={"view":view,"food":food}
# print(dict_city)
# for key,value in dict_city.items():
#     print("%s的景区有%s；美食有%s。"%(key,value["view"],value["food"]))
"""

输出结果为
dict01={'北京': {'view': '故宫,天安门,天坛', 'food': '烤鸭,炸酱面,豆汁,卤煮'},
        '四川': {'view': '九寨沟,峨眉山,春熙路', 'food': '火锅,串串香,兔头'}}
"""
# dict_city={}
# while True:
#     city = input("请输入城市名称：")
#     if city =="":
#         break
#     dict_city[city] = {"view": [], "food":[]}
#     while 1:
#         view=input("请输入景区名称：")
#         if view  == "":
#             pass############返回到dict_city[city]["view"].append(view)语句仍然执行，也就是说空格会被添加到列表中。景区和美食的数量可以不同
#             # continue###########返回到view=input("请输入景区名称：")。
#             # break#######返回到city = input("请输入城市名称：")。景区和美食的数量相同
#         dict_city[city]["view"].append(view)
#         food=input("请输入景区美食：")
#         if food == "":
#             break
#         dict_city[city]["food"].append(food)
#         # print(dict_city)
# for key,value in dict_city.items():
#     print("%s的景区有%s；美食有%s。"%(key,value["view"],value["food"]))
"""

#输出结果为
dict01={'北京':
            {'view': ['故宫', '天安门', '天坛', '', ''],
             'food': ['烤鸭', '炸酱面', '豆汁', '卤煮']},
        '四川': {'view': ['九寨沟', '峨眉山', '春熙路'],
               'food': ['火锅', '串串香', '兔头']}}

"""

# ###需求:获取四川的所有美食
# print(dict01["北京"]["food"])
# # 需求:获取所有城市
# for key in dict01:
#     print(key)
# # 需求：所有城市的景区
# # print(dict01["四川"]["景区"])
# # print(dict01["北京"]["景区"])
# # print(dict01["xxx"]["景区"])
# list02 = []
# # 遍历大字典，获取的是地区
# for key in dict01:
#     # 遍历景区列表
#     for item in dict01[key]["view"]:
#         # 地区+景区
#         list02.append(key + ":" + item)
#
# print(list02)
"""
5.(扩展)计算一个字符串中的字符以及出现的次数.
# 思想：
# 逐一判断字符出现的次数.
# 如果统计过则增加１，如果没统计过则等于１.
abcdefce
a 1
b 1
c 2
d 1
e 2
f 1
"""

# dict_result = {}
# str_target = "abcdefce"
# for item in str_target:
#     if item not in dict_result:
#         dict_result[item] = 1
#     else:
#         dict_result[item] += 1
#
# print(dict_result)