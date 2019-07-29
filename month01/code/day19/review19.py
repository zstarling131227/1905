############练习１
"""

"""
# def verify_permissions(func):
#     def wrapper(*args, **kwargs):#########参数的数量不固定，所以用＊
#        print("账号验证")
#        func(*args,**kwargs)
#     return wrapper
#
# @verify_permissions
# def deposit(money):
#     print("存%d钱喽"%money)
#
# @verify_permissions
# def withdraw(login_id,pwd):
#     print("取钱喽",login_id,pwd)
#
# deposit(1000000)
# withdraw("王八蛋",131227)

############练习２
"""

"""
import time

def print_time(func):
    def wrapper(*args,**kwargs):
        ##记录调用前的时间
        start_time=time.time()
        result=func(*args,**kwargs)
        ##记录调用后的时间
        execute_time=time.time()-start_time
        print("执行时间是：", execute_time)
        return result
    return wrapper

@print_time
def fun01():
    time.sleep(2)
    print("王八蛋")
@print_time
def fun02(a):
    time.sleep(1)
    print("钥玥",a)

fun01()
fun02("&")















