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

'''
SMS(단문)를 전송합니다.
 - 메시지 내용이 90Byte 초과시 메시지 내용은 자동으로 제거됩니다.
'''

try:
    print("=" * 15 + " 단문메시지(SMS) 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = "8888888888"

    # 팝빌회원 아이디
    UserID = "koreatest"

    # 발신번호
    Sender = "010-8349-0706"

    # 발신자명
    SenderName = "발신자명"

    # 수신번호
    ReceiverNum = "01083490706"

    # 수신자명
    ReceiverName = "수신자명"

    # 단문메시지 내용, 90Byte 초과시 길이가 조정되 전송됨
    Contents = "aiaiai 무로거부 080-1"

    # 예약전송시간, 형태 yyyyMMddHHmmss 공백 기재시 즉시전송
    reserveDT = "20190207164809"

    # 광고문자 전송여부
    adsYN = True

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = "20190107-002"

    receiptNum = messageService.sendSMS(CorpNum, Sender, ReceiverNum, ReceiverName,
                                        Contents, reserveDT, adsYN, UserID, SenderName, RequestNum)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
