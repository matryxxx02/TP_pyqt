import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CanvasDessin import CanvasDessin

def main(args):
    app = QApplication(sys.argv)
    dessin = Dessin()
    dessin.show()
    sys.exit(app.exec_())

class Dessin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.defaultWidth = 1
        self.currentColor = QColor(124, 255, 155)
        self.canvas = CanvasDessin(self.currentColor,self.defaultWidth)
        self.toolbar()
        self.setCentralWidget(self.canvas)
    
    def toolbar(self):
        # selection de la couleur
        pixMap = QPixmap(15,15)
        pixMap.fill(self.currentColor)
        self.colorDialog = QAction(QIcon(pixMap), "&select color", self)
        self.colorDialog.triggered.connect(self.selectColor)
        # selection de l'epaisseur
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(50)
        self.slider.setValue(1)
        self.slider.setPageStep(5)
        self.slider.valueChanged.connect(self.widthSlider)
        # suppression du contenu
        self.resetButton = QPushButton("Reset canvas")
        self.resetButton.clicked.connect(self.resetCanvas)

        toolbar = self.addToolBar("MyToolBar")
        toolbar.addAction(self.colorDialog)
        toolbar.addWidget(self.slider)
        toolbar.addWidget(self.resetButton)

    def selectColor(self):
        self.currentColor = QColorDialog.getColor()
        self.canvas.changeColorTrace(self.currentColor)

    def widthSlider(self,value):
        self.canvas.changeWidthTrace(value)

    def resetCanvas(self):
        self.canvas.resetTraces()

if __name__ == "__main__":
	main(sys.argv)