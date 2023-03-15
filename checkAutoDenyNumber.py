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

from popbill import MessageService, PopbillException, RefundForm

messageService = MessageService(testValue.LinkID, testValue.SecretKey)
messageService.IsTest = testValue.IsTest
messageService.IPRestrictOnOff = testValue.IPRestrictOnOff
messageService.UseStaticIP = testValue.UseStaticIP
messageService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
팝빌회원에 등록된 080 수신거부 번호 정보를 확인합니다.
- https://developers.popbill.com/reference/message/python/api/point#CheckAutoDenyNumber
'''

try:
    print("=" * 15 + " 환불 신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 팝빌 아이디
    UserID = testValue.UserID

    autoDenyNumberInfo = messageService.checkAutoDenyNumber(CorpNum, UserID)

    print(" smsdenyNumber (전용 080 번호) : %s" % autoDenyNumberInfo.smsdenyNumber)
    print(" regDT (등록일시) : %s" % autoDenyNumberInfo.regDT)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
