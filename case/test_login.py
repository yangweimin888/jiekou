# -*- coding:utf-8 -*-
# @Time   : 2018-11-06 15:26
# @Author : YangWeiMin

import requests
from common.logger import Log
from common.CommonMethod import CommonMethod
from config.get_parm import GetParm
from common.assert_equal import AssertEqual
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Login(object):


    def __init__(self):
        self.log = Log()
        self.tenant_parm = GetParm().get_tenant_parm()
        self.host = GetParm().get_tenant_parm()['host']['test_233']


    def test_client_login(self):
        """
        作用：模拟登录获取token和session信息
        :return: token、cookie
        """

        url = CommonMethod().get_url('clientLogin')
        headers = CommonMethod().login_headers()
        data = CommonMethod().login_request_data()
        request = requests.post(url, headers=headers, data=data, verify=False)
        AssertEqual().login_assert_equal(request)
        Session = request.cookies["WQSESSIONID"]
        Token = request.cookies["x-token"]
        cookie = "WQSESSIONID=" + Session
        token = "x-token=" + Token
        return cookie, token
