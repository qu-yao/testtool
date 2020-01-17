# coding=utf-8
import os
import win32com.client


# from pathlib import Path

# url = "http://172.31.212.125:8081/qcbin"
# username = "test"
# password = "123456"
# domain = "TEST"
# project = "test"
# # nodePath = u"Root\公共组"
# # testSetName = u"票据1"
# filename = r"C:\Users\q\Desktop\111111"
# testSetID = 91

def mainB(filename, url, username, password, domain, project, testSetID):
    print(filename, url, username, password, domain, project, testSetID)
    print(type(url))
    td = win32com.client.Dispatch("TDApiOle80.TDConnection")
    td.InitConnection(url)
    td.Login(username, password)
    td.Connect(domain, project)

    # tsFolder = td.TestSetTreeManager.NodeByPath(nodePath)
    # tsList = tsFolder.FindTestSets(testSetName)
    # ts_object = tsList.Item(1)
    # TSTestFact = ts_object.TSTestFactory
    # TestSetTestsList = TSTestFact.NewList("")

    TestSetFilter = td.TestSetFactory.Filter  # 获取过滤器
    TestSetFilter["CY_CYCLE_ID"] = testSetID  # 将test set id作为过滤条件
    stList = TestSetFilter.NewList()  # 获取到过滤得到的结果列表，列表中是对象TestSet
    stObject = stList.Item(1)  # 拿到TestSet对象
    # TSTestFilter = stObject.TSTestFactory.Filter#根据test set获取到test的实例
    # TSTestFilter["TC_STATUS"] = '"No Run" or "Replay"' #设置test的过滤条件
    # stScripts = TSTestFilter.NewList() #得到过滤条件的test列表，列表中是对象TSTest
    TSTestFilter = stObject.TSTestFactory.Filter
    TestSetTestsList = TSTestFilter.NewList()

    print("连接就绪!")
    times = 0
    for test in TestSetTestsList:
        name = test.name
        str1 = name.split("]")
        str2 = str1[1]
        # str2 = str2.encode("utf-8")
        filepath1 = filename + "\\" + str2 + ".docx"
        status = test.Status
        if status != "Passed":
            # test.Status
            # test.Status = "Passed"
            # test.Post()
            if os.path.exists(filepath1):
                attachmentFactory = test.Attachments
                attachment = attachmentFactory.AddItem(None)
                attachment.Filename = filepath1
                attachment.Description = ""
                attachment.Type = 1
                attachment.Post()
                times += 1
                # break
            else:
                print("文件不存在!" + filepath1)
    print("总共上传文件%d个！" % times)
    s = td.logout
