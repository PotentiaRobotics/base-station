from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel, QPushButton, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect
import sys

class RobotViewWindow(QWidget):

    def __init__(self):
        super(RobotViewWindow, self).__init__()
        self.resize(812, 627)
        self.setWindowTitle("Base Station")
        self.initUI()
    
    def initUI(self):

        self.setStyleSheet("background:rgb(41, 50, 65)")

        columnLayout = QVBoxLayout()
        formLayout = QFormLayout()
        groupBox = QGroupBox()

        upperColumn = QVBoxLayout()
        label_1 = QLabel("Camera")
        label_1.setFont(QFont("Roboto", 18))
        label_1.setAlignment(Qt.AlignCenter)
        label_1.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        camera = QLabel()
        camera.setFixedHeight(272)
        camera.setStyleSheet("background:rgb(61,90,128)")
        upperColumn.addWidget(label_1)
        upperColumn.addStretch()
        upperColumn.addWidget(camera)
        upperColumn.setSpacing(0)

        self.logs = []
        title = QLabel("Logs")
        title.setFont(QFont("Roboto", 18))
        title.setStyleSheet("color:rgb(224, 251, 252)")
        title.setAlignment(Qt.AlignCenter)
        formLayout.addRow(title)
        for i in range(20): # currently hardcoded num of logs
            b1 = QPushButton("Info")
            b1.setStyleSheet("background:rgb(152, 193, 217)")
            self.logs.append(b1)
            # self.logs[i].clicked.connect(self.getInfo(i))
            formLayout.addRow(self.logs[i])
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(300)
        scroll.setFixedWidth(320)
        scroll.setStyleSheet("background:rgb(61,90,128)")

        columnLayout.addLayout(upperColumn)
        columnLayout.addWidget(scroll)

        columns2Layout = QVBoxLayout()
        label_2 = QLabel("Route Planning")
        label_2.setFont(QFont("Roboto", 18))
        label_2.setAlignment(Qt.AlignCenter)
        label_2.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        route = QLabel()
        route.setFixedHeight(578)
        route.setStyleSheet("background:rgb(61,90,128)")
        columns2Layout.addWidget(label_2)
        columns2Layout.addStretch()
        columns2Layout.addWidget(route)
        columns2Layout.setSpacing(0)

        columns = QHBoxLayout()
        columns.addLayout(columnLayout)
        columns.addLayout(columns2Layout)
        self.setLayout(columns)
    
    # def getInfo(self, label):
    #     self.logs[label].setText("Hey! You clicked on this button!")
    #     self.update(label)

    # def update(self, label):
    #     self.logs[label].adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = RobotViewWindow()
    win.show()
    sys.exit(app.exec_())