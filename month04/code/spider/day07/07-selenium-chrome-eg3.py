from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# html = browser.page_source
# html = browser.page_source.find('百度') # #409
html = browser.page_source.find('aaaaaaaaaaas')  # # 没找到返回-1，其余返回非-1
print(html)
