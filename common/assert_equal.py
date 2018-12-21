# -*- coding:utf-8 -*-
# @Time   : 2018-12-12 10:01
# @Author : YangWeiMin

import unittest
from common.logger import Log
from common.pgsql_connect import PgsqlUtil
import json


class AssertEqual(unittest.TestCase):
    """断言方法"""
    log = Log()
    p = PgsqlUtil()

    def login_assert_equal(self, request):
        """登录断言"""
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['code'], '2')
            self.log.info('客户端登录成功')
        except Exception as e:
            self.log.error('客户端登录失败:%s' % e)


    def query_assert_equal(self, request, message):
        """
        查询断言
        :param request: 请求的对象
        :param message: 日志打印信息
        :return:
        """
        request_data = json.loads(request.text)
        print(request_data)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['code'], '1')
            self.log.info('查询%s成功' % message)
        except Exception as e:
            self.log.error('查询%s失败:%s' % (message, e))


    def add_assert_equal(self, request, message, bill_id):
        """
        新增断言
        :param request: 请求的对象
        :param message: 日志打印信息
        :param bill_id: 单据id
        :return:
        """
        request_data = json.loads(request.text)
        if request_data['response_data'] is None:
            self.log.error(request_data['message'])
        else:
            response = json.loads(request_data['response_data'])
            try:

                    self.assertEqual(str(response['id']), str(bill_id))
                    self.assertEqual(request.status_code, 200)
                    self.assertEqual(request_data['code'], '1')
                    self.log.info('新增%s成功' % message)
            except Exception as e:
                self.log.error('新增%s失败:%s' % (message, e))


    def verify_assert_equal(self, request, message):
        """
        审批断言
        :param request: 请求对象
        :param message: 日志打印信息
        :return:
        """
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '1')
            self.log.info('%s审批成功' % message)
        except Exception as e:
            self.log.error('%s审批失败:%s' % (message, e))
