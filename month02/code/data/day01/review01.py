########linklist.py(看图)
"""
linklist.py
功能：　实现单链表的构建和功能操作
重点代码
"""
# 　创建节点类
class Node:
    """
    思路：　将自定义的类视为节点的生成类，实例对象中
    　　　　包含数据部分和指向下一个节点的ｎｅｘｔ
    """

    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环下一个节点关系


# 　做链表操作
class LinkList:
    """
        思路：　单链表类，生成对象可以进行增删改查操作
    　　　　具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):####(看ｄａｙ01_ｌｉｎｋ图片)
        p = self.head  ###ｐ作为移动变量
        for item in list_:
            # node=Node(item)###创建节点
            # p.next=node###ｈｅａｄ的下一个节点与创建的节点链接
            # p=node####ｈｅａｄ与节点相连

            ####上述简化为下列代码
            p.next = Node(item)
            p = p.next

        return list_

    #####遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:  # ##对象判断用is和is not ,判断值时用!=和==
            print(p.val)
            p = p.next  ####p向后移


    ####判断链表为空
    def is_empty(self):
        return self.head.next is None

    ###清空链表
    def clear(self):
        self.head.next = None

    ###尾部插入(有问题)
    def append_end(self,val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next=Node(val)

    ###插入头部
    def append_begin(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    ###指定插入位置
    def fixed_append(self, index, val):
        a = self.head
        for i in range(index):
            if a.next is None:
                break
            a = a.next

        p = Node(val)
        p.next = a.next
        a.next = p

    ####删除节点
    def delete(self, x):
        p = self.head
        while  p.next and p.next.val!=x :#####确认节点存在且不是要删除的节点（查找要删除的节点）（循环结束时，输出的是P节点）
            p=p.next

        if p.next is None:
            raise ValueError("x not in linklist")#####若要删除的节点是最后一个节点则报错．
        else:
            p.next = p.next.next

    ###获取索引(获取某个节点值,传入节点位置获取节点值)#####根据索引获取该索引位置的元素．
    def get_index(self, index):
        if index < 0:
            raise IndexError("index out of range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val


list01=[1,24,35,43,532]
l=LinkList()
l.init_list(list01)
l.show()
# print("-----")
# l.delete(24)
# l.show()
# print("-----")
# print(l.get_index(3))
# print("-----")
# l.fixed_append(3,7)
# l.show()
# print("-----")
# l.append_begin(9)
# l.show()
# print("-----")
# l.append_end(0)
# l.show()
# print("-----")
# print(l.is_empty())

# print("-----")
# l.clear()
# l.show()
# print("-----")
