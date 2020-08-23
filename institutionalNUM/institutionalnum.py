import random


def haoma():
    ww = [3, 7, 9, 10, 5, 8, 4, 2]  # suan fa yin zi
    cc = []
    dd = 0

    for i in range(8):  # gei CC fu zhi
        cc.append(random.randint(1, 9))
        dd = dd + cc[i] * ww[i]
    for i in range(len(cc)):
        cc[i] = str(cc[i])
    C9 = 11 - dd % 11
    if C9 == 10:
        C9 = 'X'
    else:
        if C9 == 11:
            C9 = '0'
        else:
            C9 = str(C9)
    cc.append('-' + C9)

    return "".join(cc)



