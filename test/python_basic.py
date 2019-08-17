'''

a=1
b=2
# a = a+b
# b = a-b
# a = a-b
# print(a,b)
# a = a^b
# b = b^a
# a = a^b
# print(a,b)
a,b=b,a
print(a,b)
'''

'''
class Parent(object):
	x = 1
class Child1(Parent):
	pass
class Child2(Parent):
	pass
print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)


l = []
for i in range(10):
	l.append({'num':i})
print(l)


l = []
a = {'num':0}
for i in range(10):
	a['num'] = i
	l.append(a)
print(l)

from multiprocessing import process
def get_line():
	l = []
	with open('file.txt','rb') as f:
		for eachline in f:
			l.append(eachline)
	return l

def get_lines():
	l = []
	with open('file.txt', 'rb') as f:
		data = f.readlines(60000)
	l.append(data)
	yield l

if __name__ == '__main__':
	for e in get_lines():
		process(e) #处理每一行数据
'''

# import os
# for sChild in os.listdir(sPath):
#     sChildPath = os.path.join(sPath, sChild)
#     if os.path.isdir(sChildPath):
#         print_directory_contents(sChildPath)
#     else:
#         print(sChildPath)



