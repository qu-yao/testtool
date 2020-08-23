import xlrd
import xlwt
from win32com.client import Dispatch


class ExclRead(object):
    def __init__(self, casepath, sheetindex):
        self.wa = xlrd.open_workbook(casepath)
        self.wj = self.wa.sheet_by_index(sheetindex)

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


# 新建并写入数据
class ExclNew(object):
    def __init__(self, sheetname):
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet(sheetname)
        self.x = 0

    def wairt(self, value, y, data):
        self.ws.write(self.x, y, data)
        self.x = self.x + value

    def save(self, filenamepath1, casepath):
        print(filenamepath1 + '/' + casepath.replace('\\', '-') + '.xls')
        self.wb.save(filenamepath1 + '/' + casepath.replace('\\', '-') + '.xls')


def getTest(tdc, caseid):
    testF = tdc.TestFactory
    testFilter = testF.Filter
    testFilter.SetFilter("TS_TEST_ID", caseid)
    testlst = testF.NewList(testFilter.Text)
    test = testlst.Item(1)
    return test


#   获取步骤list
def getSteplst(theTest):
    dsFact = theTest.DesignStepFactory
    steplst = dsFact.NewList("")
    print(steplst.Count)
    return steplst


#   获取步骤数据
def getStepData(steplist):
    list1 = []
    if steplist.Count == 0:
        return list1
    for dsstep in steplist:
        if '<html><body>' in dsstep.StepDescription:
            str04 = dsstep.StepDescription
            str004 = str04.replace('<html><body>', '')
            str0004 = str004.replace('</body></html>', '')
            str05 = dsstep.StepExpectedResult
            str005 = str05.replace('<html><body>', '')
            str0005 = str005.replace('</body></html>', '')
            if '<br/>' in str0004:
                description = str0004.split('<br/>')
            else:
                description = str0004.split('<br>')

            if '<br/>' in str0005:
                expectedresult = str0005.split('<br/>')
            else:
                expectedresult = str0005.split('<br>')
            list1.append(description)
            list1.append(expectedresult)
            return list1

        str03 = dsstep.StepName, '：', dsstep.StepDescription, '——>预期结果：', dsstep.StepExpectedResult
        list1.append(str03)

    return list1


def getTestSet(td, testsetid):
    tdc = td
    TestSetFact = tdc.TestSetFactory
    tsTreeMgr = tdc.TestSetTreeManager
    tSetFolder = tsTreeMgr.Root
    tsFilter = TestSetFact.Filter
    tsFilter.SetFilter("CY_CYCLE_ID", testsetid)
    tsList = tSetFolder.FindTestSets("", False, tsFilter.Text)
    print('>>>>>>>>>>>>>>>>>>>>>>>>' + tsList.Item(1).name + '<<<<<<<<<<<<<<<<<<<<<<<<')
    return tsList.Item(1)


def FindTestSets(td, path):
    tdc = td
    tsTreeMgr = tdc.TestSetTreeManager
    tsFolder = tsTreeMgr.NodeByPath(path)
    tsList = tsFolder.FindTestSets('')
    namelist = []
    idlist = []
    for atestset in tsList:
        print(atestset.name, atestset.id)
        namelist.append(atestset.name)
        idlist.append(atestset.id)
    return namelist, idlist


def spanned_file(qcServer, qcUser, qcPassword, qcDomain, qcProject, casepath, filepath):
    def test(stObject, setname, testSetID):
        TSTestFilter = stObject.TSTestFactory.Filter
        TestSetTestsList = TSTestFilter.NewList()
        for test in TestSetTestsList:
            caseid = test.TestId
            casename = test.Field("TS_NAME")
            casestatus = test.Status
            excl.wairt(0, 0, caseid)
            excl.wairt(0, 1, casename)
            excl.wairt(1, 2, casestatus)

    td = Dispatch("TDApiOle80.TDConnection")
    td.InitConnection(qcServer)
    td.Login(qcUser, qcPassword)
    td.Connect(qcDomain, qcProject)
    excl = ExclNew('Sheet')
    excl.wairt(0, 0, '案例ID')
    excl.wairt(0, 1, '案例名称')
    excl.wairt(1, 2, '案例状态（例如：Passed）')
    namelist, idlist = FindTestSets(td, casepath)
    for setname, testSetID in zip(namelist, idlist):
        test(getTestSet(td, testSetID), setname, testSetID)
    excl.save(filepath, casepath)
    td.logout()


def upioad_file(qcServer, qcUser, qcPassword, qcDomain, qcProject, casepath, filepath):
    td = Dispatch("TDApiOle80.TDConnection")
    td.InitConnection(qcServer)
    td.Login(qcUser, qcPassword)
    td.Connect(qcDomain, qcProject)
    casepath1 = casepath.replace('\\', '-')
    exclread = ExclRead(filepath + '/' + str(casepath1) + '.xls', 0)
    idlist = exclread.Excl_Read_colx(0)
    statuslist = exclread.Excl_Read_colx(2)
    namelist, setidlist = FindTestSets(td, casepath)
    for setname, testSetID in zip(namelist, setidlist):
        stObject = getTestSet(td, testSetID)
        TSTestFilter = stObject.TSTestFactory.Filter
        TestSetTestsList = TSTestFilter.NewList()
        for test in TestSetTestsList:
            if test.TestId in idlist:
                test.Status = statuslist[idlist.index(test.TestId)]
                test.Post()
    td.logout()
