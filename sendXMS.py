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
    print("단/장문 자동인식 메시지 1건 전송")
    # 단/장문 자동인식 메시지 전송의 경우 메시지 내용(Contesnts) 길이 90Byte를 기준으로하여 단/장문을 자동인식하여 전송

    # 발신번호
    Sender = "07075103710"

    # 발신자명
    SenderName = "발신자명"

    # 수신번호
    ReceiverNum = "010111222"

    # 수신자명
    ReceiverName = "수신자명"

    # 메시지 내용, 90Byte 기준으로 단/장문 자동인식
    Contents = "장문메시지 단건전송 테스트"

    # 메시지 제목
    Subject = "장문 문자 제목"

    # 예약전송시간, 형태 yyyyMMddHHmmss 공백 처리시 즉시전송
    reserveDT = ""

    # 광고문자 전송여부
    adsYN = False

    receiptNum = messageService.sendXMS(testValue.testCorpNum,Sender,SenderName,ReceiverNum,ReceiverName,Subject,Contents,reserveDT,adsYN)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
