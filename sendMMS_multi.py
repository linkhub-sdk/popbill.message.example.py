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
    print("멀티메시지(MMS) 다량(최대1000건) 전송")

    # 발신번호(동보전송용)
    Sender = "07075103710"

    # 장문 메시지 제목(동보전송용)
    Subject = "동보전송용 메시지 제목"

    # 장문 메시지 내용, 2000Byte 초과시 길이가 조정되어 전송됨.
    Contents = "동보전송용 메시지 내용"

    # 예약전송시간, 공백 처리시 즉시전송(작성형태 yyyyMMddHHmmss)
    reserveDT = ""

    # 전송할 파일경로
    filePath = "test.jpeg"

    # 광고문자 전송여부
    adsYN = False

    # 개별 전송정보 배열 (최대 1000건)
    messages = []
    for x in range(0, 100):
        messages.append(
                    MessageReceiver(
                                    snd='07075103710', # 발신번호
                                    rcv='010111222', # 수신번호
                                    rcvnm='수신자명'+str(x), # 수신자명
                                    msg='멀티 문자 API TEST', # msg값이 없는 경우 동보전송용 메시지로 전송됨.
                                    sjt='멀티 문자제목'# 장문 메시지 제목
                                   )
                    )


    receiptNum = messageService.sendMMS_Multi(testValue.testCorpNum,Sender,Subject,Contents,messages,filePath,reserveDT,adsYN)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
