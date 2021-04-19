from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from math import sqrt
from random import random, randrange
import time 
from csv import writer

class BubbleCursor(QWidget):
    def __init__(self, targets, toSelected, currentUserNb, method, density, currentTargetSize):
        QWidget.__init__(self)
        self.defaultColor = QColor(134, 245, 95)
        self.x = 0
        self.y = 0
        self.size = 10
        self.targets = targets
        self.closest = None
        self.currentUserNb = currentUserNb
        self.method = method
        self.density = density
        self.currentTargetSize = currentTargetSize
        self.toSelected = toSelected
        self.selected = self.randomSelector()
        self.selected.toSelect = True
        self.timer = time.time()

    def paint(self, painter):
        painter.setPen(QPen(self.defaultColor, 1))
        painter.drawEllipse(QPoint(self.x, self.y), self.size, self.size)

    def move(self, x, y):
        self.x = x
        self.y = y
        closest = self.targets[0]
        if(self.closest!= None):
            self.closest.highlighted = False
        minDist = self.distance(x,y,closest)
        for target in self.targets:
            newDist = self.distance(x, y, target)
            if (newDist < minDist):
                minDist = newDist
                closest = target

        self.size = minDist
        self.closest = closest
        self.closest.highlighted = True
            

    def select(self):
        newTime = time.time()
        selectedTarget = 0
        if self.closest.toSelect == True:
            self.selected.toSelect = False
            self.update()
            self.selected = self.randomSelector()
            selectedTarget = 1
            if (self.selected == None):
                self.quitMessageBox()
            else:
                self.selected.toSelect = True
        result = str(self.currentUserNb)+","+self.method+","+str(self.density)+","+str(self.currentTargetSize)+","+str(newTime - self.timer)+","+str(selectedTarget)
        self.writeResultInCSV(result)
        print(result)
        self.timer = newTime
        
    def randomSelector(self):
        if(len(self.toSelected)>0) :
            selected = self.toSelected[randrange(0, len(self.toSelected))]
            self.toSelected.remove(selected)
            print(selected.x, selected.y)
            return selected
        return None


    def distance(self, cursorx, cursory, target):
        x = (target.x - cursorx) ** 2
        y = (target.y - cursory) ** 2
        return sqrt(x + y) - target.size / 2
        
    def writeResultInCSV(self, result):
        with open('result.csv', 'a') as file:
            file.write(result+"\n")
            file.close()
    
    def sameTarget(self, t1, t2):
        return (t1.x == t2.x and t1.y == t2.y)

    def quitMessageBox(self):
        msg = QMessageBox.information(self, "The end", "The experience is finish", QMessageBox.Ok)
        if (msg == QMessageBox.Ok):
            QApplication.quit()
