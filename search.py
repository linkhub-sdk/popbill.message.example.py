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

try:
    print("=" * 15 + " 문자전송 목록 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 최대 검색기간 : 6개월 이내
    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20180901"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20181010"

    # 전송상태 배열, 1-대기, 2-성공, 3-실패, 4-취소
    State = ['1','2','3','4']

    # 전송유형, SMS-단문, LMS-장문, MMS-포토
    Item = ['SMS', 'LMS', 'MMS']

    # 예약전송 검색여부, 0-전체조회, 1-예약전송건 조회
    ReserveYN = '0'

    # 개인조회여부, 0-전체조회, 1-개인조회
    SenderYN = '0'

    # 페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    #정렬방향, D-내림차순, A-오름차순
    Order = "D"

    response = messageService.search(CorpNum, SDate, EDate, State, Item, ReserveYN,
        SenderYN, Page, PerPage, Order, UserID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    i = 1
    for info in response.list :
        print("====== 문자전송 정보 [%d] ======"% i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
