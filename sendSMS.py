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
    print("단문메시지(SMS) 1건 전송")

    Sender = "07075103710" # 발신번호
    ReceiverNum = "010111222" # 수신번호
    ReceiverName = "수신자명" # 수신자명
    Contents = "문자 API 단건전송 테스트" # 단문메시지 내용, 90Byte 초과시 길이가 조정되 전송됨
    reserveDT = "20150326200000" # 예약전송시간, 형태 yyyyMMddHHmmss 공백 기재시 즉시전송

    receiptNum = messageService.sendSMS(testValue.testCorpNum,Sender,ReceiverNum,ReceiverName,Contents,reserveDT)

    print("receiptNum : %s" % receiptNum)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))