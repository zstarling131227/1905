import requests
from lxml import etree

url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
html = requests.get(url=url, headers=headers).text
res = etree.HTML(html)
link = res.xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[2]/td[2]/a/@href')
# link = res.xpath('//a[@class="artitlelist"]/@href')[1]
print(link)

url = 'http://www.mca.gov.cn' + str(link)
print(url)
# two_html = requests.get(url, headers=headers).text
# print(two_html)
