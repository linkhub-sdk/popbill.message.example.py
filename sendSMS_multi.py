# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import MessageService, MessageReceiver, PopbillException

messageService =  MessageService(testValue.LinkID,testValue.SecretKey)
messageService.IsTest = testValue.IsTest

try:
    print("단문메시지(SMS) 다량(최대1000건) 전송")

    # 발신번호(동보전송용)
    Sender = "07075103710"

    # 단문메시지 내용(동보전송용)
    Contents = "동보전송용 메시지 내용"

    # 예약전송시간, 형태 yyyyMMddHHmmss 공백 기재시 즉시전송
    reserveDT = ""

    # 광고문자 전송여부
    adsYN = False

    # 개별수신정보 배열(최대 10000건)
    messages = []
    for x in range(0, 100):
        messages.append(
                    MessageReceiver(
                                    snd = '07075103710', # 발신번호
                                    rcv = '010111222', # 수신번호
                                    rcvnm = '수신자명'+str(x), # 수신자명
                                    msg = '단문 문자 API TEST' # 메시지 내용, msg값이 없는경우 동보전송 메시지로 전송됨
                                   )
                    )


    receiptNum = messageService.sendSMS_multi(testValue.testCorpNum,Sender,Contents,messages,reserveDT,adsYN)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
