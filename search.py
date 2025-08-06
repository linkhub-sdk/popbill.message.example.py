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
검색조건을 사용하여 문자전송 내역을 조회합니다. (조회기간 단위 : 최대 2개월)
- 문자 접수일시로부터 6개월 이내 접수건만 조회할 수 있습니다.
- https://developers.popbill.com/reference/sms/python/api/info#Search
"""

try:
    print("=" * 15 + " 문자전송 목록 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 최대 검색기간 : 6개월 이내
    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20250801"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20250831"

    # 전송상태 배열 ("1" , "2" , "3" , "4" 중 선택, 다중 선택 가능)
    # └ 1 = 대기 , 2 = 성공 , 3 = 실패 , 4 = 취소
    # - 미입력 시 전체조회
    State = ["1", "2", "3", "4"]

    # 검색대상 배열 ("SMS" , "LMS" , "MMS" 중 선택, 다중 선택 가능)
    # └ SMS = 단문 , LMS = 장문 , MMS = 포토문자
    # - 미입력 시 전체조회
    Item = ["SMS", "LMS", "MMS"]

    # 예약여부 (None, False , True 중 택 1)
    # └ None = 전체조회, False = 즉시전송건 조회, True = 예약전송건 조회
    # - 미입력 시 전체조회
    ReserveYN = False

    # 개인조회 여부 (False , True 중 택 1)
    # False = 접수한 문자 전체 조회 (관리자권한)
    # True = 해당 담당자 계정으로 접수한 문자만 조회 (개인권한)
    # 미입력시 기본값 False 처리
    SenderYN = False

    # 페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    # 정렬방향, D-내림차순, A-오름차순
    Order = "D"

    # 조회하고자 하는 발신자명 또는 수신자명
    # - 미입력시 전체조회
    QString = ""

    response = messageService.search(
        CorpNum,
        SDate,
        EDate,
        State,
        Item,
        ReserveYN,
        SenderYN,
        Page,
        PerPage,
        Order,
        UserID,
        QString,
    )

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 목록 건수) : %s " % response.perPage)
    print("pageNum (페이지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    for info in response.list:
        print("subject (메시지 제목) : %s " % info.subject)
        print("content (메시지 내용) : %s " % info.content)
        print("sendNum (발신번호) : %s " % info.sendNum)
        print("senderName (발신자명) : %s " % info.senderName)
        print("receiveNum (수신번호) : %s " % info.receiveNum)
        print("receiveName (수신자명) : %s " % info.receiveName)
        print("receiptDT (접수일시) : %s " % info.receiptDT)
        print("sendDT (전송일시) : %s " % info.sendDT)
        print("resultDT (전송결과 수신일시) : %s " % info.resultDT)
        print("reserveDT (예약일시) : %s " % info.reserveDT)
        print("state (상태코드) : %s " % info.state)
        print("result (결과코드) : %s " % info.result)
        print("type (메시지 타입) : %s " % info.type)
        print("tranNet (전송처리 이동통신사명) : %s " % info.tranNet)
        print("receiptNum (접수번호) : %s " % info.receiptNum)
        print("requestNum (요청번호) : %s " % info.requestNum)
        print("interOPRefKey (파트너 지정키) : %s" % info.interOPRefKey + "\n")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
