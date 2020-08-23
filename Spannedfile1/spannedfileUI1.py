import tkinter
from time import sleep
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog
from Spannedfile1.spannedfile1 import mainB


def spanned_file1(top, config):
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
        value8 = status.get()
        value9 = casepath.get()

        def change_schedule(now_schedule, all_schedule):
            canvas.coords(fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 400, 25))
            window_upioad_file.update()
            x.set(str(round(now_schedule / all_schedule * 100, 2)) + '%')
            if round(now_schedule / all_schedule * 100, 2) == 100.00:
                x.set("完成")

        canvas = tkinter.Canvas(window_upioad_file, width=400, height=30, bg="white")
        canvas.place(x=10, y=550)
        x = tkinter.StringVar()
        # 进度条以及完成程度
        # out_rec = canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
        fill_rec = canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="green")

        tkinter.Label(window_upioad_file, textvariable=x).place(x=420, y=560)

        '''
        使用时直接调用函数change_schedule(now_schedule,all_schedule)
        下面就模拟一下....
        '''

        for i in range(60):
            sleep(0.05)
            change_schedule(i, 99)

        if value1 == '选择附件位置':
            mb.showerror("错误", "未选择附件位置！")
        else:
            try:
                massge = mainB(value1, value2, value3, value4, value5, value6, value7, value8, value9)
                config.configwrite("filepath", value1)
                config.configwrite("url", value2)
                config.configwrite("username", value3)
                config.configwrite("password", value4)
                config.configwrite("domain", value5)
                config.configwrite("project", value6)
                config.configwrite("testSetID", value7)
                config.configwrite("status", value8)
                config.configwrite("casepath", value9)
                config.configwritesave()

                for i in range(61, 100):
                    sleep(0.05)
                    change_schedule(i, 99)

                mb.showinfo('提示', massge)
            except:
                mb.showerror("错误", "程序出错，请联系管理员！")

        window_upioad_file.destroy()

    def file_path_tool():
        path_ = filedialog.askdirectory(initialdir=r'C:/')
        filename.set(path_)

    # 定义长在窗口上的窗口
    window_upioad_file = tkinter.Toplevel(top)
    window_upioad_file.geometry('600x600')
    window_upioad_file.title('生成文档')
    window_upioad_file.resizable(0, 0)

    filename = tkinter.StringVar()
    test_id = tkinter.StringVar()
    need_id = tkinter.StringVar()
    casedescription = tkinter.StringVar()
    casenature = tkinter.StringVar()
    stepid = tkinter.StringVar()
    resultid = tkinter.StringVar()
    status = tkinter.StringVar()
    casepath = tkinter.StringVar()

    if config.configread("filepath") == '':
        filename.set('选择生成文档路径')
    else:
        filename.set(config.configread("filepath"))
    tkinter.Label(window_upioad_file, text='文档路径: ').place(x=10, y=10)
    tkinter.Entry(window_upioad_file, width=50, textvariable=filename).place(x=90, y=10)
    btn_file_path_tool = tkinter.Button(window_upioad_file, text='..', command=file_path_tool)
    btn_file_path_tool.place(x=500, y=6)

    test_id.set(config.configread("url"))
    tkinter.Label(window_upioad_file, text='Url: ').place(x=10, y=50)
    entry_test_id = tkinter.Entry(window_upioad_file, width=50, textvariable=test_id)
    entry_test_id.place(x=90, y=50)

    need_id.set(config.configread("username"))
    tkinter.Label(window_upioad_file, text='Username: ').place(x=10, y=90)
    entry_need_id = tkinter.Entry(window_upioad_file, textvariable=need_id)
    entry_need_id.place(x=90, y=90)

    casedescription.set(config.configread("password"))
    tkinter.Label(window_upioad_file, text='Password: ').place(x=10, y=130)
    entry_casedescription = tkinter.Entry(window_upioad_file, textvariable=casedescription, show="*")
    entry_casedescription.place(x=90, y=130)

    casenature.set(config.configread("domain"))
    tkinter.Label(window_upioad_file, text='Domain: ').place(x=10, y=170)
    entry_casenature = tkinter.Entry(window_upioad_file, textvariable=casenature)
    entry_casenature.place(x=90, y=170)

    stepid.set(config.configread("project"))
    tkinter.Label(window_upioad_file, text='Project: ').place(x=10, y=210)
    entry_stepid = tkinter.Entry(window_upioad_file, textvariable=stepid)
    entry_stepid.place(x=90, y=210)

    resultid.set(config.configread("testSetID"))
    tkinter.Label(window_upioad_file, text='TestSetID: ').place(x=10, y=250)
    entry_resultid = tkinter.Entry(window_upioad_file, textvariable=resultid)
    entry_resultid.place(x=90, y=250)

    casepath.set(config.configread("casepath"))
    tkinter.Label(window_upioad_file, text='CasePath: ').place(x=10, y=290)
    entry_casepath = tkinter.Entry(window_upioad_file, width=50, textvariable=casepath)
    entry_casepath.place(x=90, y=290)

    indexnum = ["Blocked", "Failed", "N/A", "No Run", "Not Completed", "Passed"].index(config.configread("status"))
    tkinter.Label(window_upioad_file, text="status：").place(x=10, y=330)
    de = ttk.Combobox(window_upioad_file, textvariable=status, width=12, height=15)
    de.bind("<<ComboboxSelected>>")
    de["value"] = ("Blocked", "Failed", "N/A", "No Run", "Not Completed", "Passed")
    de.current(indexnum)
    de.place(x=90, y=330)

    str_ = '''
    *说明*： 
    1、url处需要填写QC的服务地址，例如：http://127.0.0.1:8080/qcbin
    2、username处需要填写QC的登录账户名字
    3、password处需要填写QC的登录账户密码
    4、domain处需要填写QC的登录域
    5、project处需要填写QC的登录项目
    6、testSetID处需要填写QC的测试集id，进入qc找到要上传的测试集，点击详细信息，就能找到测试集id
    7、CasePath处需要填写QC的测试路径（当testSetID不为空，优先选择testSetID）
    7、生成多个测试集，中间用+号隔开例如：1234+5678+8520
    8、status选择导出案例的状态
    '''

    tkinter.Label(window_upioad_file, text=str_, fg="red", justify="left").place(x=10, y=370)

    btn_comfirm_sign_up = tkinter.Button(window_upioad_file, text='开始生成', command=upioad_file_logic)
    btn_comfirm_sign_up.place(x=500, y=550)
