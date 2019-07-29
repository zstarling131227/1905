class ListHelper:
    """
        列表助手类
    """
    @staticmethod
    def find_all(list_target, func_condition):
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, fun_condition):
        for item in list_target:
            if fun_condition(item):
                return item

    @staticmethod
    def sum_enemy(list_target, fun_condition):
        sum_value = 0
        for i in list_target:
            sum_value += fun_condition(i)
        return sum_value

    @staticmethod
    def cancle(list_target, con):
        list_result = []
        for item in list_target:
            list_result.append(con(item))
        return list_result

    ####ｃａｎｃｌｅ方法的改进版（因为后返回的是列表，含有多个变量，可以直接用ｙｉｅｌｄ返回）
    @staticmethod
    def cancle1(list_target, con):
        for item in list_target:
            yield con(item)

    @staticmethod
    def max_enemy(list_target, con):
        max_value = con(list_target[0])
        for item in range(len(list_target)):
            if max_value < con(list_target[item]):
                max_value = con(list_target[item])
        return max_value


    @staticmethod
    def max_enemy1(list_target, con):
        max_value = list_target[0]
        for item in range(len(list_target)):
            if con(max_value) < con(list_target[item]):
                max_value = list_target[item]
        return max_value

    @staticmethod###(升序)
    def sort_enemy(list_target, con):
        for i in range(len(list_target)):
            for j in range(i, len(list_target)):
                if con(list_target[i]) > con(list_target[j]):
                    list_target[j] , list_target[i] = list_target[i], list_target[j]
        # return list_target

    @staticmethod
    def min_enemy(list_target, con):
        min_value = con(list_target[0])
        for item in range(len(list_target)):
            if min_value > con(list_target[item]):
                min_value = con(list_target[item])
        return min_value


    @staticmethod
    def min_enemy1(list_target, con):
        min_value = list_target[0]
        for item in range(len(list_target)):
            if con(min_value) > con(list_target[item]):
                min_value = list_target[item]
        return min_value

    @staticmethod###(降序)
    def sort_enemy1(list_target, con):
        for i in range(len(list_target)):
            for j in range(i, len(list_target)):
                if con(list_target[i]) < con(list_target[j]):
                    list_target[j] , list_target[i] = list_target[i], list_target[j]
        return list_target

    @staticmethod
    def del_enemy(list_target, con):
        for item in range(len(list_target) - 1, -1, -1):
            if con(list_target[item]):
                list_target.remove(list_target[item])
        return list_target
