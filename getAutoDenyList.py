# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import MessageService,PopbillException

messageService =  MessageService(testValue.LinkID,testValue.SecretKey)
messageService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 080수신거부 목록 확인 " + "=" * 15)

    response = messageService.getAutoDenyList(testValue.testCorpNum, testValue.testUserID)

    for info in response :
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        print("")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
