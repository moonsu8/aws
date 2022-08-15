######### 공통 라이브러리 ########
from ast import While
import time

from sqlalchemy import true
import common;
from datetime import datetime
now = datetime.now()

#########################
# 설정값
# 1.종료시간 ########
Endtime = 2022915120000

# 2.종가 / 시가의 비율(%)
closePerOpen = 3

# 3.거래량 비율(배)
volumeRatio =  8

# 4.거래량 비교 데이터수(분봉수)
volumeDataNum =  6

#########################
def nowtimeInt():
    nowtime = int(
    str(now.year) + str(now.month) + str(now.day)+ 
    str(now.hour) + str(now.minute)+ str(now.second))
    return nowtime

AllKrwTickers = common.getAllKRWTickers()
time.sleep(0.1)
print(AllKrwTickers)
 
while 1:
    nowtime = nowtimeInt()
    if nowtime < Endtime :
        for idx in range(len(AllKrwTickers)):
            # A= 종가 / 시가 -> 3%이상 (IN 1분 분봉DATA)
            # 해당 데이터를 불러오는 시각(분)에는 데이터가 쌓이는 중이기 때문에 항상 1분전 데이터를 기준으로 삼는다
            a = common.getCoinInfoMin(AllKrwTickers[idx],'minute1',2)
            time.sleep(0.1)
            condition1 = bool( (a.iloc[0]['close'] / a.iloc[0]['open']) > (1 + closePerOpen/100))
            
            # 몇몇 코인들은 코인당 가격이 너무 작아서 (ex: 0.0014(비트토렌트)) 코인당 5원 이상인 것들만 고려함
            condition2 = bool( a.iloc[0]['close'] > 5)
            # 초기화
                
            if condition1 and condition2 :
                print("==================================")
                print(" A= 종가 / 시가 -> 3%이상 패스 종목: ", AllKrwTickers[idx])
                print(" A= 종가 / 시가 -> 3%이상 패스 시간: ", datetime.now())
                print(" A= 종가 / 시가 -> 비율: ", (a.iloc[0]['close'] / a.iloc[0]['open'], " % "))
                print("==================================")
                b_1 = common.getCoinInfoMin(AllKrwTickers[idx],'minute1',volumeDataNum)
                time.sleep(0.1)

                sumMin = 0
                #volumeDataNum의 (리스트수 -1)개의 평균데이터를 취합 
                for idx2 in range(0,volumeDataNum-2):
                    # 이전 5분 거래량의 평균값이 8배 이상 오를경우만 체크됨       
                    sumMin = sumMin + b_1.iloc[idx2]['volume']
                    ##print("idx2 = ",idx2, "sumMin",sumMin)
                perMin =  sumMin/(volumeDataNum-1)  
                
                 # 해당 데이터를 불러오는 시각(분)에는 데이터가 쌓이는 중이기 때문에 항상 1분전 데이터를 기준으로 삼는다
                if b_1.iloc[volumeDataNum-2]['volume'] > (perMin*volumeRatio) :
                    # 성공!
                    print("     ****************성공****************")
                    print("     매매타이밍시간 : ", datetime.now())
                    print("     해당코인명 : ", AllKrwTickers[idx])
                    print("     해당시점 매수가(종가): ", b_1.iloc[volumeDataNum-2]['close'])
                    print("     해당시점 이전 총 거래량(sumMin): ", sumMin )
                    print("     해당시점 이전 평균 거래량(perMin): ", perMin )
                    print("     해당시점 거래량: ", b_1.iloc[volumeDataNum-2]['volume'] )
                    print("     해당시점 거래량변화: ", b_1.iloc[volumeDataNum-2]['volume'] / perMin * 100, " % 증가")
                    print("     매매총데이터 : ", b_1)    
                    print("     ************************************")
        time.sleep(1)    
    else:   
        break



