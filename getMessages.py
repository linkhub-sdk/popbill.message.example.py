# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import MessageService, PopbillException

messageService = MessageService(testValue.LinkID, testValue.SecretKey)
messageService.IsTest = testValue.IsTest

'''
문자전송요청에 대한 전송결과를 확인합니다.
'''

try:
    print("=" * 15 + " 문자전송 전송결과 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 문자전송 요청시 반환받은 접수번호
    receiptNum = "016080910000000009"

    resultList = messageService.getMessages(CorpNum, receiptNum)

    i = 1
    for f in resultList:
        print("%d:" % i)
        print("    state : %s" % f.state)
        print("    type : %s" % f.type)
        print("    subject : %s" % f.subject)
        print("    sendNum : %s" % f.sendNum)
        print("    senderName : %s" % f.senderName)
        print("    receiveNum : %s" % f.receiveNum)
        print("    receiveName : %s" % f.receiveName)
        print("    reserveDT : %s" % f.reserveDT)
        print("    sendDT : %s" % f.sendDT)
        print("    resultDT : %s" % f.resultDT)
        print("    sendResult : %s" % f.sendResult)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
