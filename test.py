# import time
# import datetime
# from dateutil import parser
# 
# 
# #open file
# file = open('keyboard_log.txt', mode='r', encoding='utf-8')
# 
# #init empty list here we put data from file
# list = []
# 
# #add data from file to list
# for lines in file:
#     list.append(lines)
#     
# for lines in file:
#     if list[lines] == '\n':
#        list.remove[lines]     
# #take first and last element of list be course we want calculate sum of time when script was ran
# first_el_of_list = list[0]
# last_el_of_list = list[-1]
# 
# print('Начало работы скрипта : ' + first_el_of_list + 'Конец работы скрипта  : ' + last_el_of_list)
# 
# #parse time from string to time datatype
# start_time = parser.parse(first_el_of_list)
# end_time = parser.parse(last_el_of_list)
# 
# #calculate delta 
# time_when_srcipt_was_on = end_time - start_time
# 
# time_when_srcipt_was_on_str_format = str(time_when_srcipt_was_on)
# 
# print('Время работы скрипта  :            ', time_when_srcipt_was_on_str_format)
# print('-------------------------------------------')
# 
# #delete dublicates in list by doing list to set
# uniq_set = set(list)
# #Time when mouse was in work
# sum_of_seconds = len(uniq_set) - 1
# 
# 
# #format time from int to  time datatype
# formatted_sum_of_seconds = str(datetime.timedelta(seconds=sum_of_seconds))
#     
# print('Время клавы в работе  :            ', formatted_sum_of_seconds)
# 
# #calculate % of time when mouse was in work
# 
# #how much seconds script work time
# start_scr_time_in_sec = time_when_srcipt_was_on.total_seconds()
# 
# #convert time when keyboard was in work from str to time datatype and convert it time to seconds
# formatted_sum_of_seconds_in_seconds = time.strptime(formatted_sum_of_seconds,'%H:%M:%S')
# formatted_sum_of_seconds_in_seconds = datetime.timedelta(hours=formatted_sum_of_seconds_in_seconds.tm_hour,\
#                                                          minutes=formatted_sum_of_seconds_in_seconds.tm_min,\
#                                                          seconds=formatted_sum_of_seconds_in_seconds.tm_sec).total_seconds()
# 
# percent_in_work = (formatted_sum_of_seconds_in_seconds * 100) / start_scr_time_in_sec
# 
# if percent_in_work < 10 :
#     print('Процент занятости     :                %.2f' % percent_in_work)
# else:
#     print('Процент занятости     :               %.2f' % percent_in_work)







# import keyboard
# import time
# from datetime import datetime  
# 
# 
# 
# def myKeyBoardEvent():
#     while True:
#         nowTime = datetime.now()
#         keyBoadrdWasMoveAt = nowTime.strftime('%Y-%m-%d %H:%M:%S')    
#         try:
#             if keyboard.is_pressed('q') != False:   
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('w') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('e') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('r') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('t') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('y') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('u') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)    
#             elif keyboard.is_pressed('i') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)    
#             elif keyboard.is_pressed('o') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)    
#             elif keyboard.is_pressed('p') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)    
#             elif keyboard.is_pressed('[') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)    
#             elif keyboard.is_pressed(']') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('\\') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('a') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('s') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('d') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('f') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('g') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('h') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('j') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('k') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('l') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)  
#             elif keyboard.is_pressed(';') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('\'') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('z') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('x') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('c') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('v') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('b') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('l') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('n') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('m') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed(',') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('.') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('ctrl') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('alt') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('space') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)  
#             elif keyboard.is_pressed('tab') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)    
#             elif keyboard.is_pressed('1') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#             elif keyboard.is_pressed('2') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#             elif keyboard.is_pressed('3') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#             elif keyboard.is_pressed('4') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)                 
#             elif keyboard.is_pressed('5') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)   
#             elif keyboard.is_pressed('6') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#             elif keyboard.is_pressed('7') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#             elif keyboard.is_pressed('8') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)                 
#             elif keyboard.is_pressed('9') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)
#             elif keyboard.is_pressed('0') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#             elif keyboard.is_pressed('-') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#             elif keyboard.is_pressed('=') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2)                 
#             elif keyboard.is_pressed('enter') != False:
#                 print(keyBoadrdWasMoveAt)
#                 time.sleep(0.2) 
#         except(RuntimeError):
#             print('')        
# 
# 
# myKeyBoardEvent()






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