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
검색조건을 사용하여 문자전송 내역을 조회합니다.
- 최대 검색기간 : 6개월 이내
'''

try:
    print("=" * 15 + " 문자전송 목록 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 최대 검색기간 : 6개월 이내
    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20190101"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20190117"

    # 전송상태 배열, 1-대기, 2-성공, 3-실패, 4-취소
    State = ['1', '2', '3', '4']

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

    # 정렬방향, D-내림차순, A-오름차순
    Order = "D"

    response = messageService.search(CorpNum, SDate, EDate, State, Item, ReserveYN,
                                     SenderYN, Page, PerPage, Order, UserID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    for info in response.list:
        print("subject (메시지 제목) : " + str(info.subject))
        print("content (메시지 내용) : " + str(info.content))
        print("sendNum (발신번호) : " + str(info.sendNum))
        print("receiveNum (수신번호) : " + str(info.receiveNum))
        print("receiveName (수신자명) : " + str(info.receiveName))
        print("receiptDT (접수일시) : " + str(info.receiptDT))
        print("sendDT (발송일시) : " + str(info.sendDT))
        print("resultDT (전송결과 수신일시) : " + str(info.resultDT))
        print("reserveDT (예약일시) : " + str(info.reserveDT))
        print("state (전송 상태코드) : " + str(info.state))
        print("result (전송 결과코드) : " + str(info.result))
        print("type (메시지 타입) : " + str(info.type))
        print("tranNet (전송처리 이동통신사명) : " + str(info.tranNet))
        print("receiptNum (접수번호) : " + str(info.receiptNum))
        print("requestNum (요청번호) : " + str(info.requestNum) + '\n')

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
