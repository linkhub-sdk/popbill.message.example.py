# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

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
문자 API 서비스 과금정보를 확인합니다.
- https://developers.popbill.com/reference/sms/python/api/point#GetChargeInfo
"""

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 문자유형, SMS(단문)/LMS(장문)/MMS(포토)
    MsgType = "SMS"

    response = messageService.getChargeInfo(CorpNum, MsgType)

    print(" unitCost (전송단가) : %s" % response.unitCost)
    print(" chargeMethod (과금유형) : %s" % response.chargeMethod)
    print(" rateSystem (과금제도) : %s" % response.rateSystem)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
