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
    print("장문메시지(LMS) 1건 전송")

    Sender = "07075103710" # 발신번호
    ReceiverNum = "010111222" # 수신번호
    ReceiverName = "수신자명"  # 수신자명
    Subject = "장문 문자 제목" # 장문 메시지 제목
    Contents = "장문메시지 단건전송 테스트" # 장문 메시지 내용, 길이가 2000Byte 초과시 길이가 조정되어 전송됨.
    reserveDT = "20150326200000" # 예약전송시간, 형태 yyyyMMddHHmmss, 공백 처리시 즉시전송

    receiptNum = messageService.sendLMS(testValue.testCorpNum,Sender,ReceiverNum,ReceiverName,Subject,Contents,reserveDT)

    print("receiptNum : %s" % receiptNum)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))