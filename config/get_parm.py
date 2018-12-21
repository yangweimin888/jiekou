# -*- coding:utf-8 -*-
# @Time   : 2018-12-20 10:25
# @Author : YangWeiMin
import os
import yaml


class GetParm(object):
    """获取参数"""


    def open_parm_file(self, path):
        """公共方法，读取参数文件"""
        self.parm_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
        with open(self.parm_path, 'r', encoding='utf-8') as f:
            data = yaml.load(f)
            return data


    def get_api_parm(self):
        """获取接口数据"""
        api = self.open_parm_file('api_parm.yaml')
        return api


    def get_database_parm(self):
        database_parm = self.open_parm_file('database_parm.yaml')
        return database_parm


    def get_tenant_parm(self):
        tenant_parm = self.open_parm_file('tenant_parm.yaml')
        return tenant_parm

