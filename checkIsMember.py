# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import MessageService, PopbillException

messageService =  MessageService(testValue.LinkID, testValue.SecretKey)
messageService.IsTest = testValue.IsTest

'''
해당 사업자의 파트너 연동회원 가입여부를 확인합니다.
'''

try:
    print("=" * 15 + " 연동회원 가입여부 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    result = messageService.checkIsMember(CorpNum)

    print("가입여부 : [%d] %s" % (result.code,result.message) )

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
