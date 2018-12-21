# -*- coding:utf-8 -*-
# @Time   : 2018-11-06 15:26
# @Author : YangWeiMin

import json
import requests
import unittest
from common.logger import Log
from common.CommonMethod import CommonMethod
from common.pgsql_connect import PgsqlUtil
from case.test_login import Login
from common.assert_equal import AssertEqual
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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


    # def test_GetCarInventory(self):
    #     """
    #     作用:获取车辆商品库存信息
    #     :return:
    #     """
    #
    #     url = CommonMethod().get_url()
    #     headers = {
    #                 #将参数化的cookie和token进行拼接
    #                 "Cookie": "login_tenant=" +self.tenant_id + ";" + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #
    #     }
    #
    #     request = requests.post(url,headers=headers,verify=False)
    #     self.log.info("获取车辆库存的结果：%s"%request.content)
    #     self.assertEqual(request.status_code,200)
    #     result = request.json()
    #     data = result['datas']
    #     get_result = data[0]['change_num']
    #     print(get_result)
    #
    #
    #
    # @unittest.skip('test_huoQuTiHuoOrHuiKuShenQingParam')
    # def test_huoQuTiHuoOrHuiKuShenQingParam(self):
    #     """
    #     名称:提货申请页面初始化、回库申请页面初始化、获取是否有未审核的提货和回库申请接口
    #     :return:
    #     """
    #
    #     url = "http://" + Login.client_host + "/app/esss/carsale/client/v2/huoQuTiHuoOrHuiKuShenQingParam.action"
    #     headers = {
    #                  #将参数化的cookie和token进行拼接
    #                 "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #     request = requests.post(url,headers=headers,verify=False)
    #     self.log.info("提货申请页面初始化、回库申请页面初始化结果：%s"%request.content)
    #     self.assertEqual(request.status_code,200)
    #
    #
    #
    #
    # @unittest.skip('test_huoQuTiHuoShenQingRecords')
    # def test_huoQuTiHuoShenQingRecords(self):
    #     """
    #     名称:获取提货申请记录
    #     :return:
    #     """
    #     url = "http://" + Login.client_host + "/app/esss/carsale/client/v2/huoQuTiHuoOrHuiKuShenQingParam.action"
    #     headers = {
    #                  #将参数化的cookie和token进行拼接
    #                 "Cookie": "login_tenant=" + Login.tenant_id + "; "+ self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #     request = requests.post(url,headers=headers,verify=False)
    #     self.log.info("获取提货申请记录结果：%s"%request.content)
    #     self.assertEqual(request.status_code,200)
    #
    #
    #
    # @unittest.skip('test_GetReceiviableHistory')
    # def test_GetReceiviableHistory(self):
    #     """
    #     名称:根据业务单据id查看收款明细
    #     :return:
    #     """
    #     url = "http://" + Login.client_host + "/app/esss/carsale/client/v3/listReceiviableHistory.do"
    #
    #     headers = {
    #         # 将参数化的cookie和token进行拼接
    #         "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #     data = {
    #         "billId" : "8384303983525808210",
    #         "billType" : "4"   #1、期初余额 2、销售发货单 3、销售退货单 4、车销单
    #     }
    #
    #     request = requests.post(url,headers=headers,data=data,verify=False)
    #     self.log.info("根据单据id查看收款明细结果:%s"%request.content)
    #     self.assertEqual(request.status_code,200)
    #
    # @unittest.skip('test_getCanUseBalanceByCmId')
    # def test_getCanUseBalanceByCmId(self):
    #     """
    #     名称:根据客户id获取客户剩余余额
    #     :return:
    #     """
    #
    #     url = "http://" + Login.client_host + "/app/esss/client/api/getCmAmount.do?cmId=6838606579422169335"
    #
    #     headers = {
    #         # 将参数化的cookie和token进行拼接
    #         "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #
    #     request = requests.get(url,headers=headers,verify=False)
    #     self.log.info("根据客户id获取客户余额结果:%s"%request.content)
    #     self.assertEqual(request.status_code,200)
    #
    # @unittest.skip('test_getBookOrderById')
    # def test_getBookOrderById(self):
    #     """
    #     名称:根据id获取订货单详情
    #     :return:
    #     """
    #     url = "http://" + Login.client_host + "/app/esss/book_order/api/getBookOrderById.do"
    #
    #     headers = {
    #         "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #     data = {
    #         "id" : "6303023093965999684"
    #     }
    #
    #     request = requests.post(url,headers=headers,data=data,verify=False)
    #     self.log.info("根据id获取单据详情结果:" + request.content )
    #     self.assertEqual(request.status_code,200)
    #
    # @unittest.skip('test_getBookOrderList')
    # def test_getBookOrderList(self):
    #     """
    #     名称:根据客户获取还货主题及相关的订货单信息
    #     :return:
    #     """
    #     url = "http://" + Login.client_host + "/app/esss/book_order/api/getBookOrderList.do"
    #     headers = {
    #         "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #     request = requests.get(url,headers=headers,verify=False)
    #     self.log.info("根据客户获取还货主题及相关的订货单信息结果:" + request.content)
    #     self.assertEqual(request.status_code,200)
    #
    #
    # @unittest.skip('test_saveEsssOrder')
    # def test_saveEsssOrder(self):
    #     """
    #     名称:保存车销单记录
    #     :return:
    #     """
    #     url = 'http://' + Login.client_host + '/app/esss/carsale/client/v2/baoCunXiaoShouDan.action'
    #
    #     headers = {
    #         "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #     data = {
    #         'data.account':'10',
    #         'data.backProducts':'',
    #         'data.changeProducts':'',
    #         'data.cm_id':'8474128111592925628',
    #         'data.deal_amount':'20.00',
    #         'data.debt_amount':'0.00',
    #         'data.discount_amount':'0.00',
    #         'data.emp_id':'5615317598638557453',
    #         'data.isGoOnCreditLow':'0',
    #         'data.locationStr':'31.983281,118.730387|_1_江苏省南京市建邺区嘉陵江东街|_|_|_|_|_|_|_0|_0|',
    #         'data.location_type':'1',
    #         'data.receive_amount':'20.00',
    #         'data.remark':'',
    #         'data.returnProducts':'',
    #         'data.saleProducts':'[{"sale_num":"2.000","id":"5939131273017815124","sale_price":"10.000","sale_input_unit":"6019946915290783275","sale_amount":"20.000000","sale_type":"10","write_off_sale_num":"-2.000"}]',
    #         "data.token":'',
    #         'data.total_amount':'20.00',
    #         'data.use_balance_amount':'',
    #         'data.use_balance_time_str':'',
    #         'data.visit_implement_id':''
    #     }
    #
    #     request = requests.post(url,headers=headers,data=data,verify=False)
    #     self.log.info("保存车销单成功:" + request.content)
    #     self.assertEqual(request.status_code,200)
    #     result = json.loads(request.content)['id']
    #     return result
    #
    #
    # @unittest.skip('test_getEsssOrderRecord')
    # def test_getEsssOrderRecord(self):
    #     """
    #     说明:获取车销单列表的最新单据
    #     :return:
    #     """
    #     url = 'http://' + Login.client_host + '/app/esss/carsale/client/v2/huoQuXiaoShouDanRecords.action'
    #     headers = {
    #         "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #     data = {
    #         "conditions.curPage":'1',
    #         "conditions.isQueryMyAndSubData":'1'
    #     }
    #     request = requests.post(url,headers=headers,data=data,verify=False)
    #     self.log.info("车销单列表最新单据获取成功" + request.content)
    #     self.assertEqual(request.status_code,200)
    #
    #
    #
    # @unittest.skip('test_deleteEsssOrder')
    # def test_deleteEsssOrder(self):
    #     """
    #     名称:作废车销单
    #     :return:
    #     """
    #     data_id = self.test_saveEsssOrder()
    #
    #     url = "http://" + Login.client_host + '/app/esss/carsale/client/v2/zuoFeiXiaoShouDan.action'
    #
    #     headers = {
    #         "Cookie": "login_tenant=" + Login.tenant_id + "; " + self.cookie + ";" + self.token + "; sourceType=CLIENT; "
    #     }
    #
    #     data = {
    #         'data.id':data_id,
    #         'data.isCheckReAndChStock':'1',
    #         'data.modifyTime':'',
    #         'data.token':''
    #     }
    #
    #     request = requests.post(url,headers=headers,data=data,verify=False)
    #     self.log.info("作废车销单据成功!" + request.content)
    #     self.assertEqual(request.status_code,200)
    #     result = request.json()
    #     print(result)






if __name__ == '__main__':
    unittest.main()



