'''
shopping_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

order = []


def gou_wu():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            for key, value in shopping_info.items():
                print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
            while True:
                cid = int(input("请输入商品编号："))
                if cid in shopping_info:
                    break
                else:
                    print("该商品不存在")
            count = int(input("请输入购买数量："))
            order.append({"cid": cid, "count": count})
            print("添加到购物车。")
        elif item == "2":
            zong_jia = 0
            for item in order:
                shang_pin = shopping_info[item["cid"]]
                print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
                zong_jia += shang_pin["price"] * item["count"]
            while True:
                qian = float(input("总价%d元，请输入金额：" % zong_jia))
                if qian >= zong_jia:
                    print("购买成功，找回：%d元。" % (qian - zong_jia))
                    order.clear()
                    break
                else:
                    print("金额不足.")


gou_wu()
'''


dict_target = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def gou_wu():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buy()
        elif item == "2":
            pay()

def pay():
    print_order()
    good_total_money = buy_good_info()
    total_price(good_total_money)


def total_price(good_total_money):
    while True:
        pay_money = float(input("总价%d元，请输入金额：" % good_total_money))
        if pay_money >= good_total_money:
            print("购买成功，找回：%d元。" % (pay_money - good_total_money))
            list_order.clear()
            break
        else:
            print("金额不足.")


def buy_good_info():
    good_total_money =0
    for order in list_order:
        good = dict_target[order["cid"]]
        good_total_money += good["price"] * order["count"]
    return good_total_money


def print_order():
    for order in list_order:
        good = dict_target[order["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (good["name"], good["price"], order["count"]))


def buy():
    good_name_count()
    creat_order()
    print("添加到购物车。")

def creat_order():
    cid = input_good_id()
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    list_order.append(order)



def input_good_id():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_target:
            break
        else:
            print("该商品不存在")
    return cid


def good_name_count():
    """
    获取商品的信息
    :return:
    """
    for key, value in dict_target.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


gou_wu()

########老师讲
dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
        选择菜单
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
        结算
    """
    print_orders()
    total_price = calculate_total_price()
    paying(total_price)


def paying(total_price):
    """
        支付过程
    :param total_price: 需要支付的价格
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足.")


def calculate_total_price():
    """
        计算总价格
    """
    total_price = 0
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        total_price += commodity["price"] * order["count"]
    return total_price


def print_orders():
    """
        打印订单
    """
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], order["count"]))


def buying():
    """
        购买
    """
    print_commodity_info()

    create_order()

    print("添加到购物车。")


def create_order():
    """
        创建订单
    """
    cid = input_commodity_id()
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    list_order.append(order)


def input_commodity_id():
    """
        获取商品订单
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    return cid


def print_commodity_info():
    """
        打印商品信息
    """
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


select_menu()
