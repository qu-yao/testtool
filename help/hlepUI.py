import os
import tkinter


def help_info(top, path1, config):
    window_sign_up = tkinter.Toplevel(top)
    window_sign_up.geometry('600x600')
    window_sign_up.resizable(0, 0)
    window_sign_up.title('帮助')

    # 创建一个图片管理类
    photo = tkinter.PhotoImage(file="./config/logo_jr.png")  # file：t图片路径
    imgLabel = tkinter.Label(window_sign_up, image=photo)  # 把图片整合到标签类中
    imgLabel.place(x=210, y=7)  # 自动对齐

    str1 = r'''
本工具可实现通过用例表生成单个的执行记录单，可将执行记录单批量上传至qc平台。

第一次使用上传附件功能需要安装插件TDConnect.exe


[2020-05-09]:修改了上传附件只上传未通过的案例！
[2020-05-11]:修复qc所有步骤内容写在一个步骤的情况！
[2020-05-11]:新增生成附件时，检查本地是否已经存在该测试集文件夹，如果存在则重命名！
[2020-05-14]:新增上传和生成文档数量提示！
[2020-05-16]:修改当用例无步骤时程序出错，闪退！
[2020-05-16]:新增导出案例功能，增加按QC路径生成附件，增加选项控制如果已经有附件是否上传！
'''

    def intallTD():
        path3 = path1 + r"\TDConnect.exe"
        os.system(path3)

    tkinter.Label(window_sign_up, text=str1, justify="center").place(y=60, x=50)

    version = config.configread('version')+"——"+"@QuYao"
    str_ = '版本号：' + version
    tkinter.Label(window_sign_up, text=str_).place(x=210, y=510)

    btn_help = tkinter.Button(window_sign_up, text='安装插件', command=intallTD)
    btn_help.place(x=260, y=550)

    window_sign_up.mainloop()
