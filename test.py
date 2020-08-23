import os

from win32com.client import Dispatch


class ALM(object):
    def __init__(self):
        self.info = {'qcServer': 'http://172.31.27.156:8080/qcbin', 'qcUser': '屈尧', 'qcPassword': '',
                     'qcDomain': '贵州银行信息系统测试2020', 'qcProject': '贵州银行630紫微工程SIT测试'}

    def makeConnect(self):
        tdc = Dispatch("TDApiOle80.TDConnection")
        tdc.InitConnection(self.info['qcServer'])  # ALM服务器名，如：http://192.168.1.10:8080/qcbin
        tdc.Login(self.info['qcUser'], self.info['qcPassword'])  # 用户名，密码
        tdc.Connect(self.info['qcDomain'], self.info['qcProject'])  # 域，项目
        print(tdc.Connected)  # 如果已连接，则为True
        self.tdc = tdc

    def getTestSet(self, testsetid):
        TestSetFact = self.tdc.TestSetFactory
        tsTreeMgr = self.tdc.TestSetTreeManager
        tSetFolder = tsTreeMgr.Root
        tsFilter = TestSetFact.Filter
        tsFilter.SetFilter("CY_CYCLE_ID", testsetid)
        tsList = tSetFolder.FindTestSets("", False, tsFilter.Text)
        print('>>>>>>>>>>>>>>>>>>>>>>>>' + tsList.Item(1).name + '<<<<<<<<<<<<<<<<<<<<<<<<')
        return tsList.Item(1)

    def getTest(self, caseid):
        testF = self.tdc.TestFactory
        testFilter = testF.Filter
        testFilter.SetFilter("TS_TEST_ID", caseid)
        testlst = testF.NewList(testFilter.Text)
        for test in testlst:
            return test
        return ""

    #   获取步骤list
    def getSteplst(self, theTest):
        dsFact = theTest.DesignStepFactory
        steplst = dsFact.NewList("")
        print(steplst.Count)
        return steplst

    #   获取步骤数据
    def getStepData(self, steplist):
        print(steplist.Count)
        if steplist.Count == 0:
            return
        for dsstep in steplist:
            print('步骤名称：', dsstep.StepName, '步骤描述：', dsstep.StepDescription, '步骤预期结果：', dsstep.StepExpectedResult)

    def getAllTestSet(self):
        TreeMgr = self.tdc.TreeManager
        Trees = TreeMgr.RootList
        RootName = Trees.Item(1)
        SubjRoot = TreeMgr.TreeRoot(RootName)
        xdpt = SubjRoot.Child(5).Child(1)
        print('*', xdpt.name, '-', xdpt.Child(1).name)
        xdpt = xdpt.Child(1)
        for i in range(1, xdpt.Count):
            print('**', xdpt.Child(i).name)
            for x in range(1, xdpt.Child(i).Count):
                print('***', xdpt.Child(i).Child(x).name)
                for y in range(1, xdpt.Child(i).Child(x).Count):
                    print('****', xdpt.Child(i).Child(x).Child(y).name)
                    for z in range(1, xdpt.Child(i).Child(x).Child(y).Count):
                        print('*****', xdpt.Child(i).Child(x).Child(y).Child(z).name)

    def test(self, stObject, path_):
        TSTestFilter = stObject.TSTestFactory.Filter
        TestSetTestsList = TSTestFilter.NewList()
        for test in TestSetTestsList:
            casename = test.Field("TS_NAME")
            caseid = test.TestId
            print(path_ + casename + '.docx')
            if os.path.exists(path_ + casename + '.docx'):
                try:
                    os.rename(path_ + casename + '.docx', path_ + '【' + str(caseid) + '】' + casename[-15:] + '.docx')
                except:
                    os.rename(path_ + casename + '.docx', path_ + '【' + str(caseid) + '】' + casename + '.docx')

    def FindTestSets(self, path):
        tdc = self.tdc
        tsTreeMgr = tdc.TestSetTreeManager
        tsFolder = tsTreeMgr.NodeByPath(path)
        tsList = tsFolder.FindTestSets('')
        for atestset in tsList:
            print('>>>>>>>>>>>>>>>>>>>>>>>>' + atestset.name + '<<<<<<<<<<<<<<<<<<<<<<<<')
            print(atestset.ID)
            TSTestFilter = atestset.TSTestFactory.Filter
            TestSetTestsList = TSTestFilter.NewList()
            for test in TestSetTestsList:
                casename = test.Field("TS_NAME")
                testpath = test.FullPath
                print(testpath)
                # 检查是否有附件
                if test.HasAttachment:
                    pass
                else:
                    print(casename, '：无附件')

    def test1(self, stObject):
        TSTestFilter = stObject.TSTestFactory.Filter
        TestSetTestsList = TSTestFilter.NewList()
        for test in TestSetTestsList:

            caseid = test.TestId
            if caseid == '94074':
                casestatus = 'Passed'
            else:
                continue

            # test.Field("TS_USER_01") = '董文夏'
            # test.Status = casestatus
            #
            # test.Post()


# path_ = input(str(r'请输入文件路径，例如（C:\Users\q\Desktop\111111\5669\5669\）：'))#'C:\\Users\\q\\Desktop\\111111\\5669\\5669\\'
# testsetid = input(str(r'请输测试集id：'))
alm = ALM()
alm.makeConnect()
# alm.test(alm.getTestSet(testsetid))
while 1:
    a = str(input('请输入检查路径例如（Root\信贷组\CBP_信贷业务平台\冒烟测试一批次）：'))
    alm.FindTestSets(a)

# testop = alm.test(alm.getTestSet(4325))
# stepstr = alm.getStepData(alm.getSteplst(alm.getTest(testop.TestId)))
# print('end')

# alm.getAllTestSet()
