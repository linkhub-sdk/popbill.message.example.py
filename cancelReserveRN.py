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

'''
문자전송요청시 할당한 전송요청번호(requestNum)로 예약문자전송을 취소합니다.
- 예약취소는 예약전송시간 10분전까지만 가능합니다.
- https://docs.popbill.com/message/python/api#CancelReserveRN
'''

try:
    print("=" * 15 + " 예약문자메시지 전송취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 예약문자전송시 할당한 전송요청번호(requestNum)
    requestNum = "20190124-1"

    result = messageService.cancelReserveRN(CorpNum, requestNum)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
