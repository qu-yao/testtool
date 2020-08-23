import random
from datetime import datetime, timedelta
import sqlite3


def generate_id(sex, regionID):
    print(sex, regionID)
    """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""
    # 随机生成一个区域码(6位数)
    id_number = str(regionID)
    # 限定出生日期范围(8位数)
    start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2000-12-30", "%Y-%m-%d")
    birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
    id_number += str(birth_days)
    # 顺序码(2位数)
    id_number += str(random.randint(10, 99))
    # 性别码(1位数)
    id_number += str(random.randrange(sex, 10, step=2))
    # 校验码(1位数)
    numlist = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    sun = 0
    indexid = 0
    for i in id_number:
        sun += int(i) * numlist[indexid]
        indexid += 1
    print(sun)
    num = sun % 11
    print(num)
    strlist = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    id_number += strlist[num]
    return id_number


class SelectDB(object):
    def __init__(self):
        self.conn = sqlite3.connect('./db/data.db')
        self.c = self.conn.cursor()

    def select(self, sql):
        print(sql)
        # sql = 'select * from COMPANY where id=1'
        self.c.execute(sql)
        data = self.c.fetchall()
        return data

    def connect_close(self):
        self.conn.close()
