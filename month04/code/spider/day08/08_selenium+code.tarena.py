from selenium import webdriver
import time
import pymysql


class GoverSpider(object):
    def __init__(self):
        self.browesr = webdriver.Chrome()
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.db = pymysql.connect('localhost', 'root', '123456', 'govdb', charset='utf8')
        self.cursion = self.db.cursor()
        self.provice = []
        self.city = []
        self.county = []

    def get_false_page(self):
        self.browesr.get(self.one_url)
        td_list = self.browesr.find_elements_by_xpath('//td[@class="arlisttd"]/a[contains(@title,"代码")]')
        # print(td_list)
        if td_list:
            two_url_element = td_list[0]
            two_url = two_url_element.get_attribute('href')
            sel = 'select * from version where link=%s'
            self.cursion.execute(sel, [two_url])
            if self.cursion.fetchall():
                print('数据已经是最新')
            else:
                # # 注意
                two_url_element.click()
                time.sleep(5)
                all_handle = self.browesr.window_handles
                self.browesr.switch_to_window(all_handle[1])

                self.get_data()
                ins = "insert into version values(%s)"
                self.cursion.execute(ins, [two_url])
                self.db.commit()

    def get_data(self):
        print('哈哈')
        tr_list = self.browesr.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            print(name, code)
            # 判断层级关系,添加到对应的数据库表中(对应表中字段)
            # province: p_name p_code
            # city    : c_name c_code c_father_code
            # county  : x_name x_code x_father_code
            if code[-4:] == '0000':
                self.provice.append([name, code])
                if name in ['北京市', '天津市', '上海市', '重庆市']:
                    city = [name, code, code]
                    self.city.append(city)

            elif code[-2:] == '00':
                city = [name, code, code[:2] + '0000']
                self.city.append(city)
            else:
                # 四个直辖市区县的上一级为: xx0000
                if code[:2] in ['11', '12', '31', '50']:
                    county = [name, code, code[:2] + '0000']
                # 普通省市区县上一级为: xxxx00
                else:
                    county = [name, code, code[:4] + '00']
                # county = [name, code, code[:4] + '00']
                self.county.append(county)

        self.insert_mysql()

    def insert_mysql(self):
        del_pro = 'delete from province'
        del_cit = 'delete from city'
        del_cou = 'delete from county'
        self.cursion.execute(del_pro)
        self.cursion.execute(del_cit)
        self.cursion.execute(del_cou)
        ins_pro = 'insert into province values(%s,%s)'
        ins_cit = 'insert into city values(%s,%s,%s)'
        ins_cou = 'insert into county values(%s,%s,%s)'
        self.cursion.executemany(ins_pro, self.provice)
        self.cursion.executemany(ins_cit, self.city)
        self.cursion.executemany(ins_cou, self.county)
        self.db.commit()
        print('数据抓取完成')

    def main(self):
        self.get_false_page()
        self.cursion.close()
        self.db.close()
        self.browesr.quit()


if __name__ == '__main__':
    sp = GoverSpider()
    sp.main()
