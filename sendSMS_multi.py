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
messageService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
최대 90byte의 단문(SMS) 메시지 다수건 전송을 팝빌에 접수합니다. (최대 1,000건)
- 모든 수신자에게 동일한 내용을 전송하거나(동보전송), 수신자마다 개별 내용을 전송할 수 있습니다(대량전송).
- https://developers.popbill.com/reference/sms/python/api/send#SendSMSAll
'''

try:
    print("=" * 15 + " 단문메시지(SMS) 다량(최대1000건) 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호(동보전송용)
    Sender = ""

    # 단문메시지 내용(동보전송용), 길이가 90Byte 초과시 초과된 메시지 내용은 자동으로 제거됩니다.
    Contents = "동보전송용 메시지 내용"

    # 예약전송시간, 형태 yyyyMMddHHmmss 공백 기재시 즉시전송
    reserveDT = ""

    # 광고성 메시지 여부 ( true , false 중 택 1)
    # └ true = 광고 , false = 일반
    adsYN = False

    # 개별수신정보 배열(최대 10000건)
    messages = []
    for x in range(0, 10):
        messages.append(
            MessageReceiver(
                snd='',  # 발신번호
                sndnm='발신자명',  # 발신자명
                rcv='',  # 수신번호
                rcvnm='수신자명' + str(x),  # 수신자명
                msg='단문 문자 API TEST',  # 메시지 내용, msg값이 없는경우 동보전송 메시지로 전송됨
                interOPRefKey='20220803-'+str(x) # 파트너 지정키
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
