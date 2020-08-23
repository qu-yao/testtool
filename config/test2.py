import config.configfile as configfile
from config import test1


test1.mainA()

# 查看修改后的全局变量
print(configfile.get_name())
