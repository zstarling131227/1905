print('hello world!')

# n = int(input("请输入一个数"))
# i = 1
# while i <= n:
#     if i % 3 == 0:
#         i = i + 1
#         continue
#     print(i)
#     i = i + 1

str='hello world'
for i in str:
    print(i)

# n=int(input('输入整数：'))
# a=0
# for i in range(1,n+1):
#     a+=i
# print(a)

# 用while循环实现随机生成n位密码
# /验证码(数字、字母、下划线)
#方法1 while
# import random
# str = "abcdefghijklmn\
# opqrstuvwxyz_0123456789"
# i = 1
# n = int(input("请输入密码位数"))
# pwd = ""
# while i <= n:
#     char = random.choice(str)
#     pwd = pwd + char
#     i = i + 1
# print(pwd)
#方法2 for
# import random
# str='0123456789_abcdefghijklmnopqrstuvwxyz'
# a=int(input('请输入密码位数：'))
# pwd=''
# for i in range(a):
#     char = random.choice(str)
#     pwd +=char
# print(pwd)

# # 方法1 for
# nam='ren'
# mim='123'
# for i in range(1,4):
#     name = input('请输入登录名：')
#     mima = input('请输入密码：')
#     if name==nam and mima==mim:
#         print('登录成功')
#         break
#     else:
#         print('输入错误')
#     print('一共三次机会，您还剩',3-i,'次')
# else:
#     print('登录失败')
#方法2 while
# nam='ren'
# mim='123'
# i=1
# while i<=3:
#     name = input('请输入登录名：')
#     mima = input('请输入密码：')
#     if name == nam and mima == mim:
#         print('登录成功')
#         break
#     else:
#         print('输入错误')
#     print('您还剩%d次机会'% (3-i))
#     i+=1
# else:
#     print('登录失败')

# for a in range(1,10):
#     for b in range(1,a+1):
#         print('%d*%d=%2d' % (a,b,a*b),end=' ')
#     print()

# for a in range(9,0,-1):
#     for b in range(a,0,-1):
#         print('%d*%d=%2d' % (a, b, a * b), end=' ')
#     print()

# b=0
# str=input('输入字符串：')
# for a in str:
#     if a==' ':
#         b+=1
# print(b)


# str='hello world'
# for i in str:
#     if i=='w':
#         break
#     print(i)


# h=int(input('请输入高度：'))
# h1=h
# for i in range(2):
#     h=h/2
#     h1 += h * 2
# print(h/2)
# print(h1)



