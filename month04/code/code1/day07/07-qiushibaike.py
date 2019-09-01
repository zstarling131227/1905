from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('https://www.qiushibaike.com/text/')

# xpath = '//div[@class="content"]/span'
# xpath = '//div[@class="content"]'
# span = browser.find_element_by_xpath(xpath)
# print(span.text)

xpath = '//div[@class="content"]/span'
span = browser.find_elements_by_xpath(xpath)
print(span)
for s in span:
    print(s)

