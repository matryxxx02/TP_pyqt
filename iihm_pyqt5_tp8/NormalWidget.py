from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Target import Target
from NormalCursor import NormalCursor
import csv

class NormalWidget(QWidget):
    def __init__(self,fileBubble,fileSelectedTarget, currentUserNb, method, density, currentTargetSize):
        QWidget.__init__(self)
        self.targets = []
        self.toSelected = []
        # chargé les fichier csv
        self.createTargets(fileBubble)
        self.createSelectedTargets(fileSelectedTarget)
        self.cursor = NormalCursor(self.targets, self.toSelected, currentUserNb, method, density, currentTargetSize)

    def paintEvent(self, event):
        painter = QPainter(self)
        for target in self.targets:
            target.paint(painter)
        # self.cursor.paint(painter)

    def mouseReleaseEvent(self, event):
        self.cursor.select(event.x(), event.y())
        self.update()

    def createTargets(self, filename):
        with open(filename, 'r') as bubbles:
            reader = csv.reader(bubbles)
            for row in reader:
                self.targets.append(Target(int(row[0]), int(row[1]), int(row[2])))

    def createSelectedTargets(self, filename):
        with open(filename, 'r') as selected:
            reader = csv.reader(selected)
            for row in reader:
                self.toSelected.append(self.targets[int(row[0])])


        
