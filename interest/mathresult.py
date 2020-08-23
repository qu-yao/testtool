import datetime


# def Caltime(date1, date2):
#     # 将字符串转为日期
#     date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
#     date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
#     date_difference = date2 - date1
#     print(date_difference.days)
#     return date_difference.days


def mathrut(sum, deadline, lvnum, payway):
    # 贷款额为a，月利率为i，年利率为I，还款月数为n
    sum, deadline, lvnum, payway = float(sum), int(deadline), float(lvnum), payway
    a = sum
    I = lvnum
    i = I / 1200
    n = deadline
    if payway == "等额本息":
        print("-----等额本息计算-----")
        # 月均还款(本金+利息)
        b = a * i * pow((1 + i), n) / (pow((1 + i), n) - 1)
        # 还款利息总和w
        lxsumnum = n * b - a
        # 应还总金额
        moneysumnum = n * b
        money1sumnum = b
    else:
        print("-----等额本金计算-----")
        money1sumnum, lxsumnum, moneysumnum = 0, 0, 0

        # 每月应还本金
        d = a / n
        str1 = ''
        for m in range(1, n + 1):
            f = (a - d * (m - 1)) * i  # 每月应还利息
            g = d + f
            str1 += ("第%d个月应还金额为%.4f\n" % (m, g))
            lxsumnum += f
        moneysumnum = lxsumnum + a
        money1sumnum=str1

    return money1sumnum, lxsumnum, moneysumnum
