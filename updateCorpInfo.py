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
from popbill import CorpInfo, MessageService, PopbillException

messageService = MessageService(testValue.LinkID, testValue.SecretKey)
messageService.IsTest = testValue.IsTest
messageService.IPRestrictOnOff = testValue.IPRestrictOnOff
messageService.UseStaticIP = testValue.UseStaticIP
messageService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
팝빌 연동회원의 회사정보를 수정합니다.
- https://developers.popbill.com/reference/sms/python/api/member#UpdateCorpInfo
"""

try:
    print("=" * 15 + " 회사정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 회사정보
    corpInfo = CorpInfo(
        # 대표자성명 (최대 100자)
        ceoname="대표자성명",
        # 상호 (최대 200자)
        corpName="상호",
        # 주소 (최대 300자)
        addr="주소",
        # 업태 (최대 100자)
        bizType="업태",
        # 종목 (최대 100자)
        bizClass="종목",
    )

    result = messageService.updateCorpInfo(CorpNum, corpInfo)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
