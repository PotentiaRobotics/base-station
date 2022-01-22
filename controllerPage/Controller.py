from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QShortcut, QBoxLayout
from PyQt5.QtCore import QTime, Qt
import sys

class Window(QMainWindow):
   def __init__(self):
      super(Window, self).__init__()
      self.starting_state()
      
   def starting_state(self):
      self.setGeometry(0, 0, 1005, 575)
      self.setWindowTitle("Controller")
      self.setStyleSheet("background-color: #3D5A80;")
      self.extra = None
      
      self.main_interface = QtWidgets.QPushButton(self)
      self.main_interface.move(10, 5)
      self.main_interface.resize(30, 40)
      self.main_interface.setText("Main Interface")
      self.main_interface.setStyleSheet('QPushButton {background-color: #98C1D5; border-style: outset; border-width: 3px; border-color: black; font: bold 20px; min-width: 10em;}')
      self.main_interface.clicked.connect(self.main_interface_clicked)

      self.sensors = QtWidgets.QPushButton(self)
      self.sensors.move(260, 5)
      self.sensors.resize(30, 40)
      self.sensors.setText("Sensors")
      self.sensors.setStyleSheet('QPushButton {background-color: #98C1D5; border-style: outset; border-width: 3px; border-color: black; font: bold 20px; min-width: 10em;}')
      self.sensors.clicked.connect(self.sensors_clicked)
      
      self.robot_view = QtWidgets.QPushButton(self)
      self.robot_view.move(510, 5)
      self.robot_view.resize(30, 40)
      self.robot_view.setText("Robot View")
      self.robot_view.setStyleSheet('QPushButton {background-color: #98C1D5; border-style: outset; border-width: 3px; border-color: black; font: bold 20px; min-width: 10em;}')
      self.robot_view.clicked.connect(self.robot_view_clicked)
      
      self.controller = QtWidgets.QPushButton(self)
      self.controller.move(760, 5)
      self.controller.resize(30, 40)
      self.controller.setText("Controller")
      self.controller.setStyleSheet('QPushButton {background-color: #3D5A80; border-style: outset; border-width: 3px; border-color: black; font: bold 20px; color: #E0FBFC; min-width: 10em;}')
      self.controller.clicked.connect(self.controller_clicked)

      self.label = QtWidgets.QLabel(self)
      self.picture = QtGui.QPixmap('Controller.png')
      self.label.setScaledContents(True)
      self.label.setPixmap(self.picture)
      self.label.resize(970, 500)
      self.label.move(20, 50)

      self.key1 = QShortcut(QKeySequence('M'), self)
      self.key1.activated.connect(self.keyboard)
      self.key2 = QShortcut(QKeySequence('N'), self)
      self.key2.activated.connect(self.keyboard)
      self.key3 = QShortcut(QKeySequence('L'), self)
      self.key3.activated.connect(self.keyboard)
      self.key4 = QShortcut(QKeySequence('A'), self)
      self.key4.activated.connect(self.keyboard)
      self.key5 = QShortcut(QKeySequence('F'), self)
      self.key5.activated.connect(self.keyboard)
      self.key6 = QShortcut(QKeySequence('T'), self)
      self.key6.activated.connect(self.keyboard)
      self.key7 = QShortcut(QKeySequence('D'), self)
      self.key7.activated.connect(self.keyboard)
      self.key8 = QShortcut(QKeySequence('R'), self)
      self.key8.activated.connect(self.keyboard)
      self.key9 = QShortcut(QKeySequence('J'), self)
      self.key9.activated.connect(self.keyboard)
      self.key0 = QShortcut(QKeySequence('W'), self)
      self.key0.activated.connect(self.keyboard)
   
   def main_interface_clicked(self):
      popup = QMessageBox()
      popup.setWindowTitle("Popup")
      time = QTime.currentTime()
      popup.setText("The main interface button has been clicked at " + time.toString(Qt.DefaultLocaleLongDate))
      popup.exec_()
   
   def sensors_clicked(self):
      popup = QMessageBox()
      popup.setWindowTitle("Popup")
      time = QTime.currentTime()
      popup.setText("The sensors button has been clicked at " + time.toString(Qt.DefaultLocaleLongDate))
      popup.exec_()
   
   def robot_view_clicked(self):
      popup = QMessageBox()
      popup.setWindowTitle("Popup")
      time = QTime.currentTime()
      popup.setText("The robot view button has been clicked at " + time.toString(Qt.DefaultLocaleLongDate))
      popup.exec_()

   def controller_clicked(self):
      popup = QMessageBox()
      popup.setWindowTitle("Popup")
      time = QTime.currentTime()
      popup.setText("The controller button has been clicked at " + time.toString(Qt.DefaultLocaleLongDate))
      popup.exec_()
   
   def keyboard(self):
      popup = QMessageBox()
      popup.setWindowTitle("Popup")
      time = QTime.currentTime()
      popup.setText("A button (either M, N, L, A, F, T, D, R, J, W) has been clicked at " + time.toString(Qt.DefaultLocaleLongDate))
      popup.exec_()

def win():
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec_())

win()