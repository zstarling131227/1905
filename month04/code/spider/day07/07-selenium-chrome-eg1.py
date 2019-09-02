from selenium import webdriver

# #未添加环境变量时，需要手动添加（下载后解压的文件路径）
# browser = webdriver.Chrome(executable_path='/home/tarena/software/chromedriver_linux64/chromedriver')
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')
# browser.quit()

# browser = webdriver.Firefox()
# browser.get('http://www.baidu.com/')
# browser.quit()

# ##在内存中
browser1 = webdriver.PhantomJS()
browser1.get('http://www.baidu.com/')
browser1.save_screenshot('baidu.png')
browser1.quit()
