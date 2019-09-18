import time

from selenium import webdriver


class JdSpider(object):
    def __init__(self):
        self.brower = webdriver.Chrome()
        self.url = 'https://www.jd.com/'
        self.i = 0

    def get_page(self):
        self.brower.get(self.url)
        self.brower.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书籍')
        self.brower.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    def parse_page(self):
        # 把进度条拉到最下面
        self.brower.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(1)

        r_list = self.brower.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        # print(r_list)

        for i in r_list:
            # print(i.text)
            # print('*' * 50)
            info = i.text.split('\n')
            if info[0].startswith('每满'):
                price = info[1]
                name = info[2]
                number = info[3]
                market = info[4]
            elif info[0] == "单件":
                price = info[3]
                name = info[4]
                number = info[5]
                market = info[6]
            elif info[0].startswith('￥') and info[1].startswith('￥'):
                price = info[0]
                name = info[2]
                number = info[3]
                market = info[4]
            else:
                price = info[0]
                name = info[1]
                number = info[2]
                market = info[3]
            dic = {
                'price': price,
                'name': name,
                'number': number,
                'market': market
            }
            print(dic)
            self.i += 1

    def main(self):
        self.get_page()
        # while True:
        for i in range(2):
            self.parse_page()
            if self.brower.page_source.find('pn-next disabled') == -1:
                self.brower.find_element_by_class_name('pn-next').click()
                time.sleep(2)
            else:
                self.brower.quit()
                break
        print(self.i)


if __name__ == '__main__':
    spider = JdSpider()
    spider.main()
