# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import MessageService, PopbillException

messageService =  MessageService(testValue.LinkID,testValue.SecretKey)
messageService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)

    MsgType = "SMS" # 문자유형, SMS(단문)/LMS(장문)/MMS(포토)

    response = messageService.getChargeInfo(testValue.testCorpNum, MsgType, testValue.testUserID)
    
    print(" unitCost (단가) : %s" % response.unitCost)
    print(" chargeMethod (과금유형) : %s" % response.chargeMethod)
    print(" rateSystem (과금제도) : %s" % response.rateSystem)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
