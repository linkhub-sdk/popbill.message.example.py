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
    print("문자 메시지 전송결과 확인")
    
    receiptNum = "015032710000000001" # 문자전송 요청시 반환받은 접수번호
    resultList = messageService.getMessages(testValue.testCorpNum, receiptNum)
    
    #전송결과 항목에 대한 자세한 사항은 "문자 API 연동매뉴얼 > [3.3.1. 전송내역 상태확인] 참조
    
    i = 1
    for f in resultList:
        print("%d:" % i)
        print("    state : %s" % f.state)
        print("    type : %s" % f.type)
        print("    subject : %s" % f.subject)

        print("    sendNum : %s" % f.sendNum)
        print("    receiveNum : %s" % f.receiveNum)
        print("    receiveName : %s" % f.receiveName)
        print("    reserveDT : %s" % f.reserveDT)
        print("    sendDT : %s" % f.sendDT)
        print("    resultDT : %s" % f.resultDT)
        print("    sendResult : %s" % f.sendResult)
        i += 1
    
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))