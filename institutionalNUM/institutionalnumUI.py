import tkinter
from .institutionalnum import haoma


def institutional(top):
    def builder():
        institutionalnum.set(haoma())

    window_sign_up = tkinter.Toplevel(top)
    window_sign_up.geometry('400x100')
    window_sign_up.resizable(0, 0)
    window_sign_up.title('组织机构代码生成器')
    institutionalnum = tkinter.StringVar()
    tkinter.Entry(window_sign_up, textvariable=institutionalnum, width=18, font=('Arial', 20), fg='red').place(x=10,
                                                                                                               y=50)
    btn_comfirm_sign_up = tkinter.Button(window_sign_up, text='生成', command=builder)
    btn_comfirm_sign_up.place(x=350, y=50)

    window_sign_up.mainloop()
