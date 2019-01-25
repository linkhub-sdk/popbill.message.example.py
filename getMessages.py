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
문자전송요청시 발급받은 접수번호(receiptNum)로 전송상태를 확인합니다.
 - 응답항목에 대한 자세한 사항은 "[문자 API 연동매뉴얼] >  3.3.1. GetMessages (전송내역 확인)을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 문자전송 전송결과 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 문자전송 요청시 반환받은 접수번호
    receiptNum = "019012409000000005"

    resultList = messageService.getMessages(CorpNum, receiptNum)

    for index, f in enumerate(resultList):
        print("%d:" % index)
        print("    state (전송상태 코드) : %s" % f.state)
        print("    result (전송결과 코드) : %s" % f.result)
        print("    type (메시지유형) : %s" % f.type)
        print("    subject (메시지 제목) : %s" % f.subject)
        print("    content (메시지 내용) : %s" % f.content)
        print("    sendNum (발신번호) : %s" % f.sendNum)
        print("    senderName (발신자명) : %s" % f.senderName)
        print("    receiveNum (수신번호) : %s" % f.receiveNum)
        print("    receiveName (수신자명) : %s" % f.receiveName)
        print("    receiptDT (접수일시) : %s" % f.receiptDT)
        print("    reserveDT (예약일시) : %s" % f.reserveDT)
        print("    sendDT (전송일시) : %s" % f.sendDT)
        print("    resultDT (전송결과 수신일시) : %s" % f.resultDT)
        print("    tranNet (전송처리 이동통신사명) : %s" % f.tranNet)
        print("    receiptNum (접수번호) : %s" % f.receiptNum)
        print("    requestNum (요청번호) : %s" % f.requestNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
