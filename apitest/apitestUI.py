import tkinter
from time import sleep
from tkinter import messagebox as mb
from tkinter import filedialog
from UploadFile.uploadfile import mainB


def apitest(top, config):
    def upioad_file_logic():
        value1 = filename.get()
        value1 = str(value1).replace("/", "\\")
        print(value1, type(value1))
        value2 = testversion.get()

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
                mainB(value1, value2)
                for i in range(61, 100):
                    sleep(0.05)
                    change_schedule(i, 99)

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
    window_upioad_file.title('批量接口测试')
    window_upioad_file.resizable(0, 0)

    filename = tkinter.StringVar()
    testversion = tkinter.StringVar()


    filename.set('选择案例位置')
    tkinter.Label(window_upioad_file, text='案例位置: ').place(x=10, y=10)
    tkinter.Entry(window_upioad_file, width=50, textvariable=filename).place(x=90, y=10)
    btn_file_path_tool = tkinter.Button(window_upioad_file, text='..', command=file_path_tool)
    btn_file_path_tool.place(x=500, y=6)

    testversion.set(config.configread("url"))
    tkinter.Label(window_upioad_file, text='Url: ').place(x=10, y=50)
    entry_test_id = tkinter.Entry(window_upioad_file, width=50, textvariable=testversion)
    entry_test_id.place(x=90, y=50)

    str_ = '''
*说明*： 
1、选择案例所处文件夹
2、填写当前版本编号
3、测试报告生成位置在案例所处文件夹
4、模板下载位置在选择案例所处文件夹
'''

    tkinter.Label(window_upioad_file, text=str_, fg="red", justify="left").place(x=10, y=290)

    btn_comfirm_sign_up = tkinter.Button(window_upioad_file, text='开始执行', command=upioad_file_logic)
    btn_comfirm_sign_up.place(x=500, y=550)

    btn_comfirm_sign_up = tkinter.Button(window_upioad_file, text='下载模板', command=upioad_file_logic)
    btn_comfirm_sign_up.place(x=500, y=550)
