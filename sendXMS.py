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

from popbill import MessageService, PopbillException

messageService = MessageService(testValue.LinkID, testValue.SecretKey)
messageService.IsTest = testValue.IsTest
messageService.IPRestrictOnOff = testValue.IPRestrictOnOff
messageService.UseStaticIP = testValue.UseStaticIP

"""
XMS(단문/장문 자동인식)를 전송합니다.
- 메시지 내용의 길이(90byte)에 따라 SMS/LMS(단문/장문)를 자동인식하여 전송합니다.
- 90byte 초과시 LMS(장문)으로 인식 합니다.
- https://docs.popbill.com/message/python/api#SendXMS
"""

try:
    print("=" * 15 + " 단/장문 자동인식 메시지 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호
    Sender = "07043042992"

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

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = messageService.sendXMS(CorpNum, Sender, ReceiverNum, ReceiverName,
                                        Subject, Contents, reserveDT, adsYN, UserID, SenderName, RequestNum)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
