import tkinter
from tkinter import ttk, messagebox
from .mathresult import mathrut


def interest(top):
    window_sign_up = tkinter.Toplevel(top)
    window_sign_up.geometry('500x500')
    window_sign_up.resizable(0, 0)
    window_sign_up.title('贷款利息计算器')

    sum = tkinter.StringVar()
    deadline = tkinter.StringVar()
    lvnum = tkinter.StringVar()
    payway = tkinter.StringVar()
    lxsum = tkinter.StringVar()
    moneysum = tkinter.StringVar()
    money1sum = tkinter.StringVar()

    # day = tkinter.StringVar()
    # year1 = tkinter.StringVar()
    # month1 = tkinter.StringVar()
    # day1 = tkinter.StringVar()
    #
    # def updatastartdate(*args):
    #     global startdate
    #     startdate = "%s-%s-%s" % (year1.get(), month1.get(), day1.get())
    #     print("startdate:" + startdate)

    def builde(*args):
        # updatastartdate()
        print(sum.get(), deadline.get(), lvnum.get(), payway.get())
        money1sumnum, lxsumnum, moneysumnum = mathrut(sum.get(), deadline.get(), lvnum.get(), payway.get())
        # try:
        #     money1sumnum, lxsumnum, moneysumnum = mathrut(sum.get(), deadline.get(), lvnum.get(),payway.get())
        # except:
        #     messagebox.showerror("错误", "程序出错，请联系管理员！")
        #     return
        print(lxsumnum, moneysumnum)
        lxsum.set(format(lxsumnum, '.4f'))
        moneysum.set(format(moneysumnum, '.4f'))
        mylist.insert('end', money1sumnum)
        # if type(money1sumnum) != float:
        #     money1sum.set(money1sumnum)
        # else:
        #     money1sum.set(format(money1sumnum, '.4f'))

    yearlist = []
    for year2 in range(1990, 2051):
        yearlist.append(year2)
    monthlist = []
    for month2 in range(1, 13):
        monthlist.append(month2)
    daylist = []
    for day2 in range(1, 32):
        daylist.append(day2)
    deadlinelist = []
    for deadline1 in range(1, 61):
        deadlinelist.append(deadline1)

    tkinter.Label(window_sign_up, text="贷款金额：").place(x=10, y=10)
    tkinter.Entry(window_sign_up, textvariable=sum).place(x=70, y=10)

    tkinter.Label(window_sign_up, text="贷款期限：").place(x=10, y=50)

    tkinter.Label(window_sign_up, text="期").place(x=130, y=50)
    de = ttk.Combobox(window_sign_up, textvariable=deadline, width=5, height=15)
    de.place(x=70, y=50)
    de.bind("<<ComboboxSelected>>")
    de["value"] = deadlinelist
    de.current(0)

    tkinter.Label(window_sign_up, text="贷款利率：").place(x=10, y=90)
    tkinter.Entry(window_sign_up, textvariable=lvnum, width=7).place(x=70, y=90)
    tkinter.Label(window_sign_up, text="%").place(x=130, y=90)

    tkinter.Label(window_sign_up, text="贷款方式：").place(x=10, y=130)

    de = ttk.Combobox(window_sign_up, textvariable=payway, width=7, height=15)
    de.place(x=70, y=130)
    de.bind("<<ComboboxSelected>>")
    de["value"] = ["等额本息", "等额本金"]
    de.current(0)

    lxsum.set("00.0000")
    tkinter.Label(window_sign_up, text="累计支付利息：").place(x=10, y=170)
    tkinter.Label(window_sign_up, textvariable=lxsum).place(x=100, y=170)

    moneysum.set("00.0000")
    tkinter.Label(window_sign_up, text="累计还款总额：").place(x=10, y=210)
    tkinter.Label(window_sign_up, textvariable=moneysum).place(x=100, y=210)


    tkinter.Label(window_sign_up, text="每月应还金额：").place(x=10, y=250)
    # tkinter.Label(window_sign_up, textvariable=money1sum).place(x=100, y=250)
    scrollbar = tkinter.Scrollbar(window_sign_up)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    mylist = tkinter.Text(window_sign_up, yscrollcommand=scrollbar.set, width=50, height=10)
    mylist.insert('end', money1sum.get())
    mylist.place(x=10, y=290)
    scrollbar.config(command=mylist.yview)

    btn = tkinter.Button(window_sign_up, text="开始计算", command=builde)
    btn.place(x=420, y=450)

    window_sign_up.mainloop()
