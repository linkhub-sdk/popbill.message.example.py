# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import MessageService, MessageReceiver, PopbillException

messageService = MessageService(testValue.LinkID, testValue.SecretKey)
messageService.IsTest = testValue.IsTest
messageService.IPRestrictOnOff = testValue.IPRestrictOnOff
messageService.UseStaticIP = testValue.UseStaticIP

'''
[대량전송] LMS(장문)를 전송합니다.
 - 메시지 내용이 2,000Byte 초과시 초과된 메시지 내용은 자동으로 제거됩니다.
 - https://docs.popbill.com/message/python/api#SendLMS_Multi
'''

try:
    print("=" * 15 + " 장문메시지(LMS) 다량(최대1000건) 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호(동보전송용)
    Sender = "07043042992"

    # 장문 메시지 제목(동보전송용)
    Subject = "동보전송용 메시지 제목"

    # 장문 메시지 내용(동보전송용), 길이가 2000Byte 초과시 초과된 메시지 내용은 자동으로 제거됩니다.
    Contents = "동보전송용 메시지 내용"

    # 예약전송시간, 공백 처리시 즉시전송(작성형태 yyyyMMddHHmmss)
    reserveDT = ""

    # 광고문자 전송여부
    adsYN = False

    # 개별 전송정보 배열 (최대 1000건)
    messages = []
    for x in range(0, 100):
        messages.append(
            MessageReceiver(
                snd='07043042992',  # 발신번호
                sndnm='발신자명',  # 발신자명
                rcv='010111222',  # 수신번호
                rcvnm='수신자명' + str(x),  # 수신자명
                msg='장문 문자 API TEST',  # msg값이 없는 경우 동보전송용 메시지로 전송됨.
                sjt='장문문자제목'  # 장문 메시지 제목
            )
        )

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = messageService.sendLMS_multi(CorpNum, Sender, Subject, Contents,
                                              messages, reserveDT, adsYN, UserID, RequestNum)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
