import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0'}
proxies = {
    # 'http': 'http://112.85.172.77:9999',
    # 'https': 'https://112.85.172.77:9999//',
    'http': 'http://218.91.112.47:9999',
    'https': 'https://218.91.112.47:9999//',
    # 'http': 'http://60.13.42.86:9999',
    # 'https': 'https://60.13.42.86:9999//'
}

html = requests.get(url=url, headers=headers, proxies=proxies).text
print(html)
