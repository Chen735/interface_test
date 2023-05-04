import requests
import hashlib
import uuid
from handle.handle_log import info_log

class BaseRequest():

    def handle_header(self):
        nonce = str(uuid.uuid4())
        version_key = '0EAE2E06-1830-454D-9695-EC5BD651E8CF'
        sign = nonce + version_key
        m = hashlib.md5()
        m.update(bytes(sign, encoding='utf8'))
        result = m.hexdigest()
        header = {
            "X-NONCE": nonce,
            "X-SIGNATURE": result,
            "X-TOKEN": "fbeb55f3-3f41-47e6-989c-63dcec2ee20b",
            "X-VERSION": "linkr-dev-web-1.0",
            "content-type": "application/json"
        }
        return header

    def post(self, url, data=None, headers=None):
        if headers is None:
            headers = self.handle_header()
        if data is not None:
            info_log("接口请求参数>>>>>>>>>>{}".format(data))
        res = requests.post(url=url, data=data, headers=headers)
        info_log("接口返回参数>>>>>>>>>>{}".format(res.json()))
        return res.json()


request = BaseRequest()
