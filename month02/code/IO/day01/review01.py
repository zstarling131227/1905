##########file_read.py
"""
file_read.py
文件读取演示
"""
# f=open("img.jpg","rb")

# f=open("test","r")
# data=f.read()
# print(data)

# while 1:
#     data=f.read(50)
#     if not data:
#         break
#     print(data)

# data=f.readline(10)
# print(data)

# data=f.readlines(66)
# print(data)

# for i in f:
#     print(i)

##########exec_1.py
# f=open("dict.txt","r")
# word="abandon"
# for i in f:
#     a = i.index(" ")
#     if word < i[:a]:
#         print("没有找到该单词")
#         break
#     if word==i[:a]:
#         print(i)####打印一行
#         print(i[a:].strip(" "))####只打印注释
#         break
# else:
#     raise ValueError("the word is not existing.")
# f.close()

##########file_open.py
"""
file_open.py
文件打开方式训练
"""
# f=open("test","w")##########清空再写入
# f=open("img.jpg","wb")##########二进制文件清空再写入
# f=open("test","a")##########不清空，在结尾处继续写入
# l=["wangbadan\n","yaoyue"]
# f.close()

##########file_write.py
"""
file_write.py
文件写操作演示
"""
# f.writelines(l)
# f.write("hello 死鬼\n".encode())
# f.write("王八蛋".encode())#################字符串没有ｅｎｃｏｄｅ功能
# s="王八蛋".encode()
# f.write(s.decode())
# f.close()
