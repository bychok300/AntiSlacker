import sys 
import math
import time
from datetime import datetime


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


scriptStartAt = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
print('Script start at : ', scriptStartAt)
# time.sleep(3)
# print('Script start at : ', datetime.now())
print('time')

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Frame:
    def __init__(self, position, time):
        self.position = position
        self.time = time

    def speed(self, frame):
        d = distance(*self.position, *frame.position)
        time_delta = abs(frame.time - self.time)
        return d / time_delta

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.last_frame = None
        self.setMouseTracking(True)
    def keyPressEvent(self, event):
        print(event.text())

    def mouseMoveEvent(self, event):
        #объясвляем время
        nowTime = datetime.now()
        mouseWasMoveAt = nowTime.strftime('%H:%M:%S')
        #работаем с окном
        new_frame = Frame((event.x(), event.y()), time.time())

        if self.last_frame:
            print(new_frame.speed(self.last_frame), mouseWasMoveAt) #print speed and time

        self.last_frame = new_frame
           

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.resize(1,1)
    w.show()

    app.exec_()
    
    