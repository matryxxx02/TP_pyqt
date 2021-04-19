import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ButtonModel import ButtonModel

def main(args):
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle("TP2")
		self.resize(800, 500)
		self.widget = CanvasButton()
		self.setCentralWidget(self.widget)
    
class CanvasButton(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.bbox = QRect(100,100,500,200)
		self.defaultCol = QColor(0, 255, 0)
		self.buttonModel = ButtonModel()
		self.setMouseTracking(True)
		
	#se declenche lors du clic
	def mousePressEvent(self, event):	
		if self.buttonModel.state == "hover":
			self.buttonModel.onPressIn()
		else:
			self.buttonModel.onPressOut()

		self.update()

	#se declenche lorsque la souris bouge
	def mouseMoveEvent(self, event):
		if "press" in self.buttonModel.state:
			# click
			if self.cursorOnEllipse(event.pos()):
				# Inside
				self.buttonModel.onPressIn()
			else:
				# Outside
				self.buttonModel.onPressOut()
		else:
			# pas de click
			if self.cursorOnEllipse(event.pos()):
				# Inside
				self.buttonModel.onHover()
			else:
				# Outside
				self.buttonModel.onIdle()
		self.update()

	#se declenche lors du relachement du clic
	def mouseReleaseEvent(self, event):
		if self.buttonModel.state == "pressIn":
			self.buttonModel.action()
			self.buttonModel.onHover()
		else:
			self.buttonModel.onIdle()
		self.update()

	def paintEvent(self, event):	
		painter = QPainter(self)
		painter.setPen(self.defaultCol)

		if self.buttonModel.state == "hover":
			painter.setBrush(self.buttonModel.hoverCol)
		elif self.buttonModel.state == "pressIn":
			painter.setBrush(self.buttonModel.pressCol)
		else:
			painter.setBrush(self.defaultCol)
			
		painter.drawEllipse(self.bbox)

	def cursorOnEllipse(self, point):
		ellipse = QRegion(self.bbox, QRegion.Ellipse)
		return ellipse.contains(point)

if __name__ == "__main__":
	main(sys.argv)