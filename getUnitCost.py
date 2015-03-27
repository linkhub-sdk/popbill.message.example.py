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
    print("문자 전송 단가 확인")

    MsgType = "SMS" # 문자유형, SMS(단문)/LMS(장문)
    
    unitCost = messageService.getUnitCost(testValue.testCorpNum, MsgType)

    print("단가: %f" % unitCost)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))