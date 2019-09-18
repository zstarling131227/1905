"""
作业 ： 1. 熟悉markdown标签规则，会编写基本的markdown文档
        
	　　2. 熟练重点代码

		3. 编程作业

    编写一个接口程序，获取一段文字，判定文字中括号是否匹配正确，
    如果正确则打印正确，不正确则支出出错的地方

    "Thanks to {the} flexibility of Python and the
    [powerful] ecosystem of pac(kages, {the Azure
    (CLI)} supports features such as autoc]ompletion
    (in shells that support it), persistent credentials,
     JMESPath result parsing, lazy initialization,
      network-less unit tests, and more."
"""
#######3. 编程作业
# (看day03/day03.zip/exec_1.py)
###字典，生成器，鏈式栈，
from review02 import *
str01="Thanks to {the} flexibility of Python and the\
    [powerful] ecosystem of pac(kages, {the Azure\
    (CLI)} supports features such as autoc]ompletion\
    (in shells that support it), persistent credentials,\
     JMESPath result parsing, lazy initialization,\
      network-less unit tests, and more. "
dict01= {"]": "[", ")": "(", "}": "{"}
ls=LStack

####生成器(目的：获取字符串中的括号和其位置)
def double(str_target):
    i, str_target_len = 0, len(str_target)
    while 1:
        while i <str_target_len and str_target[i] not in str_target:
            if i >=str_target_len:
                return
            else:
                yield str_target[i],i
                i+=1
for k,v in double(str01):
    print(k,v)


"""
一段文字中有()[]{},编写一个接口程序去判断括号是否匹配正确
"""

text = "The core (of) extensible programming [is] defining functions. Python allows {mandatory [and]} optional (arguments, {keyword} arguments), and even arbitrary argument lists."

#　将验证条件提前定义好
parens = "()[]{}"  #　特殊处理的字符集
left_parens = "([{"  #　入栈字符集
#　验证匹配关系　
opposite = {'}':'{',']':'[',')':'('}

ls = LStack()  #　存储括号的栈

# 编写生成器，用来遍历字符串，不断的提供括号及其位置
def parent(text):
    #　i 遍历字符串的索引位置
    i,text_len = 0,len(text)

    #　开始遍历字符串
    while True:
        while i < text_len and text[i] not in parens:
            i += 1

        #　到字符串结尾了
        if i >= text_len:
            return
        else:
            yield text[i],i
            i += 1

#　功能函数判断提供的括号是否匹配
def ver():
    for pr,i in parent(text):
        if pr in left_parens:
            ls.push((pr,i)) #　左括号入栈
        elif ls.is_empty() or ls.pop()[0] != opposite[pr]:
            print("Unmatching is found at %d for %s"%(i,pr))
            break
    else:
        if ls.is_empty():
            print("All parentheses are matched")
        else:
            #　左括号多了
            d = ls.pop()
            print("Unmatching is found at %d for %s" %(d[1],d[0]))

#　逻辑验证
ver()










