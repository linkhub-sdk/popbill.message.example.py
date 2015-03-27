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
    print("연동회원 가입여부 확인")
    
    result = messageService.checkIsMember(testValue.testCorpNum)
    
    print("가입여부 : %d %s" % (result.code,result.message) )

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))