#coding=utf-8
import os

# try:
import xlrd
# except:
#     os.system(u"cd Spannedfile/xlrd-1.2.0 && python setup.py install")
#     print("\n\n\n\n************执行结束，缺少xlrd包，正在重新执行************\n\n\n\n")
#     os.system(u"python main.py")
#     exit()


class ExclRead(object):
    def __init__(self, filename, sheetid):
        self.wa = xlrd.open_workbook(filename)
        self.wj = self.wa.sheet_by_index(sheetid)

    # 读取数据
    def Excl_Read(self, x, y):
        try:
            data = self.wj.cell(x, y).value
        except:
            data = ""
        return data

    # 读取有效行数
    def Excl_Read_Ynum(self):
        data = self.wj.nrows
        return data

    # 获取这行的所有列，并组成列表
    def Excl_Read_rowx(self, x):
        try:
            data = self.wj.row_values(x)
        except:
            data = []
        return data

    # 获取这列的所有行，并组成列表
    def Excl_Read_colx(self, y):
        try:
            data = self.wj.col_values(y)
        except:
            data = []
        return data

    # 获取所有合并单元格的列表
    def merged(self):
        data = self.wj.merged_cells
        return data

    def Excl_sheet(self):
        data = []
        indexid1 = 0
        while 1:
            try:
                hh = self.wa.sheet_by_index(indexid1)
                data.append(indexid1)
                indexid1 += 1
            except:
                return data
                break

    def sheetname(self):
        data = self.wa.sheet_names()
        return data


