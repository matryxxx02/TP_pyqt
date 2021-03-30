from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Trace import Trace

class CanvasDessin(QWidget):
    def __init__(self, color, width):
        QWidget.__init__(self)
        QWidget.setMinimumSize(self, 800, 800)
        self.drag = False
        self.traceList = []
        self.colorTrace = color #QColor(124, 255, 155)
        self.widthTrace = width

    #se declenche lors du clic
    def mousePressEvent(self, event):
        self.drag = True
        trace = Trace(self.widthTrace, self.colorTrace)
        trace.points.append(event.pos())
        self.traceList.append(trace)

	#se declenche lorsque la souris bouge
    def mouseMoveEvent(self, event):
        if self.drag == True:
            #recup dernier trace
            trace = self.traceList[len(self.traceList) - 1]
            trace.points.append(event.pos())
        self.update()

    #se declenche lors du relachement du clic
    def mouseReleaseEvent(self, event):
        self.drag = False

    def paintEvent(self, event):	
        for i in range(len(self.traceList)):
            self.paintTrace(self.traceList[i])

    def paintTrace(self, trace):
        path = QPainterPath(trace.points[0])
        painter = QPainter(self)
        for i in range(len(trace.points) - 1):
            painter.setPen(QPen(trace.color, trace.width))
            path.lineTo(trace.points[i])
        painter.drawPath(path)
            
    def changeWidthTrace(self, width):
        self.widthTrace = width
    
    def changeColorTrace(self, color):
        self.colorTrace = color
    
    def resetTraces(self):
        self.traceList = []
        self.update()