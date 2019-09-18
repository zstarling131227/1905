import requests, time, random
from hashlib import md5


def get_salt_sign_ts(word):
    ts = str(int(time.time() * 1000))
    salt = str(int(time.time() * 1000)) + str(random.randint(0, 9))
    string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
    s = md5()
    s.update(string.encode())
    sign = s.hexdigest()
    # print(salt, '\n', sign, '\n', ts)
    return salt, sign, ts


def attack_yd(word):
    salt, sign, ts = get_salt_sign_ts(word)
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "244",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "ntes_nnid=753292a885f26a669e6c259a451c2a05,1565779212369; "
                  "OUTFOX_SEARCH_USER_ID_NCOO=1256349591.9709954; OUTFOX_SEARCH_USER_ID=-1944207920@122.224.206.179; JSESSIONID=aaa0NEXRcckFtaVH0kcZw; ___rl__test__cookies=1566625747693",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Pragma": "no-cache",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    # headers = {
    #     "Cookie": "ntes_nnid=753292a885f26a669e6c259a451c2a05,1565779212369; OUTFOX_SEARCH_USER_ID_NCOO=1256349591.9709954; OUTFOX_SEARCH_USER_ID=-1944207920@122.224.206.179; JSESSIONID=aaa0NEXRcckFtaVH0kcZw; ___rl__test__cookies=1566625747693",
    #     "Referer": "http://fanyi.youdao.com/",
    #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    # }

    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": "e2baf4b7602e0ecc32bd1350facecf0b",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    html = requests.post(url, data=data, headers=headers).text
    # html = requests.post(url, data=data, headers=headers).json
    print(html)
    # print(type(html))


if __name__ == '__main__':
    word = input("输入单词：")
    attack_yd(word)
