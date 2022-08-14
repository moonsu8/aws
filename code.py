import requests
import json
import time
import CoinInfo

# 최근 2주일간 분당 평균 거래량조회

AllCoinData = CoinInfo.getAllCoinData()
print(AllCoinData)

for idx in range(len(AllCoinData)):
    # 기준(2주일간 분당평균거래)
    a = CoinInfo.getTwoWeekPerMinData(AllCoinData[idx][0])
    time.sleep(0.1)
    print("코인명 = ", AllCoinData[idx][0]) 
    print("2주간 1분당 평균거래량 =",a)
    print(idx)
    # 현재 분당평균거래
    b = CoinInfo.getMinData(AllCoinData[idx][0],)

    