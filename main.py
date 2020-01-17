# coding=utf-8
import os
import tkinter
from time import sleep
from tkinter import messagebox as mb
from tkinter import filedialog
from Spannedfile.spannedfile import mainA
from UploadFile.uploadfile import mainB
from config.config_main import Config

# 初始化配置文件方法
path1 = os.getcwd()
path2 = path1 + r'\config\data.ini'
config = Config(path2)

# 创建窗体
top = tkinter.Tk()
top.title("用例工具")
# 设置界面大小，和界面打开位置
top.geometry("600x400+600+300")
top.resizable(0, 0)
# top.configure(bg="blue")

# 创建一个图片管理类
photo = tkinter.PhotoImage(file="logo_jr.png")  # file：t图片路径
imgLabel = tkinter.Label(top, image=photo)  # 把图片整合到标签类中
imgLabel.place(x=220, y=10)  # 自动对齐


def spanned_file():
    def spanned_file_logic():
        value1 = filename.get()
        value1 = value1.replace("/", "\\")
        print(value1, type(value1))
        value2 = test_id.get()
        value3 = need_id.get()
        value4 = casedescription.get()
        value5 = casenature.get()
        value6 = stepid.get()
        value7 = resultid.get()
        value8 = module.get()
        value9 = stepname.get()
        value10 = filename1.get()
        value10 = value10.replace("/", "\\")

        def change_schedule(now_schedule, all_schedule):
            canvas.coords(fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 100, 25))
            window_spanned_file.update()
            x.set(str(round(now_schedule / all_schedule * 100, 2)) + '%')
            if round(now_schedule / all_schedule * 100, 2) == 100.00:
                x.set("完成")

        canvas = tkinter.Canvas(window_spanned_file, width=400, height=30, bg="white")
        canvas.grid(row=0, column=0)
        x = tkinter.StringVar()
        # 进度条以及完成程度
        # out_rec = canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
        fill_rec = canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="green")

        tkinter.Label(window_spanned_file, textvariable=x).grid(row=0, column=1)

        '''
        使用时直接调用函数change_schedule(now_schedule,all_schedule)
        下面就模拟一下....
        '''

        for i in range(60):
            sleep(0.05)
            change_schedule(i, 99)

        try:
            mainA(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10)
            config.configwrite("test_id", value2)
            config.configwrite("need_id", value3)
            config.configwrite("casedescription", value4)
            config.configwrite("casenature", value5)
            config.configwrite("stepid", value6)
            config.configwrite("resultid", value7)
            config.configwrite("module", value8)
            config.configwrite("stepname", value9)
            config.configwritesave()

            for i in range(61, 100):
                sleep(0.05)
                change_schedule(i, 99)

            mb.showinfo('提示', '生成文档成功!')
        except:
            mb.showerror("错误", "程序出错，请联系管理员！")
        window_spanned_file.destroy()

    def file_path_tool():
        path_ = filedialog.askopenfilename(title='选择Excel文件', filetypes=[('Excel', '*.xlsx'), ('Wps', 'xls')],
                                           initialdir=r'C:/')
        filename.set(path_)

    def file_path_tool1():
        path_ = filedialog.askdirectory(initialdir=r'C:/')
        filename1.set(path_)

    # 定义长在窗口上的窗口
    window_spanned_file = tkinter.Toplevel(top)
    window_spanned_file.geometry('600x600')
    window_spanned_file.title('生成文档')
    window_spanned_file.resizable(0, 0)

    filename = tkinter.StringVar()
    filename1 = tkinter.StringVar()
    test_id = tkinter.StringVar()
    need_id = tkinter.StringVar()
    casedescription = tkinter.StringVar()
    casenature = tkinter.StringVar()
    stepid = tkinter.StringVar()
    resultid = tkinter.StringVar()
    module = tkinter.StringVar()
    stepname = tkinter.StringVar()

    filename.set("选择案例路径")
    tkinter.Label(window_spanned_file, text='案例路径: ').place(x=10, y=10)
    tkinter.Entry(window_spanned_file, width=50, textvariable=filename).place(x=90, y=10)
    btn_file_path_tool = tkinter.Button(window_spanned_file, text='..', command=file_path_tool)
    btn_file_path_tool.place(x=500, y=6)

    test_id.set(config.configread("test_id"))
    tkinter.Label(window_spanned_file, text='测试id列: ').place(x=10, y=50)
    entry_test_id = tkinter.Entry(window_spanned_file, textvariable=test_id)
    entry_test_id.place(x=90, y=50)

    need_id.set(config.configread("need_id"))
    tkinter.Label(window_spanned_file, text='需求id列: ').place(x=10, y=90)
    entry_need_id = tkinter.Entry(window_spanned_file, textvariable=need_id)
    entry_need_id.place(x=90, y=90)

    casedescription.set(config.configread("casedescription"))
    tkinter.Label(window_spanned_file, text='案例描述列: ').place(x=10, y=130)
    entry_casedescription = tkinter.Entry(window_spanned_file, textvariable=casedescription)
    entry_casedescription.place(x=90, y=130)

    casenature.set(config.configread("casenature"))
    tkinter.Label(window_spanned_file, text='案例性质列: ').place(x=10, y=170)
    entry_casenature = tkinter.Entry(window_spanned_file, textvariable=casenature)
    entry_casenature.place(x=90, y=170)

    stepid.set(config.configread("stepid"))
    tkinter.Label(window_spanned_file, text='案例步骤列: ').place(x=10, y=210)
    entry_stepid = tkinter.Entry(window_spanned_file, textvariable=stepid)
    entry_stepid.place(x=90, y=210)

    resultid.set(config.configread("resultid"))
    tkinter.Label(window_spanned_file, text='预期结果列: ').place(x=10, y=250)
    entry_resultid = tkinter.Entry(window_spanned_file, textvariable=resultid)
    entry_resultid.place(x=90, y=250)

    module.set(config.configread("module"))
    tkinter.Label(window_spanned_file, text='案例模块列: ').place(x=10, y=290)
    entry_module = tkinter.Entry(window_spanned_file, textvariable=module)
    entry_module.place(x=90, y=290)

    stepname.set(config.configread("stepname"))
    tkinter.Label(window_spanned_file, text='步骤名列: ').place(x=10, y=330)
    entry_stepname = tkinter.Entry(window_spanned_file, textvariable=stepname)
    entry_stepname.place(x=90, y=330)

    filename1.set("选择生成文档路径")
    tkinter.Label(window_spanned_file, text='文档路径: ').place(x=10, y=370)
    tkinter.Entry(window_spanned_file, width=50, textvariable=filename1).place(x=90, y=370)
    btn_file_path_tool = tkinter.Button(window_spanned_file, text='..', command=file_path_tool1)
    btn_file_path_tool.place(x=500, y=366)
    str_ = '''
*说明*： 
1、以上空白处分别需要填写案例id、需求id、案例描述、案例性质、案例步骤、预期结果、案例模块、
步骤名称在用例表中的列名称
2、可以填写“A,B,C...”或者“a,b,c...”
3、如果案例中没有该部分内容，可填写“无”
'''
    tkinter.Label(window_spanned_file, text=str_, fg="red", justify="left").place(x=10, y=410)

    # 下面的 sign_to_Hongwei_Website
    btn_comfirm_sign_up = tkinter.Button(window_spanned_file, text='生成', command=spanned_file_logic)
    btn_comfirm_sign_up.place(x=500, y=550)


def upioad_file():
    def upioad_file_logic():
        value1 = filename.get()
        value1 = str(value1).replace("/", "\\")
        print(value1, type(value1))
        value2 = test_id.get()
        value3 = need_id.get()
        value4 = casedescription.get()
        value5 = casenature.get()
        value6 = stepid.get()
        value7 = resultid.get()

        try:
            mainB(value1, value2, value3, value4, value5, value6, value7)
            config.configwrite("url", value2)
            config.configwrite("username", value3)
            config.configwrite("password", value4)
            config.configwrite("domain", value5)
            config.configwrite("project", value6)
            config.configwrite("testSetID", value7)
            config.configwritesave()
            mb.showinfo('提示', '上传附件成功!')
        except:
            mb.showerror("错误", "程序出错，请联系管理员！")

        window_upioad_file.destroy()

    def file_path_tool():
        path_ = filedialog.askdirectory(initialdir=r'C:/')
        filename.set(path_)

    # 定义长在窗口上的窗口
    window_upioad_file = tkinter.Toplevel(top)
    window_upioad_file.geometry('600x600')
    window_upioad_file.title('上传附件')
    window_upioad_file.resizable(0, 0)

    filename = tkinter.StringVar()
    test_id = tkinter.StringVar()
    need_id = tkinter.StringVar()
    casedescription = tkinter.StringVar()
    casenature = tkinter.StringVar()
    stepid = tkinter.StringVar()
    resultid = tkinter.StringVar()

    filename.set('选择附件位置')
    tkinter.Label(window_upioad_file, text='附件位置: ').place(x=10, y=10)
    tkinter.Entry(window_upioad_file, width=50, textvariable=filename).place(x=90, y=10)
    btn_file_path_tool = tkinter.Button(window_upioad_file, text='..', command=file_path_tool)
    btn_file_path_tool.place(x=500, y=6)

    test_id.set(config.configread("url"))
    tkinter.Label(window_upioad_file, text='url: ').place(x=10, y=50)
    entry_test_id = tkinter.Entry(window_upioad_file, width=50, textvariable=test_id)
    entry_test_id.place(x=90, y=50)

    need_id.set(config.configread("username"))
    tkinter.Label(window_upioad_file, text='username: ').place(x=10, y=90)
    entry_need_id = tkinter.Entry(window_upioad_file, textvariable=need_id)
    entry_need_id.place(x=90, y=90)

    casedescription.set(config.configread("password"))
    tkinter.Label(window_upioad_file, text='password: ').place(x=10, y=130)
    entry_casedescription = tkinter.Entry(window_upioad_file, textvariable=casedescription, show="*")
    entry_casedescription.place(x=90, y=130)

    casenature.set(config.configread("domain"))
    tkinter.Label(window_upioad_file, text='domain: ').place(x=10, y=170)
    entry_casenature = tkinter.Entry(window_upioad_file, textvariable=casenature)
    entry_casenature.place(x=90, y=170)

    stepid.set(config.configread("project"))
    tkinter.Label(window_upioad_file, text='project: ').place(x=10, y=210)
    entry_stepid = tkinter.Entry(window_upioad_file, textvariable=stepid)
    entry_stepid.place(x=90, y=210)

    resultid.set(config.configread("testSetID"))
    tkinter.Label(window_upioad_file, text='testSetID: ').place(x=10, y=250)
    entry_resultid = tkinter.Entry(window_upioad_file, textvariable=resultid)
    entry_resultid.place(x=90, y=250)

    str_ = '''
*说明*： 
1、url处需要填写QC的服务地址，例如：http://127.0.0.1:8080/qcbin
2、username处需要填写QC的登录账户名字
3、password处需要填写QC的登录账户密码
4、domain处需要填写QC的登录域
5、project处需要填写QC的登录项目
6、testSetID处需要填写QC的测试集id，进入qc找到要上传的测试集，点击详细信息，就能找到测试集id
'''

    tkinter.Label(window_upioad_file, text=str_, fg="red", justify="left").place(x=10, y=290)

    btn_comfirm_sign_up = tkinter.Button(window_upioad_file, text='开始上传', command=upioad_file_logic)
    btn_comfirm_sign_up.place(x=500, y=550)


def help_info():
    window_sign_up = tkinter.Toplevel(top)
    window_sign_up.geometry('600x400')
    window_sign_up.title('帮助')

    # 创建一个图片管理类
    photo = tkinter.PhotoImage(file="logo_jr.png")  # file：t图片路径
    imgLabel = tkinter.Label(window_sign_up, image=photo)  # 把图片整合到标签类中
    imgLabel.place(x=230, y=7)  # 自动对齐

    str1 = r'''
这个是帮助文档！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    
第一次使用上传附件功能需要安装插件TDConnect.exe

v0.0.1

author:quyao
'''
    tkinter.Label(window_sign_up, text=str1, justify="center").place(y=60, x=65)
    window_sign_up.mainloop()


btn_sign_up = tkinter.Button(top, width=10, height=2, text='生成文档', command=spanned_file)
btn_sign_up.place(x=130, y=150)

btn_sign_down = tkinter.Button(top, width=10, height=2, text='上传附件', command=upioad_file)
btn_sign_down.place(x=370, y=150)

btn_sign_down = tkinter.Button(top, text='帮助', command=help_info)
btn_sign_down.place(x=270, y=300)

# 进入死循环，监听界面所有操作
top.mainloop()
