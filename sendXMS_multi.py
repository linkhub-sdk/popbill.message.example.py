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

try:
    print("=" * 15 + " 단/장문 자동인식 메시지(XMS) 다량(최대1000건) 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호(동보전송용)
    Sender = "07043042991"

    # 메시지제목(동보전송용)
    Subject = "동보전송용 메시지 제목"

    # 메시지 내용(동보전송용)
    Contents = "동보전송용 메시지 내용"

    # 예약전송시간, 공백 처리시 즉시전송(작성형태 yyyyMMddHHmmss)
    reserveDT = ""

    # 광고문자 전송여부
    adsYN = False

    messages = []  # 개별 전송정보 배열, 최대 1000건

    for x in range(0, 10):
        messages.append(
            MessageReceiver(
                snd='07043042991',  # 발신번호
                sndnm='발신자명',  # 발신자명
                rcv='010111222',  # 수신번호
                rcvnm='수신자명' + str(x),  # 수신자명
                msg='문자 API TEST',  # 90Byte를 기준으로 단/장문을 자동으로 인식하여 전송
                sjt='장문문자제목'  # 장문메시지 제목
            )
        )

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = messageService.sendXMS_multi(CorpNum, Sender, Subject, Contents,
                                              messages, reserveDT, adsYN, UserID, RequestNum)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
