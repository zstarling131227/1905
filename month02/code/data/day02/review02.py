"""
sstack.py 栈模型的顺序存储
重点代码

思路总结：
1. 列表即顺序存储，但功能多，不符合栈的模型特征
2. 利用列表 将其封装，提供接口方法
"""
class SStackError(Exception):
    pass
#顺序栈类
class SStack:
    def __init__(self):
        self._element=[]

    def is_empty(self):
        return self._element==[]

    def push(self,val):
        return self._element.append(val)

    def pop(self):
        if self.is_empty():
            raise SStackError("Stack is empty")
        return self._element.pop()

    def top(self):
        if self.is_empty():
            raise SStackError("Stack is empty")
        return self._element[-1]

# if __name__ == "__main__":
#     st = SStack()
#     st.push(10)
#     st.push(20)
#     st.push(30)
#     st.push(40)
#     while not st.is_empty():
#         print(st.pop())


"""
lstack.py  栈的链式栈
重点代码

思路分析：
1. 源于链表结构
2. 封装栈的操作方法（入栈，出栈，栈空，栈顶元素）
3. 链表的开头作为栈顶 ？ （不用每次遍历）
"""

class LStackError(Exception):
    pass

class LSNode:
    def __init__(self,val,next=None):
        self.val =val
        self.next=next

class LStack:
    def __init__(self):
        self._top=None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        self._top=LSNode(val,self._top)

    def pop(self):
        if self._top is None:
            raise LStackError("stack is None")
        value=self._top.val
        self._top=self._top.next
        return value

    def top(self):
        if self._top is None:
            raise LStackError("stack is None")
        return self._top.val

# if __name__=="__main__":
#     st=LStack()
#     st.push(23)
#     st.push(3)
#     st.push(2)
#     print(st.pop())
#     print(st.pop())
#     print(st.pop())

"""
squeue.py 队列的顺序存储

思路分析：
1. 基于列表完成数据存储
2. 通过封装规定数据操作
3. 先确定列表的哪一段作为队头
"""

class SqueueError(Exception):
    pass

###队列变化
class Squeue:
    def __init__(self):
        self._elements=[]

    def is_empty(self):
        return self._elements ==[]

    def enqueue(self,val):
        return self._elements.append(val)

    def dequeue(self):
        if self.is_empty():
            raise SqueueError("Squeue is empty")
        return self._elements.pop(0)

# if __name__=="__main__" :
#     sq=Squeue()
#     sq.enqueue(23)
#     sq.enqueue(3)
#     sq.enqueue(2)
#     # print(sq.dequeue())
#     # print(sq.dequeue())
#     # print(sq.dequeue())
#     while not sq.is_empty():
#         print(sq.dequeue())

# ###队头变队尾(通过栈)
# if __name__=="__main__" :
#     sq=Squeue()
#     for i in range(10):
#         sq.enqueue(i)
#     st=SStack()
#     while not sq.is_empty():
#         st.push(sq.dequeue())
#     while not st.is_empty():
#         sq.enqueue(st.pop())
#     while not sq.is_empty():
#         print(sq.dequeue())

"""
lqueue.py  链式队列
重点代码

思路分析：
1. 基于链表构建队列模型
2. 链表的开端作为队头，结尾位置作为队尾
3. 单独定义队尾标记，避免每次插入数据遍历
4. 队头和队尾重叠认为队列为空
"""
class LqueueError(Exception):
    pass
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next=next

class Lqueue:
    def __init__(self):
        self.front=self.rear=Node(None)

    def is_empty(self):
        return self.front ==self.rear

    def enqueue(self,val):
        self.rear.next=Node(val)
        self.rear=self.rear.next

    def dequeue(self):
        if self.front==self.rear:
            raise LqueueError("queue is empty")
        self.front=self.front.next
        return self.front.val

# if __name__ == "__main__":
#     lq = Lqueue()
#     lq.enqueue(10)
#     lq.enqueue(20)
#     lq.enqueue(30)
#     print(lq.dequeue())

