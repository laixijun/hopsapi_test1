# coding:utf-8
from utils import HTMLTestRunnerChinese
from utils import mail
import unittest
import time
import os

# 用例路径
case_path = os.path.join(os.getcwd(), "testcase")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    # html报告文件路径
    now = time.strftime('%Y-%m-%d_%H%M%S')
    report_name = 'testResult_' + now + '.html'
    # report_abspath = os.path.join(report_path, "result.html")
    report_abspath = os.path.join(report_path, report_name)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunnerChinese.HTMLTestRunner(stream=fp, title=u'自动化测试报告,测试结果如下：', description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()
    # 发送邮件
    mail.sendmail()
