import keyboard
import time   



while True:
    if keyboard.is_pressed('a') != False:   
        print(keyboard.is_pressed('a'))
        

















# from dateutil import parser
# import datetime
# import time
# 
# time1 = '0:02:02'
# time2 = '0:01:10'
# 
# x = time.strptime(time1,'%H:%M:%S')
# tot = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
# tot = int(tot)
# print(tot)
# x2 = time.strptime(time2,'%H:%M:%S')
# tot2 = datetime.timedelta(hours=x2.tm_hour,minutes=x2.tm_min,seconds=x2.tm_sec).total_seconds()
# tot2 = int(tot2)
# print(tot2)
# 
# 
# 
# per = tot2 * 100 / tot
# 
# print('in proc %.5f ' % per)