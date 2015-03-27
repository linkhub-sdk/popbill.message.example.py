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
    print("문자 전송내역 조회 URL 확인")
    
    TOGO = "BOX" # 문자 전송내역 URL 지정값

    url = messageService.getURL(testValue.testCorpNum,testValue.testUserID,TOGO)

    print("BOX URL : " +url)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))