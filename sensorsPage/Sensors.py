from PyQt5 import QtWidgets, QtGui, Qt3DCore
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGraphicsScene, QGraphicsEllipseItem, QProgressBar
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import pyqtgraph
import sys

class G1Data:
    def __init__(self, one, two):
        self.thing = one
        self.otherThing = two

class SensorsWindow(QWidget):
    def __init__(self):
        super(SensorsWindow, self).__init__()
        self.resize(812, 627)
        self.setWindowTitle("Sensors")
        self.initial()
    
    def initial(self):
        self.setStyleSheet("background:rgb(41, 50, 65)")
        layout = QGridLayout()
        color = QColor(224, 251, 252)
        pen = pyqtgraph.mkPen(color=color, width=5)
        
        upperLeft = QGridLayout()
        upperMid = QLabel()
        upperRight = QGridLayout()
        lowerLeft = pyqtgraph.PlotWidget()
        lowerMid = pyqtgraph.PlotWidget()
        lowerRight = QLabel("Thermal Camera")

        # upperLeft
        left = QVBoxLayout()
        # pie1 = QGraphicsEllipseItem(0, 0, 50, 50)
        # pie1.setPos(0, 0)
        # pie1.setStartAngle(0)
        # pie1.setSpanAngle(60) #placeholder value
        # pie1.setBrush(QColor(198, 96, 62))
        label_1 = QLabel("CPU Temp: (value)")
        label_1.setFont(QFont("Roboto", 12))
        label_1.setAlignment(Qt.AlignTop)
        label_1.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        # left.addItem(pie1)
        left.addWidget(label_1)
        right = QVBoxLayout()
        # pie2 = QGraphicsEllipseItem(0, 0, 50, 50)
        # pie2.setPos(0, 0)
        # pie2.setStartAngle(0)
        # pie2.setSpanAngle(60) #placeholder value
        # pie2.setBrush(QColor(198, 96, 62))
        label_2 = QLabel("System Memory: (value)")
        label_2.setFont(QFont("Roboto", 12))
        label_2.setAlignment(Qt.AlignTop)
        label_2.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        # right.addWidget(pie2)
        right.addWidget(label_2)
        center = QLabel("Uptime: \nMemory: ")
        center.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        upperLeft.addLayout(left, 0, 0)
        upperLeft.addLayout(right, 0, 1)
        upperLeft.addWidget(center, 1, 0, 1, 2)
        layout.addLayout(upperLeft, 0, 0)

        # upperMid
        upperMid.setFixedHeight(302)
        upperMid.setStyleSheet("background:rgb(61,90,128)")
        layout.addWidget(upperMid, 0, 1)

        # upperRight
        graph_1 = pyqtgraph.PlotWidget()
        graph_1.setBackground((61, 90, 128))
        graph_1.setTitle("Graph", color=color, size="20pt")
        graph_1.setLabel('bottom', 'x-axis', color=color)
        graph_1.getAxis('bottom').setTextPen(color)
        graph_1.getAxis('bottom').setPen(color)
        graph_1.setLabel('left', 'y-axis', color=color)
        graph_1.getAxis('left').setTextPen(color)
        graph_1.getAxis('left').setPen(color)
        x = [] #can be replaced with a loop going through data
        y = [] #can be replaced with a loop going through data
        graph_1.plot(x, y, name="line 1", pen=pen, symbol="+", symbolBrush=color) #to plot multiple lines, just repeat this line w/ different x, y values (data based)
        graph_1.addLegend()
        bottom = QGridLayout()
        label_3 = QLabel("Keyboard Speed")
        label_3.setStyleSheet("color: rgb(224, 251, 252)")
        bottom.addWidget(label_3, 0, 0)
        top = QHBoxLayout()
        button_1 = QPushButton("-")
        button_1.clicked.connect(self.decrement)
        button_1.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        button_2 = QPushButton("+")
        button_2.clicked.connect(self.increment)
        button_2.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        top.addWidget(button_1)
        top.addWidget(button_2)
        self.bar = QProgressBar()
        self.bar.setMinimum(0)
        self.bar.setMaximum(100)
        bottom.addLayout(top, 0, 1)
        bottom.addWidget(self.bar, 1, 0, 1, 2)
        upperRight.addWidget(graph_1, 0, 0)
        upperRight.addLayout(bottom, 1, 0)
        layout.addLayout(upperRight, 0, 2)

        # lowerLeft
        lowerLeft.setBackground((61, 90, 128))
        lowerLeft.setTitle("CPU Temperature", color=color, size="20pt")
        lowerLeft.setLabel('bottom', 'Time (seconds)', color=color)
        lowerLeft.getAxis('bottom').setTextPen(color)
        lowerLeft.getAxis('bottom').setPen(color)
        lowerLeft.setLabel('left', 'Temperature (degrees)', color=color)
        lowerLeft.getAxis('left').setTextPen(color)
        lowerLeft.getAxis('left').setPen(color)
        x2 = [] #can be replaced with a loop going through data
        y2 = [] #can be replaced with a loop going through data
        lowerLeft.plot(x2, y2, name="line 1", pen=pen, symbol="+", symbolBrush=color)
        lowerLeft.addLegend()
        layout.addWidget(lowerLeft, 1, 0)

        # lowerMid
        lowerMid.setBackground((61, 90, 128))
        lowerMid.setTitle("Temperature", color=color, size="20pt")
        lowerMid.setLabel('bottom', 'Time (seconds)', color=color)
        lowerMid.getAxis('bottom').setTextPen(color)
        lowerMid.getAxis('bottom').setPen(color)
        lowerMid.setLabel('left', 'Temperature (degrees)', color=color)
        lowerMid.getAxis('left').setTextPen(color)
        lowerMid.getAxis('left').setPen(color)
        x3 = [] #can be replaced with a loop going through data
        y3 = [] #can be replaced with a loop going through data
        lowerMid.plot(x3, y3, name="line 1", pen=pen, symbol="+", symbolBrush=color)
        lowerMid.addLegend()
        layout.addWidget(lowerMid, 1, 1)

        # lowerRight
        lowerRight.setAlignment(Qt.AlignTop)
        lowerRight.setFixedHeight(272)
        lowerRight.setStyleSheet("color: rgb(224, 251, 252);background:rgb(61,90,128)")
        layout.addWidget(lowerRight, 1, 2)
        
        self.setLayout(layout)
    
    def decrement(self):
        self.bar.setValue(self.bar.value() - 10)
    
    def increment(self):
        self.bar.setValue(self.bar.value() + 10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SensorsWindow()
    win.show()
    sys.exit(app.exec_())