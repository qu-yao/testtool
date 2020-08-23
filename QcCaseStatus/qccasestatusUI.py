import tkinter
from time import sleep
from tkinter import filedialog
from tkinter import messagebox as mb
from .qccasestatus import spanned_file, upioad_file


def qccasestatus(top, config):
    def spanned_file_logic():
        value2 = test_id.get()  # url
        value3 = need_id.get()  # username
        value4 = casedescription.get()  # password
        value5 = casenature.get()  # demo
        value6 = stepid.get()  # projiect
        value7 = casepath.get()  # setid
        value8 = filepath.get()  # 生成案例路径

        def change_schedule(now_schedule, all_schedule):
            canvas.coords(fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 400, 25))
            window_qccasestatus.update()
            x.set(str(round(now_schedule / all_schedule * 100, 2)) + '%')
            if round(now_schedule / all_schedule * 100, 2) == 100.00:
                x.set("完成")

        canvas = tkinter.Canvas(window_qccasestatus, width=400, height=30, bg="white")
        canvas.place(x=10, y=500)
        x = tkinter.StringVar()
        # 进度条以及完成程度
        # out_rec = canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
        fill_rec = canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="green")

        tkinter.Label(window_qccasestatus, textvariable=x).place(x=420, y=510)

        '''
        使用时直接调用函数change_schedule(now_schedule,all_schedule)
        下面就模拟一下....
        '''

        for i in range(60):
            sleep(0.05)
            change_schedule(i, 99)

        try:
            spanned_file(value2, value3, value4, value5, value6, value7, value8)
            config.configwrite("url", value2)
            config.configwrite("username", value3)
            config.configwrite("password", value4)
            config.configwrite("domain", value5)
            config.configwrite("project", value6)
            config.configwrite("casepath", value7)
            config.configwritesave()

            for i in range(61, 100):
                sleep(0.05)
                change_schedule(i, 99)

            mb.showinfo('提示', '生成文档成功!')
        except:
            mb.showerror("错误", "程序出错，请联系管理员！")

    def upioad_file_logic():
        value1 = filename.get()  # 上传文件位置
        value2 = test_id.get()  # url
        value3 = need_id.get()  # username
        value4 = casedescription.get()  # password
        value5 = casenature.get()  # demo
        value6 = stepid.get()  # projiect
        value7 = casepath.get()  # setid

        def change_schedule(now_schedule, all_schedule):
            canvas.coords(fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 400, 25))
            window_qccasestatus.update()
            x.set(str(round(now_schedule / all_schedule * 100, 2)) + '%')
            if round(now_schedule / all_schedule * 100, 2) == 100.00:
                x.set("完成")

        canvas = tkinter.Canvas(window_qccasestatus, width=400, height=30, bg="white")
        canvas.place(x=10, y=540)
        x = tkinter.StringVar()
        # 进度条以及完成程度
        # out_rec = canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
        fill_rec = canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="green")

        tkinter.Label(window_qccasestatus, textvariable=x).place(x=420, y=550)

        '''
        使用时直接调用函数change_schedule(now_schedule,all_schedule)
        下面就模拟一下....
        '''

        for i in range(60):
            sleep(0.05)
            change_schedule(i, 99)

        try:
            upioad_file(value2, value3, value4, value5, value6, value7, value1)
            config.configwrite("url", value2)
            config.configwrite("username", value3)
            config.configwrite("password", value4)
            config.configwrite("domain", value5)
            config.configwrite("project", value6)
            config.configwrite("casepath", value7)
            config.configwritesave()

            for i in range(61, 100):
                sleep(0.05)
                change_schedule(i, 99)

            mb.showinfo('提示', '长传文档成功!')
        except:
            mb.showerror("错误", "程序出错，请联系管理员！")

        window_qccasestatus.destroy()

    def file_path_tool1():
        path_ = filedialog.askdirectory(initialdir=r'C:/')
        filepath.set(path_)

    def file_path_tool():
        path_ = filedialog.askdirectory(initialdir=r'C:/')
        filename.set(path_)

    # 定义长在窗口上的窗口
    window_qccasestatus = tkinter.Toplevel(top)
    window_qccasestatus.geometry('600x600')
    window_qccasestatus.title('案例状态')
    window_qccasestatus.resizable(0, 0)

    filename = tkinter.StringVar()
    filepath = tkinter.StringVar()
    test_id = tkinter.StringVar()
    need_id = tkinter.StringVar()
    casedescription = tkinter.StringVar()
    casenature = tkinter.StringVar()
    stepid = tkinter.StringVar()
    casepath = tkinter.StringVar()

    filepath.set('选择生成案例状态文档路径')
    tkinter.Label(window_qccasestatus, text='文档路径: ').place(x=10, y=10)
    tkinter.Entry(window_qccasestatus, width=50, textvariable=filepath).place(x=90, y=10)
    btn_file_path_tool = tkinter.Button(window_qccasestatus, text='..', command=file_path_tool1)
    btn_file_path_tool.place(x=500, y=6)

    test_id.set(config.configread("url"))
    tkinter.Label(window_qccasestatus, text='Url: ').place(x=10, y=50)
    entry_test_id = tkinter.Entry(window_qccasestatus, width=50, textvariable=test_id)
    entry_test_id.place(x=90, y=50)

    need_id.set(config.configread("username"))
    tkinter.Label(window_qccasestatus, text='Username: ').place(x=10, y=90)
    entry_need_id = tkinter.Entry(window_qccasestatus, textvariable=need_id)
    entry_need_id.place(x=90, y=90)

    casedescription.set(config.configread("password"))
    tkinter.Label(window_qccasestatus, text='Password: ').place(x=10, y=130)
    entry_casedescription = tkinter.Entry(window_qccasestatus, textvariable=casedescription, show="*")
    entry_casedescription.place(x=90, y=130)

    casenature.set(config.configread("domain"))
    tkinter.Label(window_qccasestatus, text='Domain: ').place(x=10, y=170)
    entry_casenature = tkinter.Entry(window_qccasestatus, textvariable=casenature)
    entry_casenature.place(x=90, y=170)

    stepid.set(config.configread("project"))
    tkinter.Label(window_qccasestatus, text='Project: ').place(x=10, y=210)
    entry_stepid = tkinter.Entry(window_qccasestatus, textvariable=stepid)
    entry_stepid.place(x=90, y=210)

    casepath.set(config.configread("casepath"))
    tkinter.Label(window_qccasestatus, text='CasePath: ').place(x=10, y=250)
    entry_casepath = tkinter.Entry(window_qccasestatus, width=50, textvariable=casepath)
    entry_casepath.place(x=90, y=250)

    filename.set('选择上传案例状态文档路径')
    tkinter.Label(window_qccasestatus, text='文档路径: ').place(x=10, y=290)
    tkinter.Entry(window_qccasestatus, width=50, textvariable=filename).place(x=90, y=290)
    btn_file_path_tool = tkinter.Button(window_qccasestatus, text='..', command=file_path_tool)
    btn_file_path_tool.place(x=500, y=290)

    str_ = '''
    *说明*： 
    1、url处需要填写QC的服务地址，例如：http://127.0.0.1:8080/qcbin
    2、username处需要填写QC的登录账户名字
    3、password处需要填写QC的登录账户密码
    4、domain处需要填写QC的登录域
    5、project处需要填写QC的登录项目
    6、testSetID处需要填写QC的测试集id，进入qc找到要上传的测试集，点击详细信息，就能找到测试集id
    7、修改案例状态的步骤为先下载对应测试集的案例列表，然后在列表中修改案例状态，最后进行上传案例
         状态列表
    '''

    tkinter.Label(window_qccasestatus, text=str_, fg="red", justify="left").place(x=10, y=330)

    btn_comfirm_sign_up = tkinter.Button(window_qccasestatus, text='开始生成', command=spanned_file_logic)
    btn_comfirm_sign_up.place(x=500, y=500)

    btn_comfirm_sign_up = tkinter.Button(window_qccasestatus, text='开始上传', command=upioad_file_logic)
    btn_comfirm_sign_up.place(x=500, y=540)
