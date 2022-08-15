import pyupbit
from pyupbit import Upbit
from pandas import DataFrame

access = 'RvHg1iA9Vu9U3W8JdZUaOjbdQwcEPR6AscWzyOrk'

secret = 'Ih3YKktjrxuN27TOLo96wy0mXNAF3Ax70rSPy3da'

upbit = Upbit(access,secret)
# balance = upbit.get_balances() 
# print(balance)

#########################
# 현재 계좌정보 조회
#############################

def getMyInfo():
    result =[]
    for data in upbit.get_balances():
        result.append( [data['currency'], float(data['balance'])] )
    df = DataFrame(result)
    df.columns= ["코인","가격"]
    print(df)

#########################
# 주문확인 조회
#############################

def getMyOder():
    result = upbit.get_order("KRW-XRP")
    return result

#########################
# 주문취소
# param : uuid
#############################

def cancelMyOrder(param):
    result = upbit.cancel_order(param)
    print(result)

#########################
# 분당 KRW 코인 정보 전체조회
#############################

def getAllKRWTickers():
    krw_tickers = pyupbit.get_tickers("KRW")
    result = krw_tickers
    return result

#########################
# 해당 코인 분봉 조회
#############################    

def getCoinInfoMin(Coin,minute,count):
    result = pyupbit.get_ohlcv(Coin,minute,count)
    return result
