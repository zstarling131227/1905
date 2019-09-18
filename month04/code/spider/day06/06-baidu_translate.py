import re
import requests
import execjs


class BaiduTranslateSpider(object):
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/translate?aldtype=16047'
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "cookie": "BIDUPSID=C2D88AA0D52C8427FFEE1DC2987C937B; BAIDUID=8362FAE9A355F563262E818E05DF61DE:FG=1; PSTM=1560427890; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=5; locale=zh; H_PS_PSSID=1436_21088_29522_29519_29721_29568_29221; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1566967453,1567046793,1567076846,1567078233; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1567078317; __yjsv5_shitong=1.0_7_a0e260fac40a3d87c2c889a344d57e3c42a1_300_1567078318268_122.224.206.179_30a61f5b; yjs_js_security_passport=d854a9891aaed57aec856352c1e99355b74bdb9d_1567078318_js",
            "pragma": "no-cache",
            "sec-fetch-site": "none",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        }

    def get_token(self):
        html = requests.get(
            url=self.get_url,
            headers=self.headers
        ).text
        # pattern = re.compile("token: '(.*?)'.*systime", re.S)
        pattern = re.compile("token: '(.*?)'.*systime", re.S)
        token = pattern.findall(html)[0]
        return token

    def get_sign(self, word):
        with open('node.js', 'r') as f:
            js_data = f.read()
        execjs_obj = execjs.compile(js_data)
        sign = execjs_obj.eval('e("{}")'.format(word))
        return sign

    def get_result(self, word, f, t):
        # def get_result(self, word):
        token = self.get_token()
        sign = self.get_sign(word)
        formdata = {
            # "from": "en",
            # "to": "zh",

            "from": f,
            "to": t,

            # "from": 'auto',
            # "to": 'auto',

            "query": word,
            "simple_means_flag": "3",
            "sign": sign,
            "token": token,
        }
        html_json = requests.post(
            url='https://fanyi.baidu.com/v2transapi',
            data=formdata,
            headers=self.headers
        ).json()
        # print(html_json)
        result = html_json['trans_result']['data'][0]['dst']
        return result


if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    choice = input('1.英译汉 2.汉译英  >>')
    if choice == '1':
        f = 'en'
        t = 'zh'
    elif choice == '2':
        f = 'zh'
        t = 'en'
    else:
        raise ValueError
    word = input('word:>>')
    # print(res)
    # print(spider.get_token())
    # print(spider.get_sign(word))
    res = spider.get_result(word, f, t)
    # res = spider.get_result(word)
    print(res)
