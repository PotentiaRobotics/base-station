from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QColor

from robotView import RobotViewWindow
from Controller import ControllerWindow

class Ui_BaseStation(object):
    def setupUi(self, BaseStation):
        BaseStation.setObjectName("BaseStation")
        BaseStation.resize(1021, 627)

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        BaseStation.setPalette(palette)
        BaseStation.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(BaseStation)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1021, 611))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(224, 251, 252))
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(224, 251, 252))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(224, 251, 252))
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(224, 251, 252, 128))
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        
        self.MainInterface = QtWidgets.QWidget()
        palette = QPalette()
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        self.MainInterface.setPalette(palette)
        self.MainInterface.setAutoFillBackground(True)
        self.MainInterface.setObjectName("MainInterface")
        self.groupBox = QtWidgets.QGroupBox(self.MainInterface)
        self.groupBox.setGeometry(QtCore.QRect(250, 20, 201, 531))
        palette = QPalette()
        brush = QBrush(QColor(224, 251, 252))
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(61, 90, 128))
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.groupBox.setPalette(palette)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(2)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 151, 31))
        palette = QPalette()
        brush = QBrush(QColor(238, 108, 77))
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 140, 201, 41))
        palette = QPalette()
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        self.line.setPalette(palette)
        self.line.setAutoFillBackground(True)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(0, 190, 201, 41))
        palette = QPalette()
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        self.line_2.setPalette(palette)
        self.line_2.setAutoFillBackground(True)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 71, 31))
        palette = QPalette()
        brush = QBrush(QColor(238, 108, 77))
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 390, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(0, 350, 201, 41))
        palette = QPalette()
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        self.line_3.setPalette(palette)
        self.line_3.setAutoFillBackground(True)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.scrollArea = QtWidgets.QScrollArea(self.MainInterface)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 231, 491))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(61, 90, 128))
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.scrollArea.setPalette(palette)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 212, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 191, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QPalette()
        brush = QBrush(QColor(152, 193, 217))
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.pushButton_2.setPalette(palette)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QPalette()
        brush = QBrush(QColor(152, 193, 217))
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QPalette()
        brush = QBrush(QColor(152, 193, 217))
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.pushButton_4.setPalette(palette)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QPalette()
        brush = QBrush(QColor(152, 193, 217))
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.pushButton_3.setPalette(palette)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QtWidgets.QLabel(self.MainInterface)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 231, 41))
        palette = QPalette()
        brush = QBrush(QColor(224, 251, 252))
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(61, 90, 128))
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(self.MainInterface)
        self.frame.setGeometry(QtCore.QRect(690, 20, 321, 531))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(61, 90, 128))
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(130, 0, 71, 31))
        palette = QPalette()
        brush = QBrush(QColor(224, 251, 252))
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.groupBox2 = QtWidgets.QGroupBox(self.MainInterface)
        self.groupBox2.setGeometry(QtCore.QRect(470, 20, 201, 531))
        palette = QPalette()
        brush = QBrush(QColor(224, 251, 252))
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(61, 90, 128))
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.groupBox2.setPalette(palette)
        self.groupBox2.setAutoFillBackground(True)
        self.groupBox2.setObjectName("groupBox2")
        self.boxLayout = QtWidgets.QVBoxLayout()
        self.label_9 = QtWidgets.QLabel(self.groupBox2)
        self.label_9.setGeometry(QtCore.QRect(60, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel()
        self.label_10.setGeometry(QtCore.QRect(10, 50, 201, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel()
        self.label_11.setGeometry(QtCore.QRect(10, 160, 201, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel()
        self.label_12.setGeometry(QtCore.QRect(10, 240, 201, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton()
        palette = QPalette()
        brush = QBrush(QColor(152, 193, 217))
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.pushButton_5.setPalette(palette)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton()
        palette = QPalette()
        brush = QBrush(QColor(152, 193, 217))
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(41, 50, 65))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.pushButton_6.setPalette(palette)
        self.pushButton_6.setObjectName("pushButton_6")
        self.boxLayout.addWidget(self.label_10)
        self.boxLayout.addWidget(self.label_11)
        self.boxLayout.addWidget(self.label_12)
        self.boxLayout.addWidget(self.pushButton_5)
        self.boxLayout.addWidget(self.pushButton_6)
        self.groupBox2.setLayout(self.boxLayout)

        self.tabWidget.addTab(self.MainInterface, "")
        self.Sensors = QtWidgets.QWidget()
        self.Sensors.setObjectName("Sensors")
        self.tabWidget.addTab(self.Sensors, "")
        self.RobotView = RobotViewWindow()
        self.RobotView.setObjectName("RobotView")
        self.tabWidget.addTab(self.RobotView, "")
        self.tab_2 = ControllerWindow()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        BaseStation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BaseStation)
        self.statusbar.setObjectName("statusbar")
        BaseStation.setStatusBar(self.statusbar)

        self.retranslateUi(BaseStation)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BaseStation)

    def retranslateUi(self, BaseStation):
        BaseStation.setWindowTitle("BaseStation")
        self.groupBox.setTitle("Middle Page")
        self.label.setText("Potentia")
        self.label_2.setText("Robotics")
        self.label_3.setText("Control Systems")
        self.label_4.setText("V 1.0")
        self.label_5.setText("Profile: Raspberry Pi\nSpeed: ___\nDuration: ___\nConnection: 10/10")
        self.label_7.setText("Profile: Controller\nSpeed: ___\nDuration: ___\nConnection: 10/10")
        self.label_9.setText("Connection")
        self.label_10.setText("Battery: ___\nConnection: ___\nDuration of Connection: ___\nPing: ___")
        self.label_11.setText("Robot Orientation Display")
        self.label_12.setText("Logging Display\n\tMotor Speed: ___\n\tIMU Values: ___")
        self.pushButton_2.setText("PushButton")
        self.pushButton.setText("PushButton")
        self.pushButton_4.setText("PushButton")
        self.pushButton_3.setText("PushButton")
        self.pushButton_5.setText("Change Mode")
        self.pushButton_6.setText("Shut Down")
        self.label_6.setText("Logs")
        self.label_8.setText("Graphs")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainInterface), "Main Interface")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sensors), "Sensors")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RobotView), "Robot View")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Controller")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaseStation = QtWidgets.QMainWindow()
    ui = Ui_BaseStation()
    ui.setupUi(BaseStation)
    BaseStation.show()
    sys.exit(app.exec_())