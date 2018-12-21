# -*- coding:utf-8 -*-
# @Time   : 2018-12-20 11:20
# @Author : YangWeiMin
from config.get_parm import GetParm
import time
import requests
import json


class CommonMethod(GetParm):
    """程序中用到的公共方法"""
    Api = GetParm().get_api_parm()
    host = GetParm().get_tenant_parm()['host']['test_233']
    tenant_id = GetParm().get_tenant_parm()['tenant_id']


    @staticmethod
    def time_stamp():
        """
        获取当前时间戳
        :return: 时间戳对象
        """
        timestamp = time.strftime('%Y%m%d%H%M%S')
        return timestamp

    @staticmethod
    def get_local_day():
        """格式化时间,精确到天"""
        local_day = time.strftime('%Y-%m-%d')
        return local_day

    @staticmethod
    def get_local_sec():
        """格式化时间,精确到秒"""
        local_sec = time.strftime('%Y-%m-%d %X')
        return local_sec

    @staticmethod
    def get_local_min():
        """格式化时间，精确到分钟"""
        local_min = time.strftime('%Y-%m-%d %H:%m')
        return local_min


    def get_url(self, api_name):
        """拼接url地址"""

        api = self.Api[api_name]
        url = 'http://' + self.host + api
        return url


    def request_post(self, data, api_name, cookie, token):
        """封装post请求"""
        url = self.get_url(api_name)
        headers = {
            "Cookie": "login_tenant=" + str(self.tenant_id) + ";" + cookie + ";" + token + "; sourceType=CLIENT; "
        }
        request = requests.post(url, data, headers=headers, verify=False)
        return request





    def login_headers(self):
        """客户端登录所使用headers"""
        headers = {
                "Host": self.host,
                "Content-Type": "application/x-www-form-urlencoded",
                "wq-lang": "zh_CN",
                "Connection": "keep-alive",
                "Accept": "*/*",
                "User-Agent": "waiqin_ios_5615317598638557453",
                "Accept-Language": "zh-Hans-CN;q=1",
                "Content-Length": "544",
                "Accept-Encoding": "gzip",
        }
        return headers


    def login_request_data(self):
        """客户端登录使用的请求参数"""
        password = self.get_tenant_parm()['client_password']
        tenant_code = self.get_tenant_parm()['Tenantcode']
        user_code = self.get_tenant_parm()['code']
        version_code = self.get_tenant_parm()['versioncode']
        data = {
            "info.appId": "waiqin365@zhangkong",
            "info.appVer": "1.2.20.0",
            "info.clientId": "gaeaclient-ioswaiqin-000001",
            "info.clientVer": "6.0.2",
            "info.datetime": "",
            "info.encec": "",
            "info.esn": "186c3a5176c6c24bcfce",
            "info.imsi": "46000bda3baed30c1448",
            "info.iosToken": "f189658c 66d1a974 861655ee d2032beb e37d3bf4 c019a518 f9a6d629 ec92569b",
            "info.language": "zh_CN",
            "info.md5": "",
            "info.os": "iOS  10.3.1",
            "info.password": password ,
            "info.phoneModel": "iPhone  10.3.1",
            "info.screenheight": "2208",
            "info.screenwidth": "1242",
            "info.tenantCode": tenant_code,
            "info.type": 1,
            "info.userCode": user_code,
            "info.versioncode": version_code
        }
        return data





