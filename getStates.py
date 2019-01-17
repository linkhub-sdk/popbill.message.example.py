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
문자 전송내역 요약정보를 확인합니다. (최대 1000건)
'''

try:
    print("=" * 15 + " 문자전송 요약정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 문자전송 요청시 반환받은 접수번호
    receiptNumList = []
    receiptNumList.append("018041717000000018")
    receiptNumList.append("018041717000000019")

    resultList = messageService.getStates(CorpNum, receiptNumList)

    for index, f in enumerate(resultList):
        print("%d:" % index)
        print("    rNum (접수번호) : %s" % f.rNum)
        print("    sn (일련번호) : %s" % f.sn)
        print("    stat (전송 상태코드) : %s" % f.stat)
        print("    rlt (전송 결과코드) : %s" % f.rlt)
        print("    sDT (전송일시) : %s" % f.sDT)
        print("    rDT (결과코드 수신일시) : %s" % f.rDT)
        print("    net (전송 이동통신사명) : %s" % f.net)
        print("    srt (구 전송 결과코드) : %s" % f.srt)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
