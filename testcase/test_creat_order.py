from base.base_request import request
import unittest
import json
from handle.handle_yaml import HandleYaml
from parameterized import parameterized
from handle.handle_log import log_method,log_method_call,log_class_methods

@log_class_methods
class TestCreatOrder(unittest.TestCase):
    url = "https://devapi.linkr.bio/store/pub/order/create"

    # 接口请求参数
    request_payload = {
        "storeId": "LRGzQN8B",
        "paymentChannel": "paypal",
        "currencyType": "USD",
        "fromCurrency": "USD",
        "toCurrency": "USD",
        "countryCode": "US",
        "customerEmail": "xx@xx.xx",
        "customerName": "32",
        "message": "321",
        "customerRegionCode": "244",
        "customerPhone": "321 32133213",
        "address": {
            "address": "321321321321",
            "city": "",
            "state": "",
            "zipCode": ""
        },
        "addOns": []
    }


    def test_request_params_require(self):
        """
        测试storeid 必填项
        :return:
        """
        data = self.request_payload
        data.pop('storeId')
        # data = self.request_payload
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], "ERR_BAD_REQUEST")
    #
    handle_yaml = HandleYaml("creat_order.yaml").get_data('test_request_params', 'storeId')

    @parameterized.expand(handle_yaml)
    def test_request_params_storeid(self, dic):
        print(dic)
        # 测试storeid 传入类型
        print("期待结果>>>>>>>", dic['code'])
        data = self.request_payload
        data['storeId'] = dic['key']
        # data = self.request_payload
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], dic['code'])

    @log_method
    # 测试payment channel 必填项
    def test_request_payment_channel_require(self):
        data = self.request_payload
        data.pop('paymentChannel')
        # data = self.request_payload
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], "ERR_BAD_REQUEST")

    # 测试payment channel 请求参数类型场景
    handle_yaml = HandleYaml("creat_order.yaml").get_data('test_request_params', 'paymentChannel')

    @log_method
    @parameterized.expand(handle_yaml)
    def test_request_params_payment(self, dic):
        data = self.request_payload
        print("期待结果>>>>>>>", dic['code'])
        data['paymentChannel'] = dic['key']
        # data = self.request_payload
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], dic['code'])

    @log_method
    # 测试customerEmail 选填项
    def test_request_email_optional(self):
        data = self.request_payload
        data.pop('customerEmail')
        # data = self.request_payload
        res = request.post(url=self.url, data=json.dumps(data))
        self.assertEqual(res['code'], "ERR_BAD_REQUEST")
# 装饰器会使用类的对象，不能使用函数级，会根据class
# 装饰器以类的级别去进行
if __name__ == '__main__':
    unittest.main()