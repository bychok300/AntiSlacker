import sys 
import math
import time
from datetime import datetime


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from toolz.itertoolz import second
from mouseSpeed import distance

scriptStartAt = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
print(scriptStartAt)

#time.sleep(3)

class Frame:
    def __init__(self, position, time):
        self.position = position
        self.time = time

    def speed(self, frame):
        d = distance(*self.position, *frame.position)
        time_delta = abs(frame.time - self.time)
        return d / time_delta

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)

def get_current_cursor_position():
    pos = QCursor.pos()
    return pos.x(), pos.y()

def get_current_frame():
    return Frame(get_current_cursor_position(), time.time())

 
    

#спрашиваем время каждую минуту
# def check_last_time():
#     nowTime = datetime.now()
#     print('Script still runing :', nowTime)
#     time.sleep(60)

if __name__ == '__main__':
    
    
    
    app = QApplication(sys.argv)

    last_frame = get_current_frame()
    

    while True:
        #объясвляем время
        nowTime = datetime.now()
        mouseWasMoveAt = nowTime.strftime('%Y-%m-%d %H:%M:%S')
        new_frame = get_current_frame()
        
        
        
        if new_frame.speed(last_frame) != 0:
            #print(get_current_cursor_position())
            print(new_frame.speed(last_frame), mouseWasMoveAt)
            last_frame = new_frame
            time.sleep(0.07)
            