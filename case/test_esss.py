# -*- coding:utf-8 -*-
# @Time   : 2018-11-06 15:26
# @Author : YangWeiMin

import unittest
from common.logger import Log
from common.CommonMethod import CommonMethod
from common.pgsql_connect import PgsqlUtil
from case.test_login import Login
from common.assert_equal import AssertEqual

class Client_Esss_Sales(unittest.TestCase):
    log = Log()
    p = PgsqlUtil()
    cookie, token = Login().test_client_login()


    def test_01(self):
        """获取车辆库存信息"""
        data = {
            'carId': self.p.get_car_id('A10086')
        }
        request = CommonMethod().request_post(data, 'carStock', self.cookie, self.token)
        AssertEqual().query_assert_equal(request, '车辆库存')



if __name__ == '__main__':
    unittest.main()



