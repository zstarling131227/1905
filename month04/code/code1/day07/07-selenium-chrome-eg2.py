from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# word = input('>>')
# browser.find_element_by_id('kw').send_keys(word)
browser.find_element_by_id('kw').send_keys('华晨宇')
browser.find_element_by_id('su').click()


time.sleep(2)
browser.find_element_by_class_name('n').click()
# browser.quit()
