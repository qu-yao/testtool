import tkinter
from tkinter import ttk
from db.idcard import SelectDB, generate_id

sele = SelectDB()

sexnum = 1


def idcaerd(top):
    window_sign_up = tkinter.Toplevel(top)
    window_sign_up.geometry('400x250')
    window_sign_up.resizable(0, 0)
    window_sign_up.title('身份证号码生成器')

    def updata1(*args):
        citylist = sele.select("SELECT DISTINCT city from regionID where province='%s'" % province.get())
        ci["value"] = citylist
        ci.current(0)
        countylist = sele.select(
            "SELECT DISTINCT county from regionID where province='%s' and city='%s'" % (province.get(), citylist[0][0]))
        co["value"] = countylist
        co.current(0)

    def updata2(*args):
        countylist = sele.select(
            "SELECT DISTINCT county from regionID where province='%s' and city='%s'" % (province.get(), city.get()))
        co["value"] = countylist
        co.current(0)

    def updata3(*args):
        global sexnum
        if sex.get() == "女":
            sexnum = 0
        else:
            sexnum = 1

    def builder():
        prtext = province.get()
        citext = city.get()
        cotext = county.get()
        regionid = sele.select(
            "SELECT id from regionID where province='%s' and city='%s' and county='%s'" % (prtext, citext, cotext))
        regionid = str(regionid[0][0])
        print(regionid, type(regionid))
        idcardnum.set(generate_id(sexnum, regionid))

    tkinter.Label(window_sign_up, text="选择身份证所属行政区：").place(x=10, y=10)

    province = tkinter.StringVar()
    provincelist = sele.select("SELECT DISTINCT province from regionID")
    tkinter.Label(window_sign_up, text="省").place(x=10, y=40)
    pr = ttk.Combobox(window_sign_up, textvariable=province, width=10, height=15)
    pr.place(x=40, y=40)
    pr.bind("<<ComboboxSelected>>", updata1, updata2)
    pr["value"] = provincelist
    pr.current(0)

    city = tkinter.StringVar()
    print(province.get(), type(province.get()))
    tkinter.Label(window_sign_up, text="市").place(x=135, y=40)
    ci = ttk.Combobox(window_sign_up, textvariable=city, width=10, height=15)
    ci.place(x=160, y=40)
    ci.bind("<<ComboboxSelected>>", updata2)
    ci.config(value=["北京市"])
    ci.current(0)

    county = tkinter.StringVar()
    tkinter.Label(window_sign_up, text="县/区").place(x=260, y=40)
    co = ttk.Combobox(window_sign_up, textvariable=county, width=10, height=15)
    co.place(x=300, y=40)
    co.config(value=["东城区"])
    co.current(0)

    tkinter.Label(window_sign_up, text="选择性别：").place(x=10, y=75)

    sex = tkinter.StringVar()
    tkinter.Label(window_sign_up, text="性别").place(x=10, y=110)
    se = ttk.Combobox(window_sign_up, textvariable=sex, width=10, height=15)
    se.place(x=40, y=110)
    se["value"] = ['男', '女']
    se.bind("<<ComboboxSelected>>", updata3)
    se.current(0)

    idcardnum = tkinter.StringVar()
    tkinter.Entry(window_sign_up, textvariable=idcardnum, width=18, font=('Arial', 20), fg='red').place(x=10, y=200)

    btn_comfirm_sign_up = tkinter.Button(window_sign_up, text='生成', command=builder)
    btn_comfirm_sign_up.place(x=350, y=200)

    window_sign_up.mainloop()
