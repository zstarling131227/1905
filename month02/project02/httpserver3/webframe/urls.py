"""
可以接收客户端什么样的数据访问
"""
from views import *

urls=[
    ('/time',show_time),
    ('/hello',hello),
    ('/bye',bye)
]