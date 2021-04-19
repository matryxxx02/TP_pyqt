from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BubbleCursor import BubbleCursor
from math import sqrt
import time 
from random import randrange

class NormalCursor(QWidget):
    def __init__(self, targets, toSelected, currentUserNb, method, density, currentTargetSize):
        QWidget.__init__(self)
        self.targets = targets
        self.currentUserNb = currentUserNb
        self.method = method
        self.density = density
        self.currentTargetSize = currentTargetSize
        self.toSelected = toSelected
        self.selected = self.randomSelector()
        self.selected.toSelect = True
        self.timer = time.time()
        self.highlighted = None

    def select(self, x, y):
        newTime = time.time()
        selectedTarget = 0
        for target in self.targets:
            distance = self.distance(x, y, target)
            if (distance<0):
                self.highlighted = target
                self.highlighted.highlighted = True
                if(target.toSelect == True):
                    self.selected.toSelect = False
                    self.selected = self.randomSelector()
                    selectedTarget = 1
                    if (self.selected == None):
                        # finish
                        self.quitMessageBox()
                    else:
                        self.selected.toSelect = True
            else:
                target.highlighted = False
        result = str(self.currentUserNb)+","+self.method+","+str(self.density)+","+str(self.currentTargetSize)+","+str(newTime - self.timer)+","+str(selectedTarget)
        self.writeResultInCSV(result)
        print(result)
        self.timer = newTime

            
    def sameTarget(self, t1, t2):
        return (t1.x == t2.x and t1.y == t2.y)

    def randomSelector(self):
        if(len(self.toSelected)>0) :
            selected = self.toSelected[randrange(0, len(self.toSelected))]
            self.toSelected.remove(selected)
            return selected
        return None
        
    def writeResultInCSV(self, result):
        with open('result.csv', 'a') as file:
            file.write(result+"\n")
            file.close()

    def distance(self, cursorx, cursory, target):
        x = (target.x - cursorx) ** 2
        y = (target.y - cursory) ** 2
        return sqrt(x + y) - target.size / 2

    def quitMessageBox(self):
        msg = QMessageBox.information(self, "The end", "The experience is finish", QMessageBox.Ok)
        if (msg == QMessageBox.Ok):
            QApplication.quit()