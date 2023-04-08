# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mille\Downloads\Code\COMP_195 Senior Project\senior-project-spring-2023-web-scraping\CarInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1199, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bg_frame = QtWidgets.QFrame(self.centralwidget)
        self.bg_frame.setStyleSheet("QFrame {\n"
"    background-color: #27062D;\n"
"    border-radius: 7px; \n"
"}")
        self.bg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_frame.setObjectName("bg_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bg_frame)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quit_button = QtWidgets.QPushButton(self.bg_frame)
        self.quit_button.setMaximumSize(QtCore.QSize(16, 16))
        self.quit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 11, 68);\n"
"    border-radius: 8px; \n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 11, 68, 150);\n"
"}\n"
"    ")
        self.quit_button.setText("")
        self.quit_button.setObjectName("quit_button")
        self.verticalLayout_2.addWidget(self.quit_button, 0, QtCore.Qt.AlignRight)
        self.frame = QtWidgets.QFrame(self.bg_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: rgb(145, 42, 166);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.button_filter = QtWidgets.QPushButton(self.frame_2)
        self.button_filter.setGeometry(QtCore.QRect(10, 10, 42, 38))
        self.button_filter.setMinimumSize(QtCore.QSize(38, 38))
        self.button_filter.setMaximumSize(QtCore.QSize(42, 38))
        self.button_filter.setSizeIncrement(QtCore.QSize(16, 16))
        self.button_filter.setBaseSize(QtCore.QSize(16, 16))
        self.button_filter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_filter.setStyleSheet("QPushButton {\n"
"    background-color: rgb(181, 84, 215);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(181, 84, 215,150);\n"
"}")
        self.button_filter.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/checkbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_filter.setIcon(icon)
        self.button_filter.setIconSize(QtCore.QSize(38, 38))
        self.button_filter.setObjectName("button_filter")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.bg_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
