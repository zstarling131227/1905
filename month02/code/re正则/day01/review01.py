import re

'''
############终端练习代码
s="2013年，参加湖南卫视《快乐男声》获年度总冠军出道 [1]  。2014年1月，首登央视春晚舞台。" \
  "同年4月，参加户外真人秀节目《花儿与少年》。9月6日-7日，在北京万事达中心连开两" \
  "场“火星”演唱会 [2]  ，随后首张个人专辑《卡西莫多的礼物》发行 [3]  ，" \
  "并凭此专辑获2015QQ音乐年度最佳内地男歌手及第十五届音乐风云榜年度最" \
  "受欢迎男歌手等奖项。2015年7月31日-8月2日，在上海大舞台连开三场个人演唱 [4]  。" \
  "12月，发行第二张专辑《异类》，获2016酷音乐亚洲盛典年度最佳专辑等奖项"
r1=re.findall(r"《\w+?》",s)
print(r1)
s="老祁： qtx@tedu.cn"
r2=re.findall('\w+@\w+\.cn',s)
print(r2)
r3=re.findall('a','abghfhsabbav')
print(r3)
r3=re.findall('ab','abghfhsabbav')
print(r3)
r3=re.findall('ba','abghfhsabbav')
print(r3)
r3=re.findall('王八蛋','abghf王八蛋hsabbav')
print(r3)
r3=re.findall('gh|ab','abghf王八蛋hsabbav')
print(r3)
r3=re.findall('王八蛋|ab','abghf王八蛋hsabbav')
print(r3)
r1=re.findall('张.丰','张三丰,张四丰,张五丰')
print(r1)
r1=re.findall('张..','张三丰,张四丰,张五丰')
print(r1)
r1=re.findall('张..','张\n丰,张四丰,张五丰')
print(r1)
r1=re.findall('[0-9]',"1989898")
print(r1)
r1=re.findall('[_#0-9a-z]',"potr#19")
print(r1)
r1=re.findall('[0-9a-z]',"potr#19")
print(r1)
r1=re.findall('[^0-9a-z]',"potr#19")
print(r1)
r1=re.findall('^0-9a-z',"potr#-+=19")
print(r1)
'''

'''
r1=re.findall('jame',"jame,hello")
print(r1)
r1=re.findall('^jame',"jame,hello")
print(r1)
r1=re.findall('^jame',"hello,jame")
print(r1)
r1=re.findall('zxl^jame',"jame,hello,zxl")
print(r1)
r1=re.findall('jame$',"jame,hello")
print(r1)
r1=re.findall('jame$',"hello,jame")
print(r1)
r1=re.findall('jame$zxl',"jame,hello,zxl")
print(r1)
'''

'''
r1=re.findall('wo*',"woooooooooooooooo~~w!")#######一个ｗ和0个或多个ｏ
print(r1)
r1=re.findall('w*',"wooooooo,woooooooo~~w!")#######findall的原理，会将*前未匹配的字符通过空字符表示
print(r1)
r1=re.findall('wo*|w*',"wooooooo,woooooooo~~w!")
print(r1)
r1=re.findall('',"how are you?")
print(r1)
r1=re.findall('[a-z][A-Z]*',"how are you?How Are You?")
print(r1)
r1=re.findall('[A-Z][a-z]*',"how are you?How Are You?")####*至少出现０次，单个字符可以查找
print(r1)
r1=re.findall('[A-Z][a-z]+',"how are you?How Are You?")
print(r1)
r1=re.findall('[A-Z][a-z]+',"I am GOOD, It is Yaoyue!")####＋至少出现１次，单个字符不可以查找
print(r1)
r1=re.findall('[A-Z][a-z]?',"I am GOOD, It is Yaoyue!")####？最多出现0次或１次
print(r1)
r1=re.findall('[A-Z][a-z][a-z]?',"I am GOOD, It is Yaoyue!")####？最多出现0次或１次
print(r1)
r1=re.findall('ab?',"ab mk am=a ababbbbba")
print(r1)
r1=re.findall('[0-9][0-9]?',"167 -28 -56 11 22 4")
print(r1)
r1=re.findall('-?[0-9]+',"167 -28 -56 11 22 4")
print(r1)
r1=re.findall('[0-9]+',"167 -28 -56 11 22 4")
print(r1)
r1=re.findall('[^ ]+',"Port-9 Error #404# %@STD")
print(r1)
'''

'''
r1=re.findall('ab{3}',"ab mk am=a ababbbbba")###指定匹配位数
print(r1)
r1=re.findall('[0-9]{11}',"yaoyue:12356554444")
print(r1)
r1=re.findall('1[0-9]{10}',"yaoyue:12356554444")
print(r1)
r1=re.findall('1[1-9]{1}[0-9]{9}',"yaoyue:12356554444")
print(r1)
r1=re.findall('张.{3}',"张程浩全")
print(r1)
r1=re.findall('14{2,4}',"yaoyue:1423144565514444")##包含２和４
print(r1)
r1=re.findall('[1-9][0-9]{5,10}',"yaoyue:14231445 06551　0444490 123456789008")##包含２和４
print(r1)
'''

'''
###\d相当于【０－９】
r1=re.findall('\d{1,5}',"Mysql: 3306, http:80 789008")
print(r1)
r1=re.findall('[0-9]{1,5}',"Mysql: 3306, http:80 789008")
print(r1)
r1=re.findall('\D',"Mysql: 3306, http:80  789008")
print(r1)
r1=re.findall('\D{1,5}',"Mysql: 3306, http:80 789008")
print(r1)
r1=re.findall('[^0-9]{1,5}',"Mysql: 3306, http:80 789008")
print(r1)
r1=re.findall('^[0-9]{1,5}',"Mysql: 3306, http:80 789008")
print(r1)
r1=re.findall('\W{1,5}',"Mysql: 3306, http:80 789008")
print(r1)
r1=re.findall('\w{1,5}',"Mysql: 3306, http:80 789008")
print(r1)
r1=re.findall('\s',"Mysql: 3306, http:80 789008")##空字符
print(r1)
r1=re.findall('\w+\s+\w+',"Mysql  hello")
print(r1)
r1=re.findall('\S+',"Mysql: 3306, http:80 789008")##非空字符
print(r1)
r1=re.findall('\Ahello',"Mysql  hello")
print(r1)
r1=re.findall('\AMysql',"Mysql  hello")
print(r1)
r1=re.findall('hello\Z',"Mysql  hello")
print(r1)
r1=re.findall('\S+',"Mysql  hello")
print(r1)
r1=re.findall('h\S',"Mysql  hello")
print(r1)
r1=re.findall('hello\Z',"Mysql  hello czx")
print(r1)
r1=re.findall('Mysql\Z',"Mysql  hello cxz")
print(r1)
r1=re.findall('\bis\b',"this a is http")
print(r1)
r1=re.findall(r'\bis\b',"this a is http")###r转换为原始字符串
print(r1)
r1=re.findall(r'is\b',"this a is http")
print(r1)
r1=re.findall(r'\bis',"this a is http")
print(r1)
r1=re.findall(r'\B_',"this a is http__")
print(r1)
r1=re.findall(r'\b_',"this a is http__")
print(r1)
r1=re.findall(r'\Bis\b',"this a is http")
print(r1)
'''

'''
r1=re.findall('-?\d+.?\d*',"12 -45 0.25 414.3 -8.9")
print(r1)
r1=re.findall('-?\d+\.?\d*',"12 -45 0.25 414.3 -8.9")
print(r1)
r1=re.findall('$\d+',"日新：$1000")
print(r1)
r1=re.findall('\$\d+',"日新：$1000")
print(r1)
r1=re.findall('\w\d+',"日新：$1000")
print(r1)
r1=re.findall('\\w \d+',"日新：$1000")
print(r1)
s="[花千骨],[陆贞传奇],[坏猪哥哥],[楚乔传]"
print(re.findall(r'\[\w+\]',s))
print(re.findall(r'\[.+\]',s))
print(re.findall(r'\[.+?\]',s))
r1=re.findall(r'\(.+\)',"(abcd)efgh(higk)")#贪婪
print(r1)
r1=re.findall(r'\(.+?\)',"(abcd)efgh(higk)")##非贪婪
print(r1)
'''

'''
#######练习
"""

"""
s="asdadasccvcvcxv＠tue.com"
r1=re.findall(r'\w+＠\.com',s)
print(r1)
s="asdadasccvcvcxv12133"
r1=re.findall(r'\w{8,12}',s)
print(r1)
s='12 -3 3.5 5.45 43% 1/3'
r1=re.findall(r'-?\d+\.?\d*%?',s)
print(r1)
s='12 -3 3.5 5.45 43% 1/3'
r1=re.findall(r'-?\d+/?\.?\d*%?',s)
print(r1)
s="asdada Sccvcv H-xv ASD iPYTon"
r1=re.findall(r'\w+',s)
print(r1)
r1=re.findall(r'[A-Z][-_a-zA-Z]*',s)
print(r1)
r1=re.findall(r'\b[A-Z][-_a-zA-Z]*',s)
print(r1)
'''

'''
r1=re.findall(r'ab+','abababababababab')
print(r1)
r1=re.search(r'(ab)+','ababababababab').group()
print(r1)
r1=re.search(r'王|张\w{1,3}','王八蛋').group()
print(r1)
r1=re.search(r'(王|张)\w{1,3}','王八蛋').group()
print(r1)
r1=re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(1)
print(r1)
r1=re.search(r'(?P<pig>ab)+',"ababababab").group('pig')
print(r1)
r1=re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(1)
print(r1)
'''

'''
######练习查身份证
r1=re.search(r'\d+',"622624199609042222").group()
print(r1)
r1=re.search(r'\d+',"622624199609042222 62262419960904222x").group()
print(r1)
r1=re.search(r'\d+',"62262419960904222x 622624199609042222").group()
print(r1)
r1=re.search(r'\d{18}',"622624199609042222 62262419960904222x").group()
print(r1)
r1=re.search(r'\d{18}',"62262419960904222x 622624199609042222").group()
print(r1)
r1=re.search(r'\d{17}(\d|x)',"62262419960904222x").group()
print(r1)
r1=re.search(r'\d{17}(\d|x)',"62262419960904222x 622624199609042222").group()
print(r1)
r1=re.search(r'\d{17}(\d|x)',"622624199609042222 62262419960904222x").group()
print(r1)
r1=re.search(r'\d.{16}(\d|x)',"622624199609042220 62262419960904222x 622624199609042220").group()
print(r1)
r1=re.search(r'\d.{16}(\d|x)',"62262419960904222x 622624199609042220 622624199609042220").group()
print(r1)
r1=re.search(r'\d.{17}(\d|x)',"622624199609042220 62262419960904222x 622624199609042220").group()
print(r1)###########注意{}和.{}的区别,此时的(\d|x)判断的是第１９位，因为１９位为空格，不匹配，故向后移动一位
r1=re.search(r'\d.{17}(\d|x)',"62262419960904222x 622624199609042220 622624199609042220").group()
print(r1)
r1=re.findall(r'\d.{17}x|\d.{17}',"62262419960904222x 622624199609042227")
print(r1)
r1=re.findall(r'\d.{17}|\d.{17}x',"62262419960904222x 622624199609042227")
print(r1)
'''

'''
#########regex.py
s="Wangbadan:1994,yaoyue:1996"
# pattern=r"\w+.\d+"
pattern=r"(\w+):(\d+)"
l=re.findall(pattern,s)
print(l)

regex=re.compile(pattern)
l=regex.findall(s)
print(l)
regex=re.compile(pattern)
# l=regex.findall(s,3,5)
l=regex.findall(s,0,14)
print(l)

l=re.split(r'[:,]',s)
print(l)

l=re.sub(r':','王八蛋',s)
print(l)
l=re.sub(r'w','王八蛋','wangbadan')
print(l)
l=re.subn(r':','王八蛋',s)
print(l)
l=re.subn(r'w','王八蛋','wangbadan')
print(l)
'''

'''
##############regex1.py
s="今年是2019年,建国70周年"
pattern=r"\d+"
it=re.finditer(pattern,s)
print(it)
for i in it:
  # print(i)
  print(i.group())
# m=re.fullmatch(r'\w+',s)#####未匹配到内容，返回值为Ｎｏｎｅ,即m的值为Ｎｏｎｅ，而ｎｏｎｅ没有ｇｒｏｕｐ属性，所以报错
# print(m.group())
m=re.fullmatch(r'[,\w]+',s)
print(m.group())
m=re.match(r'\w+',s)
print(m.group())
m=re.search(r'\d+',s)
print(m.group())
######属性
regex=re.compile(r'(ab)cd(?P<pig>ef)')
print(regex.flags)
print(regex.pattern)
print(regex.groupindex)
print(regex.groups)
'''

'''
#######regex2.py

pattren=r"(ab)cd(?P<pig>ef)"
regex=re.compile(pattren)
# obj=regex.search('abcdefghi')
obj=regex.search('abcdefghi',0,8)

print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)

print(obj.span())
print(obj.start())
print(obj.end())
print(obj.groupdict())
print(obj.groups())
print(obj.group())
print(obj.group('pig'))
'''

'''
#############flags.py
s="""Hello
北京
"""
# regex=re.compile(r'\w+')
#regex=re.compile(r'\w+',flags=re.A)
# regex=re.compile(r'[a-z]+',flags=re.I)
# regex=re.compile(r'.+',flags=re.S)
# regex=re.compile(r'^北京',flags=re.M)
# regex=re.compile(r'hello $',flags=re.M)
# regex=re.compile(r'\w+\s+\w+')
pattern="""\w+ #hello
\s+ # 匹配换行
\w+ # 北京
"""
# regex=re.compile(pattern,flags=re.X)
regex=re.compile(pattern,flags=re.X|re.I)
l=regex.findall(s)
print(l)
'''

'''
#################exc.py
"""
编写接口函数，从终端输入端口名称获取端口运行状态中的
地址值

思路分析：
1. 根据输入的端口名称找到对应的段落
2. 在该段落中匹配address
"""
def get_address(port):
    f = open("exc.txt")
    while True:
        data = ''
        for line in f:
            if line == "\n":
                # print("==============================")
                # print(line)
                break
            data += line
        if not data:
            break
        # print(data)
        obj = re.match(port, data)
        if obj:
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}\."
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
            obj = re.search(pattern, data)
            return obj.group()
    return "没有该端口"

# get_address()
if __name__ == '__main__':
    port=input("请输入端口：")
    print(get_address(port))
'''

'''
############老师讲
import re
def get_adderss(port):
    f = open('exc.txt')
    while True:
        # 获取一段内容
        data = ''
        for line in f:
            if line == '\n':
                break
            data += line

        # data为空说明到了文档结尾
        if not data:
            break

        obj = re.match(port,data) # 匹配开始位置
        # 如果obj不为None data就是目标段落
        if obj:
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
            obj = re.search(pattern,data)
            return obj.group()
    return "没有该端口"
    
if __name__ == '__main__':
    port = input("端口:")
    print(get_adderss(port))

'''