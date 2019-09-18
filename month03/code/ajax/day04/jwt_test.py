import hmac
import base64
import json
import time
import copy


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):
        header = {'alg': 'HS256', 'typ': 'JWT'}
        header_json = json.dumps(header, separators=('', ':'), sort_keys=True)
        header_bs = base64.b64encode(header_json.encode())

        payload_self = copy.deepcopy(payload)
        if not isinstance(exp, int) and not isinstance(exp, str):
            raise TypeError('Exp must be str or int!')
        payload_self['exp'] = time.time() + int(exp)
        payload_json = json.dumps(payload_self, separators=(',', ':'), sort_keys=True)
        payload_bs = base64.b64encode(payload_json.encode())

        if isinstance(key, str):
            key = key.encode()
        str_ = header_bs + b'.' + payload_bs
        h = hmac.new(key, str_, digestmod='SHA256')
        sign = h.digest()
        sign_bs = base64.urlsafe_b64encode(sign)

        return header_bs + b'.' + payload_bs + b'.' + sign_bs


if __name__ == '__main__':
    jwt = Jwt()
    token = jwt.encode({'username': 'xixi'}, '123456', 90)
    print(token)
