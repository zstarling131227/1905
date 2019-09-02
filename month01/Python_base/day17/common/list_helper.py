"""
    列表助手模块
"""

class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target,func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item


class ListHelper1:
    """
        列表助手类
    """
    @staticmethod
    def find_single(list_target, fun_condition):
        """
              通用的查找某个条件下元素方法
          :param list_target: 需要查找的列表
          :param func_condition: 需要查找的条件,函数类型
                  函数名(参数) --> bool
          :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if fun_condition(item):
                return item

    @staticmethod
    def find_lambda(list_target, fun_codition):
        """
            通用的查找某个条件下所有元素的数量方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        count = 0
        for item in list_target:
            if fun_codition(item):
                count += 1
        return count

    @staticmethod
    def find_emeny(list_target, fun_condition):
        for item in list_target:
            if fun_condition(item):
                return True
