import requests

##选中注册，进入检查（F12）。寻找地址
post_url = 'http://www.renren.com/PLogin.do'
get_url = 'http://www.renren.com/profile'
post_data = {'email': '17805052058', 'password': 'zxl199694'}
headers = {
    "Referer": "http://www.renren.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",

}

session = requests.session()
session.post(
    url=post_url, data=post_data, headers=headers
)
html = session.get(url=get_url, headers=headers).text
print(html)
