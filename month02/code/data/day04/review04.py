##############search.py
"""
search.py 二分查找方法训练
"""
def serach(list_,key):
    min_num,max_num=0,len(list_)-1
    while min_num<max_num:
        mid_num=(min_num+max_num)//2
        if list_[mid_num]<key:
            min_num=mid_num+1
        elif list_[mid_num]>key:
            max_num=mid_num-1
        elif list_[mid_num]==key:
            return mid_num
l=[1,2,3,4,5,6,7,8,9,10]
print("key index:",serach(l,8))




