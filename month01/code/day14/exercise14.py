"""
1. 三合一
3. 阅读代码 shopping_oo.py
   体会：面向过程与面向对象的区别
4. 穷尽一切手段，在互联网中搜索"六大原则"的相关资料.
   并结合课堂所讲(理论/代码)，总结为面向对象答辩的内容.
"""
"""
2. 将学生管理系统分为四个模块
M  --> model.py 数据模块
V  --> ui.py  界面模块
C  --> bll.py 业务逻辑模块
将调用View的代码--> main.py 入口模块
"""
##整体导入方式
import student_model as s01
view = s01.StudentManagerView()
view.main()
##结果在project01中，分块导入方式（model.py,ul.py,bll.py)，结果输出在main.py中.