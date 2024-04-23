# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pnframe2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFrame, QTabWidget

from frameseller import seller_TabWidget
from property_dialog import Property_Dialog
from framebuyer import Buyer_Frame


class Agent_MainWindow(object):
    userID = ""

    def __init__(self, x):
                self.userID = x
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 870)
        MainWindow.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"\n"
"}\n"
"QFrame\n"
"{\n"
" background: #470787;\n"
"}\n"
"#frame_5\n"
"{\n"
"background: white;\n"
"border-top-left-radius: 100px;\n"
"}\n"
"#frame_3\n"
"{\n"
"background: #350565;\n"
"}\n"
"#frame_6\n"
"{\n"
"background: #350565;\n"
"border-top-right-radius:100px;\n"
"}\n"
"QPushButton\n"
"{\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"background:white;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"background:#241571;\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"QToolButton\n"
"{\n"
"border-style: solid;\n"
" border-width:2px;\n"
" border-radius:15px;\n"
"background:#af69ef;\n"
"}\n"
"QToolButton:hover\n"
"{\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"background-color:#49ebff;\n"
"color:white;\n"
"}\n"
"#pn\n"
"{\n"
"border-image:url(:/images/PN.jpg);\n"
"}\n"
"QLabel\n"
"{\n"
"color:white;\n"
"font-weight:bold;\n"
"font-style:montserrat;\n"
"font-size:21px;\n"
"}\n"
"#frame_8\n"
"{\n"
"border-radius:60px;\n"
"}\n"
"#frame_9\n"
"{\n"
"background:#C5C6D0;\n"
"}\n"
"#frame_10\n"
"{\n"
"background:#C5C6D0;\n"
"}\n"
"#frame_11\n"
"{\n"
"background:#C5C6D0;\n"
"}\n"
"#frame_bottom\n"
"{\n"
"background:#350565;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1601, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(-30, -50, 599, 78))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pn = QtWidgets.QFrame(self.frame_2)
        self.pn.setGeometry(QtCore.QRect(1440, 0, 161, 61))
        self.pn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pn.setObjectName("pn")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 160, 160, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(12, 177, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 320, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        # self.pushButton_3.setGeometry(QtCore.QRect(10, 460, 111, 31))
        # self.pushButton_3.setObjectName("pushButton_3")
        self.toolButton_dashboard = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_dashboard.setGeometry(QtCore.QRect(30, 120, 61, 51))
        self.toolButton_dashboard.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/house-user-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_dashboard.setIcon(icon)
        self.toolButton_dashboard.setIconSize(QtCore.QSize(60, 25))
        self.toolButton_dashboard.setObjectName("toolButton_dashboard")
        self.toolButton_properties = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_properties.setGeometry(QtCore.QRect(30, 260, 61, 51))
        self.toolButton_properties.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/building-user-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_properties.setIcon(icon1)
        self.toolButton_properties.setIconSize(QtCore.QSize(60, 25))
        self.toolButton_properties.setObjectName("toolButton_properties")
        self.toolButton_agents = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_agents.setGeometry(QtCore.QRect(30, 400, 61, 51))
        self.toolButton_agents.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/user-tie-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_agents.setIcon(icon2)
        self.toolButton_agents.setIconSize(QtCore.QSize(60, 25))
        self.toolButton_agents.setObjectName("toolButton_agents")
        self.label_welcome = QtWidgets.QLabel(self.frame_3)
        self.label_welcome.setGeometry(QtCore.QRect(10, 60, 111, 41))
        self.label_welcome.setSizeIncrement(QtCore.QSize(7, 2))
        self.label_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_welcome.setObjectName("label_welcome")
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 59, 1601, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setGeometry(QtCore.QRect(-50, 0, 1021, 141))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.toolButton_user = QtWidgets.QToolButton(self.frame_6)
        self.toolButton_user.setGeometry(QtCore.QRect(60, 10, 81, 81))
        self.toolButton_user.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_user.setIcon(icon3)
        self.toolButton_user.setIconSize(QtCore.QSize(150, 150))
        self.toolButton_user.setObjectName("toolButton_user")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(160, 0, 351, 41))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(140, 110, 1471, 711))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setGeometry(QtCore.QRect(230, 90, 901, 471))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.toolButton_seller = QtWidgets.QToolButton(self.frame_8)
        self.toolButton_seller.setGeometry(QtCore.QRect(140, 180, 191, 141))
        self.toolButton_seller.setIcon(icon1)
        self.toolButton_seller.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_seller.setObjectName("toolButton_seller")
        self.toolButton_buyer = QtWidgets.QToolButton(self.frame_8)
        self.toolButton_buyer.setGeometry(QtCore.QRect(580, 180, 181, 131))
        self.toolButton_buyer.setIcon(icon2)
        self.toolButton_buyer.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_buyer.setObjectName("toolButton_buyer")
        self.label_seller = QtWidgets.QLabel(self.frame_8)
        self.label_seller.setGeometry(QtCore.QRect(10, 330, 451, 41))
        self.label_seller.setAlignment(QtCore.Qt.AlignCenter)
        self.label_seller.setObjectName("label_seller")
        self.label_buyer = QtWidgets.QLabel(self.frame_8)
        self.label_buyer.setGeometry(QtCore.QRect(580, 320, 211, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_buyer.setFont(font)
        self.label_buyer.setAutoFillBackground(False)
        self.label_buyer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_buyer.setObjectName("label_buyer")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setGeometry(QtCore.QRect(0, 60, 901, 80))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setGeometry(QtCore.QRect(210, 410, 121, 31))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setGeometry(QtCore.QRect(130, 410, 71, 31))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_bottom = QtWidgets.QLabel(self.frame_5)
        self.label_bottom.setGeometry(QtCore.QRect(0, 630, 1481, 81))
        self.label_bottom.setText("")
        self.label_bottom.setObjectName("label_bottom")
        self.frame_bottom = QtWidgets.QFrame(self.frame_5)
        self.frame_bottom.setGeometry(QtCore.QRect(560, 630, 911, 41))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 630, 501, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_copyright = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/copyright-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_copyright.setIcon(icon4)
        self.pushButton_copyright.setObjectName("pushButton_copyright")
        self.horizontalLayout_2.addWidget(self.pushButton_copyright)
        self.pushButton_mailus = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/envelope-circle-check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mailus.setIcon(icon5)
        self.pushButton_mailus.setObjectName("pushButton_mailus")
        self.horizontalLayout_2.addWidget(self.pushButton_mailus)
        self.pushButton_instagram = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/square-instagram.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_instagram.setIcon(icon6)
        self.pushButton_instagram.setObjectName("pushButton_instagram")
        self.horizontalLayout_2.addWidget(self.pushButton_instagram)
        self.pushButton_twitter = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/twitter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_twitter.setIcon(icon7)
        self.pushButton_twitter.setObjectName("pushButton_twitter")
        self.horizontalLayout_2.addWidget(self.pushButton_twitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def property_dialog(self):
            self.dialog = QDialog()
            self.UI = Property_Dialog()
            self.UI.setupUi(self.dialog)
            self.dialog.show()
            self.UI.pushButton.clicked.connect(self.UI.property)

    def buyer_frame(self):
            self.frame = QFrame()
            self.UI = Buyer_Frame(self.userID)
            self.UI.setupUi(self.frame)
            self.frame.show()
            self.UI.pushButton.clicked.connect(self.UI.register)

    def seller_frame(self):
            self.tab = QTabWidget()
            self.UI = seller_TabWidget(self.userID)
            self.UI.setupUi(self.tab)
            self.tab.show()
            self.UI.pushButton_14.clicked.connect(self.UI.upload)
            self.UI.comboBox_2.currentIndexChanged.connect(self.UI.onActivated)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Dashboard"))
        self.pushButton_2.setText(_translate("MainWindow", "Properties"))
        # self.pushButton_3.setText(_translate("MainWindow", "BUYER/SELLER"))
        self.label_welcome.setText(_translate("MainWindow", "WELCOME!"))
        self.label_7.setText(_translate("MainWindow", " AGENT_ID"))
        self.toolButton_seller.setText(_translate("MainWindow", "..."))
        self.toolButton_buyer.setText(_translate("MainWindow", "..."))
        self.label_seller.setText(_translate("MainWindow", "Register the sellers and their property"))
        self.label_buyer.setText(_translate("MainWindow", "Register the buyers"))
        self.pushButton_copyright.setText(_translate("MainWindow", "Copyright"))
        self.pushButton_mailus.setText(_translate("MainWindow", "MAIL US"))
        self.pushButton_instagram.setText(_translate("MainWindow", "INSTAGRAM"))
        self.pushButton_twitter.setText(_translate("MainWindow", "TWITTER"))
import form_rc
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Agent_MainWindow(3)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())