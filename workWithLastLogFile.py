import time
import datetime
from dateutil import parser


#open file
file = open('log.txt', mode='r', encoding='utf-8')

#init empty list here we put data from file
list = []

#add data from file to list
for lines in file:
    list.append(lines)
    
    
#take first and last element of list be course we want calculate sum of time when script was ran
first_el_of_list = list[0]
last_el_of_list = list[-1]

print('Начало работы скрипта : ' + first_el_of_list + 'Конец работы скрипта  : ' + last_el_of_list)

#parse time from string to time datatype
start_time = parser.parse(first_el_of_list)
end_time = parser.parse(last_el_of_list)

#calculate delta 
time_when_srcipt_was_on = end_time - start_time

time_when_srcipt_was_on_str_format = str(time_when_srcipt_was_on)

print('Время работы скрипта  :            ', time_when_srcipt_was_on_str_format)
print('-------------------------------------------')

#delete dublicates in list by doing list to set
uniq_set = set(list)

#Time when mouse was in work
sum_of_seconds = len(uniq_set)

#format time from int to  time datatype
formatted_sum_of_seconds = str(datetime.timedelta(seconds=sum_of_seconds))
    
print('Время мыши в работе   :            ', formatted_sum_of_seconds)

#calculate % of time when mouse was in work

#how much seconds script work time
start_scr_time_in_sec = time_when_srcipt_was_on.total_seconds()

#conver time when moude was in work from str to time datatype and convert it time to seconds
formatted_sum_of_seconds_in_seconds = time.strptime(formatted_sum_of_seconds,'%H:%M:%S')
formatted_sum_of_seconds_in_seconds = datetime.timedelta(hours=formatted_sum_of_seconds_in_seconds.tm_hour,minutes=formatted_sum_of_seconds_in_seconds.tm_min,seconds=formatted_sum_of_seconds_in_seconds.tm_sec).total_seconds()

percent_in_work = (formatted_sum_of_seconds_in_seconds * 100) / start_scr_time_in_sec

if percent_in_work < 10 :
    print('Процент занятости     :                %.2f' % percent_in_work)
else:
    print('Процент занятости     :               %.2f' % percent_in_work)

####


