"""
程序入口
"""
import ui
view = ui.StudentManagerView()
view.main()

###day15__name__举例

from bll import *

# 限制只能从当前模块才执行。
if __name__ =="__main__":
    view = StudentManagerView()
    view.main()