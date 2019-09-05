import random
from threading import Thread

import requests


def get_requset():
    url1 = 'http://127.0.0.1:8000/test/'
    url2 = 'http://127.0.0.1:8001/test/'
    url = random.choice([url1, url2])
    requests.get(url)


t_list = []
for i in range(30):
    t = Thread(target=get_requset)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()
