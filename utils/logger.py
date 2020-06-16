# -*- coding:utf-8 -*-
import logging
import os
import time


class Log(object):
    """编写日志类，供其他模块调用"""
    def __init__(self, logger):
        # 拼接日志文件夹，如果不存在则自动创建
        report_path = str(os.path.dirname(__file__).split('utils')[0])
        log_path = os.path.join(report_path, 'report/logs')
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        # 设置日志文件名称格式及日志等级
        self.log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，将日志写入日志文件
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式
        self.formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        ch.setFormatter(self.formatter)
        fh.setFormatter(self.formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

