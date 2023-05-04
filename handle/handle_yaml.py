"""
读取api_data中yaml 文件
"""

import yaml
import os

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class HandleYaml:

    def __init__(self, file_name):
        self.yaml_path = base_path + "/api_data/{}".format(file_name)

    def load_yaml(self):
        file = open(self.yaml_path, 'r', encoding='utf-8')
        file_data = file.read()
        yaml_result = yaml.load(file_data, Loader=yaml.FullLoader)
        return yaml_result

    def get_data(self, api_case, params):
        """

        :param api_case: 传入接口测试的某个case
        :param params: 传入接口测试的某个字段
        :return: 对应字段值
        """
        data = self.load_yaml()[api_case][params]
        return data
