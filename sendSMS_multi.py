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

'''
[대량전송] SMS(단문)를 전송합니다.
 - 메시지 내용이 90Byte 초과시 메시지 내용은 자동으로 제거됩니다.
 - 단건/대량 전송에 대한 설명은 "[문자 API 연동매뉴얼] > 3.2.1 SendSMS(단문전송)"을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 단문메시지(SMS) 다량(최대1000건) 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호(동보전송용)
    Sender = "07043042991"

    # 단문메시지 내용(동보전송용)
    Contents = "동보전송용 메시지 내용"

    # 예약전송시간, 형태 yyyyMMddHHmmss 공백 기재시 즉시전송
    reserveDT = ""

    # 광고문자 전송여부
    adsYN = False

    # 개별수신정보 배열(최대 10000건)
    messages = []
    for x in range(0, 10):
        messages.append(
            MessageReceiver(
                snd='07043042991',  # 발신번호
                sndnm='발신자명',  # 발신자명
                rcv='010111222',  # 수신번호
                rcvnm='수신자명' + str(x),  # 수신자명
                msg='단문 문자 API TEST'  # 메시지 내용, msg값이 없는경우 동보전송 메시지로 전송됨
            )
        )

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = messageService.sendSMS_multi(CorpNum, Sender, Contents, messages,
                                              reserveDT, adsYN, UserID, RequestNum)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
