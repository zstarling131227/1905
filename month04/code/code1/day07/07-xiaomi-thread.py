import time, json
from queue import Queue
# 首选多线程
from threading import Thread

import requests


class XiaomiSplder(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page=0&categoryId=2&pageSize=30'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        self.app_queue = Queue()
        self.i = 0

    def url_in(self):
        for i in range(67):
            url = self.url.format(i)
            self.app_queue.put(url)

    def get_data(self):
        while True:
            if self.app_queue.empty():
                break
            url = self.app_queue.get()
            html = requests.get(url=url, headers=self.header).content.decode('utf-8')
            html = json.loads(html)
            with open('xiaomi.json', 'a') as f:
                app_dict = {}
                for i in html['data']:
                    app_dict['app_name'] = i['displayName']
                    # app_name = i['displayName']
                    app_dict['app_link'] = 'http://app.mi.com/details?id=' + i['packageName']
                    # app_link = 'http://app.mi.com/details?id=' + i['packageName']
                    # print(app_name, app_link)
                    self.i += 1
                    json.dump(app_dict, f, ensure_ascii=False)
                    # return app_name, app_link

    def main(self):
        self.url_in()
        t_list = []
        for i in range(100):
            t = Thread(target=self.get_data)
            t_list.append(t)
            t.start()
        for i in t_list:
            i.join()
        print(self.i)


if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSplder()
    spider.main()
    end = time.time()
    print('执行时间：%.2f' % (end - start))
