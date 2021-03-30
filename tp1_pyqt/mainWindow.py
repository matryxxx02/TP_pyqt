import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def main(args):
	for monArgument in args:
		print(monArgument)

	app = QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle("TP1")
		self.resize(800,500)
		self.widget = QWidget(self)
		self.__createMenuAndToolBar()
		self.setCentralWidget(self.widget)
		self.editor()
		#status bar avec message
		self.statusBar().showMessage("Bienvenue sur ma premiere interface")

	def __createMenuAndToolBar(self):
		#definition des actions
		openFile = QAction(QIcon("images/open.png"), "&Open file", self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip("Open file")
		#connecter les actions aux slots
		openFile.triggered.connect(self.open_file)

		saveFile = QAction(QIcon("images/save.png"), "&Save file", self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.setStatusTip("Save file")
		saveFile.triggered.connect(self.save_file)

		copyFile = QAction(QIcon("images/copy.png"), "&Copy", self)
		copyFile.setShortcut('Ctrl+C')
		copyFile.setStatusTip("Copy file")
		copyFile.triggered.connect(self.copy_file)
		
		quitAction = QAction(QIcon("images/quit.png"), "&Quit", self)
		quitAction.setShortcut('Ctrl+Q')
		quitAction.setStatusTip("Quit")
		quitAction.triggered.connect(self.quit)

		#attribution des actions dans la menubar
		bar = self.menuBar()
		actionFile = bar.addMenu("&File")
		actionFile.addAction(openFile)
		actionFile.addAction(saveFile)
		actionFile.addAction(copyFile)
		actionFile.addSeparator()
		actionFile.addAction(quitAction)

		#attribution des actions dans la toolbar
		toolbar = self.addToolBar("Standard ToolBar")
		toolbar.addAction(openFile)
		toolbar.addAction(saveFile)
		toolbar.addAction(copyFile)
		toolbar.addSeparator()
		toolbar.addAction(quitAction)

	def editor(self):
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)

	def open_file(self):
		name = QFileDialog.getOpenFileName(self, 'Open file')[0]
		file = open(name, 'r')
		extension = name.split('.')[1]

		with file:
			text = file.read()
			if (extension == "html"):
				self.textEdit.setHtml(text)
			else:
				self.textEdit.setText(text)

	def save_file(self):
		name = QFileDialog.getSaveFileName(self, 'Save file')[0]
		if(name!=''):
			file = open(name,'w')
			text = self.textEdit.toPlainText()
			file.write(text)
			file.close()
	
	def copy_file(self):
		print("copy_file")

	def quit(self, event):
		#genere une QMessageBox
		reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if (reply == QMessageBox.Yes):
			sys.exit()
		else:
			pass

	def closeEvent(self, event):
		event.ignore()
		self.quit(self)

if __name__ == "__main__":
	main(sys.argv)
