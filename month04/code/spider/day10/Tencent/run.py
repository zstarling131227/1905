from scrapy import cmdline

cmdline.execute('scrapy crawl tencent'.split())
# #直接添加-o 文件名
# cmdline.execute('scrapy crawl tencent -o tencent.csv'.split())
