import time
class student:
    def get_birth(year, month, day):
        tuple_time01 = time.strptime("%d / %d / %d" % (year, month, day), "%Y / %m / %d")
        #####自己写的，计算的是总天数。
        print(tuple_time01)  ##目的：调试
        print(tuple_time01[7])
student.get_birth(2019,9,20)
