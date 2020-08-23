import xlrd
import xlwt
from xlutils.copy import copy


# 新建并写入数据
class ExclNew(object):
    def __init__(self, sheetname):
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet(sheetname)

    def wairt(self, x, y, data):
        self.ws.write(x, y, data)

    def save(self, filename):
        self.wb.save(filename)


# 读取数据
def Excl_Read(filename, sheetname, x, y):
    # path = os.path.abspath('.')
    # filename = path + filename
    wa = xlrd.open_workbook(filename)
    wj = wa.sheet_by_name(sheetname)
    data = wj.cell(x, y).value
    return data


# 读取表中有效行数
def Excl_indxout(filename):
    # path = os.path.abspath('.')
    # filename = path + filename
    wa = xlrd.open_workbook(filename)
    wj = wa.sheet_by_index(0)
    data = wj.nrows
    return data


# 打开并修改数据
class ExclWairt(object):
    def __init__(self, filename):
        self.filename = filename
        book = xlrd.open_workbook(self.filename)  # 打开excel
        self.new_book = copy(book)  # 复制excel

    def wairt(self, sheetid, x, y, data):
        sheet = self.new_book.get_sheet(sheetid)  # 获取第几个表格的数据
        sheet.write(x, y, data)  # 修改0行1列的数据为'Haha'

    def save(self):
        self.new_book.save(self.filename)

