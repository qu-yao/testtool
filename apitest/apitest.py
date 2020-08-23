import sys
import time

sys.path.append('./')
from .common.excl_class import Excl_Read, Excl_indxout
from .common.report_class import Reprot
from .common.request_class import Request
from .testConfig.readconfig import ReadConfig

'''
采用unittest的框架，自动识别excl读取案例，进行自动化的执行接口案例输出报告
'''


def case_data(filepath):
    testid_list = []
    module_list = []
    url_list = []
    data_list = []
    RequestType_list = []
    description_list = []
    ExpectedResult_list = []
    indxout = Excl_indxout(filepath)
    indx_x = 1
    while indx_x < indxout:
        testid_list.append(Excl_Read(filepath, sheetname, indx_x, 0))  # 案例id
        module_list.append(Excl_Read(filepath, sheetname, indx_x, 1))  # 案例所属模块
        url_list.append(Excl_Read(filepath, sheetname, indx_x, 2))  # url
        data_list.append(Excl_Read(filepath, sheetname, indx_x, 3))  # data
        RequestType_list.append(Excl_Read(filepath, sheetname, indx_x, 4))  # 请求类型
        description_list.append(Excl_Read(filepath, sheetname, indx_x, 5))  # 案例描述
        ExpectedResult_list.append(Excl_Read(filepath, sheetname, indx_x, 6))  # 预期结果
        indx_x += 1
    return testid_list, module_list, url_list, data_list, RequestType_list, description_list, ExpectedResult_list


if __name__ == '__main__':
    reprot = Reprot()
    request = Request()
    readconfig = ReadConfig()
    filepath = readconfig.rc('filepath')
    sheetname = readconfig.rc('sheetname')
    testversion = readconfig.rc('testversion')
    content = ''
    passtime = 0
    fail = 0
    errortime = 0
    testid_list, module_list, url_list, data_list, RequestType_list, description_list, ExpectedResult_list = case_data(
        filepath, sheetname)
    for testid, module, url, data, RequestType, description, ExpectedResult in zip(
            testid_list, module_list, url_list, data_list, RequestType_list, description_list, ExpectedResult_list):
        befortime = int(time.time() * 1000)
        if RequestType == 'get':
            res = request.request_get(url=url, data=data)
        else:
            res = request.request_get(url=url, data=data)
        aftertime = int(time.time() * 1000)
        if ExpectedResult in res:
            result = '成功'
            passtime += 1
            error_info = 'null'
        else:
            fail += 1
            result = '失败'
            error_info = res
            '''
            :param content: 累计测试结果，如果当前是第一个传过来为空
            :param test_id: 报告id
            :param driver_id: 设备id或者地址
            :param modul_name: 模块名字
            :param case_id: 用例id
            :param result: 测试结果包含成功、失败、报错
            :param case_detaile: 用例描述
            :param test_time:测试时间
            :param error_info:报错信息
            :return:返回结果为累加当前结果后的字符串
            '''
        leadtime = aftertime - befortime
        idnum = ExpectedResult_list.index(ExpectedResult) + 1
        content = reprot.test_value(content, idnum, url, module, testid, result, description, leadtime, error_info)
        '''
        :param test_version:被测版本
        :param pass_count:成功案例数
        :param fail_count:失败案例数
        :param error_count:报错案例数
        :param content:每一个测试结果信息
        :return:null
        '''
    reprot.table_write(testversion, passtime, fail, errortime, content)
