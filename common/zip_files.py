# -*- coding:utf-8 -*-
# Author: YangWeiMin
# Time: 2019/1/14 22:06
# 工具: PyCharm
import zipfile
import os

class ZipMethod(object):
    """压缩文件的公共方法"""


    def __init__(self, file_path):
        self.file_path = file_path
        # self.log = Log()


    def zip_files(self, zip_name):
        """将路径下的所有文件压缩成zip包"""
        data = os.listdir(self.file_path)
        zip_file = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for file in data:
            print('%s正在压缩中......' % file)
            zip_file.write(file)
        zip_file.close()
        print('压缩完成')


    def zip_path(self, zip_name):
        """按照全路径压缩文件"""
        data = os.listdir(self.file_path)
        if len(data) == None or len(data) < 1:
            print('待压缩的文件目录：%s' % self.file_path + '里面不存在文件，不需要压缩')
        else:
            zip_file = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
            for path, dir_names, file_names in os.walk(self.file_path):
                for filename in file_names:
                    zip_file.write(os.path.join(self.file_path, filename))
            zip_file.close()


app = ZipMethod('E:\Code\python3\day01')
app.zip_path('esss.zip')
