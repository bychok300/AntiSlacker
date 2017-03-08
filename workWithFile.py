import sys
from datetime import datetime
from dateutil import parser


#open file
file = open('log.txt', mode='r', encoding='utf-8')

#init empty list here we put data from file
list = []

#add data from file to list
for lines in file:
    list.append(lines)
    
    
#take first and last element of list be couse we want calculate sum of time when script was ran
first_el_of_list = list[0]
last_el_of_list = list[-1]

print('Начало работы скрипта : ' + first_el_of_list + 'Конец работы скрипта  : ' + last_el_of_list)

#parse time from string to time datatype
start_time = parser.parse(first_el_of_list)
end_time = parser.parse(last_el_of_list)

#calculate delta 
time_when_srcipt_will_on = end_time - start_time

print('Время работы скрипта  : ', str(time_when_srcipt_will_on))
print('-------------------------------------------')

#delete dublicates in list by doing list to set
uniq_set = set(list)

#время работы мыши
sum_of_seconds = len(uniq_set)

#приводим время работы мыши к нормальному формату

sum_of_seconds = '00:00:' + str(sum_of_seconds)
    

#sum_of_seconds_in_timedatatype = parser.parse(sum_of_seconds)
#sum_of_seconds_in_timedatatype = sum_of_seconds_in_timedatatype.strftime('%H:%M:%S')    
    
print('\nВсего секунд в работе :', sum_of_seconds)




print('\nПроцент занятости : ', sum_of_seconds)



