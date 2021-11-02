from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app=QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,800,800)
    win.setWindowTitle("Main Interface")

    label = QtWidgets.QLabel(win)
    label.setText("Test")
    label.move(100,100)

    win.show()
    sys.exit(app.exec())

window()