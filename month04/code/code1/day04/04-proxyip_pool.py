from getip import get_ip
import requests,random

url='http://httpbin.org/get'
headers={'User-Agent': 'Mozilla/5.0'}
ip_list=get_ip()
while True:
    proxy_ip=random.choice(ip_list)
    proxies={
        'http': 'http://{}'.format(proxy_ip),
        'https': 'https://{}'.format(proxy_ip),
    }
    print(proxies)
    try:
        html=requests.get(url,proxies=proxies,headers=headers).text
        print(html)
        break
    except Exception as err:
        ip_list.remove(proxy_ip)
        print("已删除！%s" % proxy_ip)
        continue
