from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com')
browser.save_screenshot('no-baidu.png')
