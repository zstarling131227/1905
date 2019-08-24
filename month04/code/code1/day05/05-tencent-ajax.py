import requests

import json


class TencentSpider(object):
    def __init__(self):
        self.one_url ='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1559294378106&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1559&postId={}&language=zh-cn'

        self.headers = {
            'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                          '76.0.3809.100Safari / 537.36'
        }

    def get_page(self, url):
        res = requests.get(url, headers=self.headers)
        html = json.loads(res.text)
        return html

    def parse_one_page(self, html):
        # 根据preview的结果写结构
        for job in html['Data']['Posts']:
            job_name = job['RecruitPostName']
            post_id = job['PostId']
            two_level = self.two_url.format(post_id)
            job_duty, job_requirement = self.parse_two_page(two_level)
            dic = {
                'name': job_name,
                'duty': job_duty,
                'require': job_requirement
            }
            print(dic)

    def parse_two_page(self, two_level):
        html = self.get_page(two_level)
        job_requirement = html['Data']['Requirement']
        job_duty = html['Data']['Responsibility']
        return job_duty, job_requirement

    def main(self):
        for pageindex in range(1, 11):
            url = self.one_url.format(str(pageindex))
            html = self.get_page(url)
            self.parse_one_page(html)


if __name__ == '__main__':
    spider = TencentSpider()
    spider.main()
