import os
from time import strftime


class Reprot(object):
    def __init__(self):
        self.now = strftime("%Y-%m-%d %H:%M:%S")
        self.path = os.path.abspath('.')
        template_path = self.path + '/testReport/template.html'
        with open(template_path, encoding='utf-8') as file:
            self.template = file.read()

    def test_value(self, content, test_id, driver_id, modul_name, case_id, result, case_detaile, test_time, error_info):
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
        str_html = '''
<tr height="40">
<td width="7%">$test_id</td>
<td width="10%">$driver_id</td>
<td width="9%">$modul_name</td>
<td width="7%">$case_id</td>
<td width="20%">$case_detaile</td>
<td width="7%" bgcolor="$color">$result</td>
<td width="15%">$test_time</td>
<td width="15%">$error_info</td>
</tr>
'''
        if result == '成功':
            color = 'green'
        elif result == '失败':
            color = 'red'
        elif result == '错误':
            color = 'yellow'

        str_html = str_html.replace('$test_id', str(test_id))
        str_html = str_html.replace('$driver_id', driver_id)
        str_html = str_html.replace('$modul_name', str(modul_name))
        str_html = str_html.replace('$case_id', str(case_id))
        str_html = str_html.replace('$result', str(result))
        str_html = str_html.replace('$color', color)
        str_html = str_html.replace('$case_detaile', str(case_detaile))
        str_html = str_html.replace('$test_time', str(test_time))
        str_html = str_html.replace('$error_info', error_info)
        content += str_html
        return content

    def table_write(self, test_version, pass_count, fail_count, error_count, content):
        '''
        :param test_version:被测版本
        :param pass_count:成功案例数
        :param fail_count:失败案例数
        :param error_count:报错案例数
        :param content:每一个测试结果信息
        :return:null
        '''
        now = strftime("%Y-%m-%d-%H-%M-%S")
        template = self.template
        template = template.replace('$test-date', str(now))
        template = template.replace('$test-version', test_version)
        template = template.replace('$pass-count', str(pass_count))
        template = template.replace('$fail-count', str(fail_count))
        template = template.replace('$error-count', str(error_count))
        template = template.replace('$last-time', str(now))
        template = template.replace('$test-result', content)
        template_path_save = self.path + '/testReport/'
        filename = now + '.html'
        with open(template_path_save + filename, mode='w+', encoding='utf-8') as file:
            file.write(template)
