import requests
from lxml import etree

url = 'http://www.renren.com/972075120/profile'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "anonymid=jzpjpf0i-p8bdd2; _r01_=1; depovince=ZJ; JSESSIONID=abccOe5Mi8Qel5XYjOvZw; ick_login=61f78a29-e531-45a9-9220-6249907f9b2a; ick=331b2b9f-4f84-4b7d-9cb8-bc75c627cbf3; jebe_key=2ae0e677-900f-4b6a-a10e-31e4b975a5f2%7C8b05e28c4146ecdc7149a749edea230c%7C1566952730065%7C1%7C1566952731519; jebe_key=2ae0e677-900f-4b6a-a10e-31e4b975a5f2%7C8b05e28c4146ecdc7149a749edea230c%7C1566952730065%7C1%7C1566952731521; first_login_flag=1; vip=1; XNESSESSIONID=7d96481d5c7e; wp=0; wp_fold=0; ln_uact=1239269939@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20190828/0925/h_main_29dq_0c170002943c195a.jpg; jebecookies=509d3741-52b9-4f0c-aac7-dabbce0fc35c|||||; _de=15F03357259F3E408863BD1FF30A778D6DEBB8C2103DE356; p=b5740d1d802dca1852ec74817505a59c0; t=c4d1ea02f35164b83d55ce50c30a74a70; societyguester=c4d1ea02f35164b83d55ce50c30a74a70; id=972075120; xnsid=2a205cf7; loginfrom=syshome",
    "Host": "www.renren.com",
    "Pragma": "no-cache",
    "Referer": "http://www.renren.com/SysHome.do",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}
html = requests.get(url, headers=headers).text
# print(html)

parse_html = etree.HTML(html)
r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
print(r_list)
