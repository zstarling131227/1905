"""
day13 作业
1. 三合一
2. 根据需求，画出当前练习设计图.

4. 将面向过程的购物车，改为面向对象的购物车.
5. (扩展)画出天龙八部3D手游技能系统框架图。
6. 穷尽一切手段，在互联网中搜索"继承多态"的相关资料.
   并结合课堂所讲(理论/代码)，总结为面向对象答辩的内容.
"""
####作业３
"""
    定义员工管理器(看内存图ｄａｙ14)
        1.管理所有员工
        2. 计算所有员工工资

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变.

"""
class EmployeeManager:
    def __init__(self):
        self._employees = []

    def add_employees(self, employee):
        if isinstance(employee, Employee):
            self._employees.append(employee)
        else:
            raise ValueError

    def get_total_wage(self):
        total_wage = 0
        for item in self._employees:
            total_wage += item.caculate_wage()
        return total_wage

class Employee:
    ###补充
    def __init__(self,basic_wage):
        self.basic_wage=basic_wage
    def caculate_wage(self):
        # raise NotImplementedError()
        return self.basic_wage

# -----------------------------------
class Programmer(Employee):
    def __init__(self, basic_wage, bonus):
        super().__init__(basic_wage)
        # self.basic_wage = basic_wage
        self.bonus = bonus

    def caculate_wage(self):
        return self.basic_wage + self.bonus


class Saler(Employee):
    def __init__(self, basic_wage, bonus):
        super().__init__(basic_wage)
        # self.basic_wage = basic_wage
        self.bonus = bonus

    def caculate_wage(self):
        return self.basic_wage + self.bonus * 0.05

p01=Programmer(10000,9000)
s01=Saler(100000,99999)
employee=EmployeeManager()
employee.add_employees(p01)
employee.add_employees(s01)
re=employee.get_total_wage()
print(re)
####老师讲
class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        self.__employees.append(emp)

    def get_total_saraly(self):
        total_saraly = 0
        for item in self.__employees:
            # 调用是抽象的员工类
            # 执行是具体的员工(程序员/销售..)
            total_saraly += item.calculate_salary()
        return total_saraly

class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

# ---------------------------------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.base_salary + self.bonus
        # 扩展重写
        return super().calculate_salary()+ self.bonus


class Salesmen(Employee):
    def __init__(self, base_salary, sale_value):
        super().__init__(base_salary)
        self.sale_value = sale_value

    def calculate_salary(self):
        return self.base_salary + self.sale_value * 0.05


# 测试
manager = EmployeeManager()
manager.add_employee(Programmer(200000,500))
manager.add_employee(Salesmen(2000,1000))
print(manager.get_total_saraly())

