import re

strtest = '''<html><body>验证[押品价值评估-外部评估],当[本行认定币种
]选择[本行认定币种为空]时的异常业务处理是否符合需求<br/><br/>1.回显[评估界面]<br/>2.在[评估方式]选择[直接认定]<br/>3.在[本行认定价值（元）]输入[输入正确的本行认定价值]<br/>4.在[本行认定币种 ]选择[本行认定币种为空]</body></html>'''

TS_DESCRIPTION = strtest
str01 = TS_DESCRIPTION.replace('<html><body>', '')
str03 = str01.replace('</body></html>', '')
str02 = str03.replace('\n', '')
if '<br' in str02:
    print(str02)
    strlist = re.search(r'验证(.*?)<br', str02).group()
    strlist = strlist.replace('<br', '')
else:
    strlist = str02
casedescription = strlist
