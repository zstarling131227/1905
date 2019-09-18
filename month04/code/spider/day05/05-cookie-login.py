import requests
from lxml import etree

url = ''
headers = {

}
html = requests.get(url, headers=headers).text
parse_html = etree.HTML(html)
result = parse_html.xpath('')
print(result)
