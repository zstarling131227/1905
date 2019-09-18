import redis, time, random
from multiprocessing import Process


class Spider(object):
    def __init__(self):
        self.r = redis.Redis('localhost', 6379, 0)

    def product(self):
        for page in range(67):
            url_list = 'http%s' % str(page)
            self.r.lpush('url1', url_list)
            time.sleep(random.randint(1, 3))

    def consum(self):
        while True:
            url = self.r.brpop('url1', 4)
            if url:
                # print(url) # #(b'url1', b'http0')
                print(url[1].decode())
            else:
                break

    def run(self):
        p1 = Process(target=self.product)
        p2 = Process(target=self.consum)
        p1.start()
        p2.start()
        p1.join()
        p2.join()


if __name__ == '__main__':
    sp = Spider()
    sp.run()
