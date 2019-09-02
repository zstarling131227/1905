###合并列表并排序
#####day02/day02_all.zip/exec_1.py
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = Node(None)

    def link_list(self, list_):
        p = self.head
        for i in list_:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:  # ##对象判断用is和is not ,判断值时用!=和==
            print(p.val)
            p = p.next

    def insert_list(self,list01, list02):
        p = list01.head
        q = list02.head.next
        while p.next is not None:
            if p.next.val < q.val:
                p = p.next
            else:
                tem = p.next
                p.next = q
                p = p.next
                q = tem
        p.next = q

# def insert_list(list01, list02):
#     p = list01.head
#     q = list02.head.next
#     while p.next is not None:
#         if p.next.val < q.val:
#             p = p.next
#         else:
#             tem = p.next
#             p.next = q
#             p = p.next
#             q = tem
#     p.next = q

list01 = [1, 2, 3, 545]
list02 = [3, 4, 5, 54]
l01 = LinkList()
l02 = LinkList()
l01.link_list(list01)
l02.link_list(list02)

l01.insert_list(l01, l02)######函数在类里的执行语句
# insert_list(l01, l02)######函数在类外的执行语句
l01.show()
# l02.show()
