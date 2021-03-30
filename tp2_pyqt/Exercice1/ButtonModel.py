from PyQt5.QtGui import *

class ButtonModel():
    def __init__(self):
        self.idle = 0
        self.hover = 1
        self.pressIn = 2
        self.pressOut = 3
        self.state = "idle"
        self.hoverCol = QColor(57, 152, 223)
        self.pressCol = QColor(44, 112, 163)

    def action(self):
        print("action:")

    def onIdle(self):
        self.state = "idle"

    def onHover(self):
        self.state = "hover"

    def onPressIn(self):
        self.state = "pressIn"

    def onPressOut(self):
        self.state = "pressOut"
