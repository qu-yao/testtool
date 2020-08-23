import configparser
import os
import sys


class ReadConfig(object):
    def rc(self, key):
        cf = configparser.ConfigParser()

        # sys.path.append('../')
        path1 = os.getcwd()
        path2 = path1 + r'\testConfig\config.ini'
        cf.read(path2, encoding='UTF-8')

        # secs = cf.sections()  # 获取文件中所有的section
        # print(secs)
        #
        # options = cf.options("UserInfo")  # 获取某个section名为UserInfo所对应的键
        # print(options)
        #
        # items = cf.items("UserInfo")  # 获取section名为UserInfo所对应的全部键值对
        # print(items)

        data = cf.get('TestInfo', key)  # 获取[UserInfo]中Username对应的值
        # print(Username)
        # print(type(Username))
        return data
