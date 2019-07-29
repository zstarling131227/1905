
shopping_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

order = []

class Shopping:
    def shopping(self):
        """
            购物
        :return:
        """
        while True:
            item = input("1键购买，2键结算。")
            if item == "1":
                self.buying()
            elif item == "2":
                self.paying()

class Paying:
    def paying(self):
        total_money = self.caculate_money()
        self.settle_money(total_money)


    def settle_money(total_money):
        while True:
            pay_money = float(input("总价%d元，请输入金额：" % total_money))
            if pay_money >= total_money:
                print("购买成功，找回：%d元。" % (pay_money - total_money))
                order.clear()
                break
            else:
                print("金额不足.")


    def caculate_money(self):
        total_money = 0
        for item in order:
            good = shopping_info[item["cid"]]
            print("商品：%s，单价：%d,数量:%d." % (good["name"], good["price"], item["count"]))
            total_money += good["price"] * item["count"]
        return total_money

class Buying:
    def buying(self):
        self.good_list_info()
        self.creat_order()
        print("添加到购物车。")


    def creat_order(self):
        cid = self.add_good()
        count = int(input("请输入购买数量："))
        order.append({"cid": cid, "count": count})


    def add_good(self):
        while True:
            cid = int(input("请输入商品编号："))
            if cid in shopping_info:
                break
            else:
                print("该商品不存在")
        return cid


    def good_list_info(self):
        for key, value in shopping_info.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


s01=Shopping()
s01.shopping()
