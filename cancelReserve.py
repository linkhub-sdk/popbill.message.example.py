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
    print("예약문자 전송취소")
    # 예약문자 취소는 예약전송시간 10분전까지만 가능

    receiptNum = "015032618000000011" # 문자전송 요청시 반환받은 접수번호

    result = messageService.cancelReserve(testValue.testCorpNum, receiptNum)
    print("처리결과 : [%d] %s" % (result.code,result.message))        
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))