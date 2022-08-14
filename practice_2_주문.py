######### 공통 라이브러리 ########
import common;

common.getMyInfo()

#########################
# 지정가 매수
#:param ticker: 마켓 티커
#:param price: 주문 가격
#:param volume: 주문 수량
#:param contain_req: Remaining-Req 포함여부
#############################

# result = common.upbit.buy_limit_order("KRW-XRP", 350 , 15)
# print(result)


#### 주문금액으로 주문 ##
# 토탈금액으로 매수 매수
#:param ticker: 마켓 티커
#:param ticker: 매수 총금액
###################
# result = common.upbit.buy_market_order("KRW-XRP", 6990)
# print(result)



#########################
# 주문확인 조회 
# 리턴 : 배열
#############################
result = common.getMyOder()
print(result)


#########################
# 주문취소 
# param : uuid
#############################

common.cancelMyOrder(result[0]['uuid'])
