# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import MessageService, PopbillException

messageService = MessageService(testValue.LinkID, testValue.SecretKey)
messageService.IsTest = testValue.IsTest
messageService.IPRestrictOnOff = testValue.IPRestrictOnOff
messageService.UseStaticIP = testValue.UseStaticIP
messageService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
최대 2,000byte의 메시지와 이미지로 구성된 포토문자(MMS) 1건 전송을 팝빌에 접수합니다. (최대 1,000건)
- 이미지 파일 포맷/규격 : 최대 300Kbyte(JPEG), 가로/세로 1,000px 이하 권장
- https://developers.popbill.com/reference/sms/python/api/send#SendMMSOne
"""

try:
    print("=" * 15 + " 멀티메시지(MMS) 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호
    Sender = ""

    # 발신자명
    SenderName = "발신자명"

    # 수신번호
    ReceiverNum = ""

    # 수신자명
    ReceiverName = "수신자명"

    # 장문 메시지 제목
    Subject = "멀티 문자 제목"

    # 장문 메시지 내용, 길이가 2000Byte 초과시 초과된 메시지 내용은 자동으로 제거됩니다.
    Contents = "멀티메시지 단건전송 테스트"

    # 예약전송시간, 형태 yyyyMMddHHmmss, 공백 처리시 즉시전송
    reserveDT = ""

    # 전송할 파일경로 (이미지 파일의 크기는 최대 300Kbyte(JPEG), 가로/세로 1500px 이하 권장)
    FilePath = "test.jpeg"

    # 광고성 메시지 여부 ( true , false 중 택 1)
    # └ true = 광고 , false = 일반
    adsYN = False

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 생성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = messageService.sendMMS(
        CorpNum,
        Sender,
        ReceiverNum,
        ReceiverName,
        Subject,
        Contents,
        FilePath,
        reserveDT,
        adsYN,
        UserID,
        SenderName,
        RequestNum,
    )

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
