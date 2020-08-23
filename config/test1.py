import config.configfile as configfile

def mainA():
    # 引用全局变量
    name = configfile.get_name()
    print(name)
    # 修改全局变量
    configfile.set_name('new_name')
    # 查看修改后的全局变量
    print(configfile.get_name())
