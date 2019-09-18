'''
# def mysort(s):
#     l=len(s)
#     i=0
#     for m in range(l):
#         if s[i]=="-":
#             s[i],s[l-1]=s[l-1],s[i]
#             l-=1
#         else:
#             i+=1
#
# # a=["+","-","+","-","+"]
# a=["+","-","-","+","-","-","+"]
# mysort(a)
# print(a)
'''

'''
#############三人年龄算法
"""
s=[[1, 1, 36], [1, 2, 18], [1, 3, 12], [1, 4, 9], [1, 6, 6], [2, 2, 9], [2, 3, 6], [3, 3, 4]]

def combine(mutiply):
    list01=[]
    for i in range(1,mutiply+1):
        for j in range(1,mutiply+1):
            for g in range(1,mutiply+1):
                if i*j*g==mutiply:
                    combine_sort=sorted((i,j,g))
                    if combine_sort not in list01:
                        list01.append(combine_sort)
    for i in range(len(list01)):
        for j in range(i+1,len(list01)):
            if sum(list01[i])==sum(list01[j]) :
                if list01[i].count(max(list01[i]))==1:
                    return list01[i]
                if list01[j].count(max(list01[j]))==1:
                    return list01[j]
print(combine(36))

def combine1(mutiply):
    list01=[]
    for i in range(1,mutiply+1):
        for j in range(1,mutiply+1):
            for g in range(1,mutiply+1):
                if i*j*g==mutiply:
                    combine_sort=sorted((i,j,g))
                    if combine_sort not in list01:
                        list01.append(combine_sort)
    # print(list01)
    list02=[sum(i) for i in list01]
    for a in list02:
        if list02.count(a)>1:
            list01.remove(list01[list02.index(a)])
            for item in list01:
                if sum(item)==a:
                    if item.count(max(item))==1:
                        return item
print(combine1(36))
'''

