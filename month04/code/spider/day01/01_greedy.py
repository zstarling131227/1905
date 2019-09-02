import re

html='''
<html>
    <div><p>成也风云</p></div>
    <div><p>败也风云</p></div>
</html>
'''
#贪婪匹配（列表只有一个元素）(空格也属于任意字符）
pattern=re.compile('<div><p>.*</p></div>',re.S)
r_list=pattern.findall(html)
print(r_list)

#非贪婪匹配（列表有n个元素）
# pattern=re.compile('<div><p>.*?</p></div>',re.S)
##分组，只显示括号例的匹配内容
pattern=re.compile('<div><p>(.*?)</p></div>',re.S)
r_list=pattern.findall(html)
print(r_list)


import re

s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))
# 结果: ['A B','C D']


##先匹配整体，再看分组
p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
# 结果: ['A','C']

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))
# 第一步(整体正则匹配): ['A B','C D']
# 第二步(匹配分组)   : [('A','B'),('C','D')]