"""
界面代码
"""
import model as m01
import bll
class StudentManagerView:
    """
    学生管理器视图
    """

    def __init__(self):
        self.__manager = bll.StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            pass

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = m01.StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        id = int(input("请输入编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = m01.StudentModel()
        stu.id = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入新的学生名称：")
        stu.age = int(input("请输入新的学生年龄："))
        stu.score = int(input("请输入新的学生成绩："))
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

view = StudentManagerView()
view.main()