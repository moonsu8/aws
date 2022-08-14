######### 공통 라이브러리 ########
import time;
import common;
from pandas import DataFrame

common.getMyInfo()

######## 주문 ########
common.upbit.buy_limit_order("KRW-XRP", 400, 200)
time.sleep(3)

######## 주문이 안됐을 경우 주문취소 ########
r = common.upbit.get_order("KRW-XRP")
if len(r) > 0:
    result = common.upbit.cancel_order(r[0]['uuid'])
    print(result)

######## 주문이 안됐을 경우 주문취소 ########
# 주문상태
# 대기 : wait
# 주문완료 : done
# 주문취소 : cancel
##########################################
result2 = common.upbit.get_order("KRW-XRP", state="done")
df = DataFrame(result2)
df.set_index('created_at')
print(df)

