############exec_2.py
"""
逆波兰表达式练习
"""
from review02 import *

st=SStack()
while 1:
    exp=input("字符串：")
    tmp=exp.split(' ')
    print(tmp)
    for i in tmp:
        if i not in ["-","+","*","/","p"]:
            st.push(float(i))
        elif i=="-":
            y=st.pop()
            x=st.pop()
            st.push(x-y)
        elif i=="+":
            y=st.pop()
            x=st.pop()
            st.push(x+y)
        elif i=="*":
            y=st.pop()
            x=st.pop()
            st.push(x*y)
        elif i=="/":
            y=st.pop()
            x=st.pop()
            st.push(x/y)
        elif i == 'p':
            print(st.top()) # 查看栈顶


    """
逆波兰表达式练习


st = SStack()

while True:
    exp = input("字符串：")
    tmp = exp.split(' ') # 按空格切割
    print(tmp)
    for i in tmp:
        if i not in ['+','-','*','/','p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x+y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x-y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x*y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x/y)
        elif i == 'p':
            print(st.top()) # 查看栈顶

"""
