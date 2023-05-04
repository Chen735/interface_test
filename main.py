import unittest
import time
from testcase.test_order_compute import TestOrderCompute
from BeautifulReport import BeautifulReport as bf

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestOrderCompute("test_params_paymentchannel_invalid"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    discover = unittest.defaultTestLoader.discover('./testcase', pattern='test_order_compute.py')  # 加载测试用例
    report_name = now + '-' + '_test_report.html'  # 报告名称
    run = bf(discover)
    run.report(filename=report_name,report_dir='./report/', description=U"酷狗音乐UI自动化功能回归测试")
