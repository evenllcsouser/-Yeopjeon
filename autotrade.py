import pyupbit
import schedule
import time

access = ""          # 본인 값으로 변경
secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))            # 보유 현금 조회


def job(): # 아래 것을 주기적으로 실행
    a = upbit.get_balance("KRW")# -5000
    b = upbit.get_balance("KRW-BTC") * pyupbit.get_current_price("KRW-BTC")
    c = upbit.get_balance("KRW-XRP") * pyupbit.get_current_price("KRW-XRP")
    d = upbit.get_balance("KRW-ETH") * pyupbit.get_current_price("KRW-ETH")
    e = a + b + c+ d
    
    if b/e < 0.7 :                                           # 참이려면 비트코인 가격이 하락하였을 때지
        upbit.buy_market_order("KRW-BTC", 0.7*e-b)     # 돈으로
    
    else :
        upbit.sell_market_order("KRW-BTC", (b-0.7*e)/pyupbit.get_current_price("KRW-BTC"))       # BTC로

    if c/e < 0.15 :                                           # 참이려면 비트코인 가격이 하락하였을 때지
        upbit.buy_market_order("KRW-XRP", 0.15*e-c)     # 돈으로
    
    else :
        upbit.sell_market_order("KRW-XRP", (c-0.15*e)/pyupbit.get_current_price("KRW-XRP"))       # XRP로

    if d/e < 0.15 :                                           # 참이려면 비트코인 가격이 하락하였을 때지
        upbit.buy_market_order("KRW-ETH", 0.15*e-d)     # 돈으로
    
    else :
        upbit.sell_market_order("KRW-ETH", (d-0.15*e)/pyupbit.get_current_price("KRW-ETH"))       # ETH로

# schedule.every().hour.do(job)
# schedule.every(1).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":00").do(job)
schedule.every().minute.at(":30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
