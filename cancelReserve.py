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
문자전송요청시 발급받은 접수번호(receiptNum)로 예약문자 전송을 취소합니다.
- 예약취소는 예약전송시간 10분전까지만 가능합니다.
'''

try:
    print("=" * 15 + " 예약문자메시지 전송취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 예약문자전송시 발급받은 접수번호(receiptNum)
    receiptNum = "019012409000000011"

    result = messageService.cancelReserve(CorpNum, receiptNum)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
