######### 공통 라이브러리 ########
from ast import While
import time

from sqlalchemy import true
import common;
from datetime import datetime
now = datetime.now()

######## 원하는시간 ########
Endtime = 2022815120000

def nowtimeInt():
    nowtime = int(
    str(now.year) + str(now.month) + str(now.day)+ 
    str(now.hour) + str(now.minute)+ str(now.second))
    return nowtime

AllKrwTickers = common.getAllKRWTickers()
time.sleep(0.1)
print(AllKrwTickers)
 
while 1:
    notime = nowtimeInt()
    if notime < Endtime :
        for idx in range(len(AllKrwTickers)):
            # A= 종가 / 시가 -> 3%이상 (IN 1분 분봉DATA)
            a = common.getCoinInfoMin(AllKrwTickers[idx],'minute1',1)
            time.sleep(0.1)
            condition1 = bool(a.iloc[0]['close'] / a.iloc[0]['open'] > 1.03)

            # 초기화
            sum5min = 0    
            if(condition1 == true):
                print("A= 종가 / 시가 -> 3%이상 패스: ", datetime.now())

                b_1 = common.getCoinInfoMin(AllKrwTickers[idx],'minute1',5)
                time.sleep(0.1)
                for idx2 in range(len(b_1)):
                    # 이전 5분 거래량의 평균값이 8배 이상 오를경우만 체크됨       
                    sum5min = sum5min + b_1.iloc[idx2]['volume']
                if( b_1.iloc[4]['volume'] > (sum5min/5)*8 ):
                    # 성공!
                    print("매매타이밍시간 : ", datetime.now())
                    print(AllKrwTickers[idx])
                    print("해당시점 매수가(종가): "+ a.iloc[0]['close'])
                    print("해당시점 거래량: "+ b_1.iloc[4]['volume'] )
                    print(b_1)    
            
    else:   
        break



