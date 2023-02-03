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
messageService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
문자 전송시 과금되는 포인트 단가를 확인합니다.
- https://developers.popbill.com/reference/sms/python/api/point#GetUnitCost
'''

try:
    print("=" * 15 + " 문자메시지 전송단가 확인 " + "=" * 15)

    # 팝빌회원 아이디
    CorpNum = testValue.testCorpNum

    # 문자전송유형, SMS(단문) / LMS(장문) / MMS(포토)
    MsgType = "SMS"

    unitCost = messageService.getUnitCost(CorpNum, MsgType)

    print(MsgType + " 전송단가 : %d" % unitCost)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
