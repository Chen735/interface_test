from base.base_request import request
import unittest
import json
from handle.handle_yaml import HandleYaml
from parameterized import parameterized
from handle.handle_log import log_method, log_method_call, log_class_methods

"""

"""
@log_class_methods
class TestOrderCompute(unittest.TestCase):
    # 公共配置
    url = "https://devapi.linkr.bio/store/sell/user/order/info"
    # 请求参数
    request_payload = {
        "storeId": "LRGzQN8B",
        "toCurrency": "SGD",
        "paymentChannel": "stripe"
    }

    def testCase01_params_storeid_require(self):
        """校验storeid 必填项"""
        data = self.request_payload
        data.pop("storeId")
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], "ERR_BAD_REQUEST")

    yaml_data = HandleYaml("order_compute.yaml").get_data('test_request_params', 'storeId')

    @parameterized.expand(yaml_data)
    def test02_params_storeid_invalid(self, dic):
        data = self.request_payload
        data['storeId'] = dic['key']
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], dic['code'])

    def test_params_to_currency_require(self):
        """ 校验toCurrency 必填项"""
        data = self.request_payload
        data.pop("toCurrency")
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], "ERR_BAD_REQUEST")

    yaml_data = HandleYaml("order_compute.yaml").get_data('test_request_params', 'toCurrency')

    @parameterized.expand(yaml_data)
    def test_params_tocurrency_invalid(self, dic):
        """校验toCurrency 参数异常类型"""
        data = self.request_payload
        data['toCurrency'] = dic['key']
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], dic['code'])

    def test_params_paymentchannel(self):
        """校验paymentChannel 必填项"""
        data = self.request_payload
        data.pop("paymentChannel")
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], "ERR_BAD_REQUEST")

    yaml_data = HandleYaml("order_compute.yaml").get_data('test_request_params', 'paymentChannel')

    @parameterized.expand(yaml_data)
    def test_params_paymentchannel_invalid(self, dic):
        """校验paymentchannel 请求参数异常情况"""
        data = self.request_payload
        data['paymentChannel'] = dic['key']
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], dic['code'])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOrderCompute("test_params_paymentchannel_invalid"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
