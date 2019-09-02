import requests
from lxml import etree

url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
html = requests.get(url=url, headers=headers).text

# link = res.xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[2]/td[2]/a/@href')
res = etree.HTML(html)
# r_list = res.xpath('//a[@class="artitlelist"]/@href')
r_list = res.xpath('//a[@class="artitlelist"]/@href')[1]
# 一级页面
# print(r_list)
two_level_url = "http://www.mca.gov.cn" + r_list
# 二级页面
# print(two_level_url)

two_html = requests.get(two_level_url, headers=headers).text
two_res = etree.HTML(two_html)
two_list = two_res.xpath('/td[3]/text()')
print(two_list)
