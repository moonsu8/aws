######### 공통 라이브러리 ########
import common;

common.getMyInfo()

#########################
# 지정가 매도
#:param ticker: 마켓 티커
#:param price: 주문 가격
#:param volume: 주문 수량
#:param contain_req: Remaining-Req 포함여부
#############################

#result = common.upbit.sell_limit_order("KRW-XRP", 449 , 15)
#print(result)

#### 주문금액으로 매도 ##
# 개수로매도
#:param ticker: 마켓 티커
#:param ticker: 매도량
###################

result = common.upbit.sell_market_order("KRW-XRP", 15)
print(result)


