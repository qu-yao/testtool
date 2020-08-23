import re
import xlwt
from win32com.client import Dispatch


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
        self.wb.save(filenamepath1 + '/' + casepath.replace('\\', '-') + '.xls')


def getTest(tdc, caseid):
    testF = tdc.TestFactory
    testFilter = testF.Filter
    testFilter.SetFilter("TS_TEST_ID", caseid)
    testlst = testF.NewList(testFilter.Text)
    for test in testlst:
        return test
    return ""


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


def spanned_file(qcServer, qcUser, qcPassword, qcDomain, qcProject, casepath, filepath, FlieStatus):
    def test(stObject, setname, testSetID):
        TSTestFilter = stObject.TSTestFactory.Filter
        TestSetTestsList = TSTestFilter.NewList()
        for test in TestSetTestsList:
            caseid = test.TestId
            casename = test.Field("TS_NAME")
            casestatus = test.Status
            module = test.Field("TS_PATH")
            casenature = test.Field("TS_USER_01")
            TS_DESCRIPTION = test.Field("TS_DESCRIPTION")
            str01 = TS_DESCRIPTION.replace('<html><body>', '')
            str03 = str01.replace('</body></html>', '')
            str02 = str03.replace('\n', '')
            if '<br' in str02:
                strlist = re.search(r'验证(.*?)<br', str02).group()
                strlist = strlist.replace('<br', '')
            else:
                strlist = str02
            casedescription = strlist
            print(caseid, type(caseid))

            excl.wairt(0, 0, testSetID)
            excl.wairt(0, 1, setname)
            excl.wairt(0, 2, caseid)
            excl.wairt(0, 3, casename)
            excl.wairt(0, 4, casenature)
            excl.wairt(0, 5, casedescription)
            excl.wairt(0, 6, module)
            if FlieStatus == 0:
                excl.wairt(1, 7, casestatus)
            else:
                excl.wairt(0, 7, casestatus)
                stepstr = getStepData(getSteplst(getTest(td, caseid)))
                excl.wairt(1, 8, str(stepstr))

    def getTestSet(testsetid):
        tdc = td
        TestSetFact = tdc.TestSetFactory
        tsTreeMgr = tdc.TestSetTreeManager
        tSetFolder = tsTreeMgr.Root
        tsFilter = TestSetFact.Filter
        tsFilter.SetFilter("CY_CYCLE_ID", testsetid)
        tsList = tSetFolder.FindTestSets("", False, tsFilter.Text)
        print('>>>>>>>>>>>>>>>>>>>>>>>>' + tsList.Item(1).name + '<<<<<<<<<<<<<<<<<<<<<<<<')
        return tsList.Item(1)

    def FindTestSets(path):
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

    td = Dispatch("TDApiOle80.TDConnection")
    td.InitConnection(qcServer)
    td.Login(qcUser, qcPassword)
    td.Connect(qcDomain, qcProject)
    namelist, idlist = FindTestSets(casepath)
    excl = ExclNew('Sheet')
    excl.wairt(0, 0, '测试集id')
    excl.wairt(0, 1, '测试集名称')
    excl.wairt(0, 2, '案例id')
    excl.wairt(0, 3, '案例名称')
    excl.wairt(0, 4, '案例性质')
    excl.wairt(0, 5, '案例描述')
    excl.wairt(0, 6, '案例模块')
    excl.wairt(0, 7, '案例状态')
    excl.wairt(1, 8, '案例步骤')
    for setname, testSetID in zip(namelist, idlist):
        test(getTestSet(testSetID), setname, testSetID)
    excl.save(filepath, casepath)
    td.logout()

# def upioad_file(qcServer, qcUser, qcPassword, qcDomain, qcProject, testsetid, filepath):
#     alm = ALM(qcServer, qcUser, qcPassword, qcDomain, qcProject)
#     alm.makeConnect()
#     if '+' in testsetid:
#         setlist = testsetid.split('+')
#         for testSetID in setlist:
#             exclread = ExclRead(filepath + '/' + str(testSetID) + '.xls', 0)
#             caseids = exclread.Excl_Read_colx(0)
#             casestatuss = exclread.Excl_Read_colx(2)
#             alm.test1(alm.getTestSet(testSetID), caseids, casestatuss)
#
#     else:
#         exclread = ExclRead(filepath + '/' + str(testsetid) + '.xls', 0)
#         caseids = exclread.Excl_Read_colx(0)
#         casestatuss = exclread.Excl_Read_colx(2)
#         alm.test1(alm.getTestSet(testsetid), caseids, casestatuss)
#
#     alm.logout()
