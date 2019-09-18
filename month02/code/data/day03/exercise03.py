###插入排序
def bubble1(list_):
    for i in range(1, len(list_)):
        j = i - 1
        temp = list_[i]
        list_[i] = list_[j]
        while j >= 0 and list_[j] > temp:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = temp
    #############
    # for i in range(1,len(list_)):
    #     j=i-1
    #     if list_[j] > list_[i]:
    #         temp=list_[i]
    #         list_[i]= list_[j]
    #         j-=1
    #         while j>=0 and list_[j]>temp:
    #             list_[j+1]=list_[j]
    #             j-=1
    #         list_[j+1]=temp
    ##################
    for i in range(1, len(list_)):
        for j in range(i - 1, -1, -1):
            if list_[j] > list_[i]:
                temp = list_[i]
                list_[i] = list_[j]
                while j >= 0 and list_[j] > temp:
                    list_[j + 1] = list_[j]
                    j -= 1
                list_[j + 1] = temp


# l = [4, 9, 3, 1, 2, 5, 8, 4]
# bubble1(l)
# print(l)


###选择排序
def bubble2(list_):
    # for i in range(len(list_) - 1):
    #     min_num = i
    #     for j in range(i + 1, len(list_)):
    #         if list_[min_num] >= list_[j]:
    #             list_[min_num], list_[j] = list_[j], list_[min_num]

    for i in range(len(list_) - 1):#（有问题）
        min_num = i
        for j in range(i + 1, len(list_)):
            if list_[min_num] >= list_[j]:
                min_num = j
            if min_num != i:
                list_[min_num], list_[i] = list_[i], list_[min_num]


l = [4, 9, 3, 1, 2, 5, 8, 4]
bubble2(l)
print(l)

##############老师讲
##############day04am.zip/sort.py
# 选择排序
def select(list_):
    # 没轮选出一个最小值，需要 len(list_) - 1 轮
    for i in range(len(list_) - 1):
        min = i  # 假设 list_[i] 为最小值
        for j in range(i + 1,len(list_)):
            if list_[min] > list_[j]:
                min = j # 擂主换人
        # 进行交换，将最小值换到应该在的位置
        if min != i:
            list_[i],list_[min] = list_[min],list_[i]

# 插入排序
def insert(list_):
    # 控制每次比较的数是谁，从第二个数开始
    for i in range(1,len(list_)):
        x = list_[i]  # 空出list_[i]的位置
        j = i - 1
        while j >= 0 and list_[j] > x:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = x


l = [4,9,3,1,2,5,8,4]
# bubble(l)
# quick(l,0,len(l)-1)
# select(l)
insert(l)

print(l)

