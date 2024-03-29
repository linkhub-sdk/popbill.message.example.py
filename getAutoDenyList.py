# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

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
전용 080 번호에 등록된 수신거부 목록을 반환합니다.
- https://developers.popbill.com/reference/sms/python/api/info#GetAutoDenyList
"""

try:
    print("=" * 15 + " 080수신거부 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    response = messageService.getAutoDenyList(CorpNum)

    for info in response:
        print("number (수신거부번호) : " + str(info.number))
        print("regDT (등록일시): " + str(info.regDT) + "\n")
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
