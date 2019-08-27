import hmac
import base64
import json
import time
import copy


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def b64encode(content):
        return base64.b64encode(content).replace(b'=', b'')

    @staticmethod
    def b64decode(b):
        s = len(b) % 4 != 0
        if s > 0:
            b += b'=' * (4 - s)
        return base64.b64decode(b)

    @staticmethod
    def encode(payload, key, exp=300):
        header = {'alg': 'HS256', 'typ': 'JWT'}
        header_json = json.dumps(header, separators=('', ':'), sort_keys=True)
        header_bs = jwt.b64encode(header_json.encode())

        payload_self = copy.deepcopy(payload)
        if not isinstance(exp, int) and not isinstance(exp, str):
            raise TypeError('Exp must be str or int!')
        payload_self['exp'] = time.time() + int(exp)
        payload_json = json.dumps(payload_self, separators=(',', ':'), sort_keys=True)
        payload_bs = jwt.b64encode(payload_json.encode())

        if isinstance(key, str):
            key = key.encode()
        str_ = header_bs + b'.' + payload_bs
        h = hmac.new(key, str_, digestmod='SHA256')
        sign = h.digest()
        sign_bs = jwt.b64encode(sign)

        return header_bs + b'.' + payload_bs + b'.' + sign_bs

    b'eyJhbGciOiJIUzI1NiIidHlwIjoiSldUIn0=.' \
    b'eyJleHAiOjE1NjY4OTc3MDYuMjg1ODg5NiwidXNlcm5hbWUiOiJ4aXhpIn0=.' \
    b'ct6GbHrW3sn4N3IJvTV8Knmj5eZTNQvmVmnswoGqS1E='

    @staticmethod
    def decode(token, key):
        # s=jwt.b64decode(token).decode().split('.')
        # header_bs, payload_bs, sign_bs = token.decode().split('.')
        header_bs, payload_bs, sign_bs = token.split(b'.')

        if isinstance(key, str):
            print(key)
            key = key.encode()
            print(key)
        str_ = header_bs + b'.' + payload_bs
        print(str_)
        h = hmac.new(key, str_, digestmod='SHA256')
        print(h)
        sign = h.digest()
        print(sign)
        if sign_bs != Jwt.b64encode(sign):
            raise ValueError

        payload_json = Jwt.b64decode(payload_bs)  ##结果为字节串
        payload = json.loads(payload_json)
        if 'exp' in payload:
            now = time.time()
            if now > payload['exp']:
                raise ValueError('已过期')
        return payload





if __name__ == '__main__':
    jwt = Jwt()
    token = jwt.encode({'username': 'xixi'}, '123456', 90)
    print(token)
    toke = jwt.decode(token, '123456')
    print(toke)
