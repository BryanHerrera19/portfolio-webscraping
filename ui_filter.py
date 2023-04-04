# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mille\Downloads\Code\COMP_195 Senior Project\senior-project-spring-2023-web-scraping\filter.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_frame_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.background_frame_2.setContentsMargins(10, 10, 10, 10)
        self.background_frame_2.setSpacing(0)
        self.background_frame_2.setObjectName("background_frame_2")
        self.background_frame = QtWidgets.QFrame(self.centralwidget)
        self.background_frame.setStyleSheet("QFrame {\n"
"    background-color: #27062D;\n"
"    border-radius: 7px; \n"
"}")
        self.background_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame.setObjectName("background_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.background_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_main_frame = QtWidgets.QFrame(self.background_frame)
        self.left_main_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.left_main_frame.setMaximumSize(QtCore.QSize(285, 16777215))
        self.left_main_frame.setStyleSheet("QFrame {\n"
"    background-color: #27062D;\n"
"    border-radius: 7px; \n"
"}")
        self.left_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_main_frame.setObjectName("left_main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_main_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo_frame = QtWidgets.QFrame(self.left_main_frame)
        self.logo_frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.logo_frame.setStyleSheet("QFrame {\n"
"    background-color: #27062D;\n"
"    border-radius: 7px; \n"
"}")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.logo_frame)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.Hbutton = QtWidgets.QPushButton(self.logo_frame)
        self.Hbutton.setMinimumSize(QtCore.QSize(0, 0))
        self.Hbutton.setMaximumSize(QtCore.QSize(1000, 100))
        self.Hbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Hbutton.setStyleSheet("QPushButton { \n"
"    border:none;\n"
"    background-color: #27062D;\n"
"    font-size: 50px; \n"
"    font-weight: bold; \n"
"    font-family: Segoe Print;\n"
"    color: white;\n"
"} \n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(156,39,176);\n"
"}\n"
"\n"
"")
        self.Hbutton.setObjectName("Hbutton")
        self.verticalLayout_14.addWidget(self.Hbutton, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.logo_frame)
        self.filter_frame = QtWidgets.QFrame(self.left_main_frame)
        self.filter_frame.setStyleSheet("QFrame{\n"
"    background-color: #27062D;\n"
"}")
        self.filter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filter_frame.setObjectName("filter_frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.filter_frame)
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.inside_filter_frame = QtWidgets.QFrame(self.filter_frame)
        self.inside_filter_frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(146, 91, 156);\n"
"}")
        self.inside_filter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inside_filter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inside_filter_frame.setObjectName("inside_filter_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.inside_filter_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.inside_filter_frame)
        self.label.setStyleSheet("QLabel {\n"
"    background-color: #B554D7;\n"
"    border-radius: 8px; \n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    font-family: Open Sans; \n"
"    color:white;\n"
"    text-align: center;\n"
"} ")
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.filter_Button = QtWidgets.QPushButton(self.inside_filter_frame)
        self.filter_Button.setObjectName("filter_Button")
        self.verticalLayout_6.addWidget(self.filter_Button)
        self.price_frame = QtWidgets.QFrame(self.inside_filter_frame)
        self.price_frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(105, 50, 126);\n"
"}")
        self.price_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.price_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.price_frame.setObjectName("price_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.price_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.price_bar = QtWidgets.QLabel(self.price_frame)
        self.price_bar.setStyleSheet("QLabel {\n"
"    background-color: #B554D7;\n"
"    border-radius: 8px; \n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    font-family: Open Sans; \n"
"    color:white\n"
"} ")
        self.price_bar.setObjectName("price_bar")
        self.verticalLayout_9.addWidget(self.price_bar, 0, QtCore.Qt.AlignTop)
        self.price_slider = QtWidgets.QSlider(self.price_frame)
        self.price_slider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.price_slider.setMaximum(50000)
        self.price_slider.setPageStep(1)
        self.price_slider.setOrientation(QtCore.Qt.Horizontal)
        self.price_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.price_slider.setTickInterval(1)
        self.price_slider.setObjectName("price_slider")
        self.verticalLayout_9.addWidget(self.price_slider)
        self.price_label = QtWidgets.QLabel(self.price_frame)
        self.price_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"    font-size:20pt;\n"
"    font-weight:bold;\n"
"}")
        self.price_label.setObjectName("price_label")
        self.verticalLayout_9.addWidget(self.price_label)
        self.verticalLayout_6.addWidget(self.price_frame)
        self.mile_frame = QtWidgets.QFrame(self.inside_filter_frame)
        self.mile_frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(105, 50, 126);\n"
"}")
        self.mile_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mile_frame.setObjectName("mile_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mile_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.miles_bar = QtWidgets.QLabel(self.mile_frame)
        self.miles_bar.setStyleSheet("QLabel {\n"
"    background-color: #B554D7;\n"
"    border-radius: 8px; \n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    font-family: Open Sans; \n"
"    color:white;\n"
"} ")
        self.miles_bar.setObjectName("miles_bar")
        self.verticalLayout_10.addWidget(self.miles_bar, 0, QtCore.Qt.AlignTop)
        self.miles_slider = QtWidgets.QSlider(self.mile_frame)
        self.miles_slider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.miles_slider.setMaximum(100000)
        self.miles_slider.setPageStep(1)
        self.miles_slider.setOrientation(QtCore.Qt.Horizontal)
        self.miles_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.miles_slider.setObjectName("miles_slider")
        self.verticalLayout_10.addWidget(self.miles_slider)
        self.mile_label = QtWidgets.QLabel(self.mile_frame)
        self.mile_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"    font-size:20pt;\n"
"    font-weight:bold;\n"
"}")
        self.mile_label.setObjectName("mile_label")
        self.verticalLayout_10.addWidget(self.mile_label)
        self.verticalLayout_6.addWidget(self.mile_frame)
        self.drop_down_frame = QtWidgets.QFrame(self.inside_filter_frame)
        self.drop_down_frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(105, 50, 126);\n"
"}")
        self.drop_down_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drop_down_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_down_frame.setObjectName("drop_down_frame")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.drop_down_frame)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.year_brand_dropdown = QtWidgets.QToolBox(self.drop_down_frame)
        self.year_brand_dropdown.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_brand_dropdown.setStyleSheet("QToolBox {\n"
"    background-color: #B554D7;\n"
"    border-radius: 8px;\n"
"    font-size:20pt; \n"
"    font-weight: bold;\n"
"    font-family: Open Sans; \n"
"    color:white;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"    text-align: left;\n"
"}")
        self.year_brand_dropdown.setObjectName("year_brand_dropdown")
        self.brand_title = QtWidgets.QWidget()
        self.brand_title.setGeometry(QtCore.QRect(0, 0, 189, 303))
        self.brand_title.setObjectName("brand_title")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.brand_title)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.brand_check_frame = QtWidgets.QFrame(self.brand_title)
        self.brand_check_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.brand_check_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.brand_check_frame.setObjectName("brand_check_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.brand_check_frame)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.nis_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.nis_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nis_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.nis_check.setObjectName("nis_check")
        self.verticalLayout_7.addWidget(self.nis_check)
        self.lex_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.lex_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lex_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.lex_check.setObjectName("lex_check")
        self.verticalLayout_7.addWidget(self.lex_check)
        self.chev_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.chev_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chev_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.chev_check.setObjectName("chev_check")
        self.verticalLayout_7.addWidget(self.chev_check)
        self.ford_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.ford_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ford_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.ford_check.setObjectName("ford_check")
        self.verticalLayout_7.addWidget(self.ford_check)
        self.tesla_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.tesla_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tesla_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.tesla_check.setObjectName("tesla_check")
        self.verticalLayout_7.addWidget(self.tesla_check)
        self.bmw_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.bmw_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bmw_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.bmw_check.setObjectName("bmw_check")
        self.verticalLayout_7.addWidget(self.bmw_check)
        self.cad_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.cad_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cad_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.cad_check.setObjectName("cad_check")
        self.verticalLayout_7.addWidget(self.cad_check)
        self.honda_check = QtWidgets.QCheckBox(self.brand_check_frame)
        self.honda_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.honda_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.honda_check.setObjectName("honda_check")
        self.verticalLayout_7.addWidget(self.honda_check)
        self.verticalLayout_4.addWidget(self.brand_check_frame)
        self.year_brand_dropdown.addItem(self.brand_title, "")
        self.year_title = QtWidgets.QWidget()
        self.year_title.setGeometry(QtCore.QRect(0, 0, 228, 443))
        self.year_title.setObjectName("year_title")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.year_title)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.year_frame = QtWidgets.QFrame(self.year_title)
        self.year_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.year_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.year_frame.setObjectName("year_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.year_frame)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.year_check = QtWidgets.QCheckBox(self.year_frame)
        self.year_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check.setObjectName("year_check")
        self.verticalLayout_11.addWidget(self.year_check)
        self.year_check1 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check1.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check1.setObjectName("year_check1")
        self.verticalLayout_11.addWidget(self.year_check1)
        self.year_check2 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check2.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check2.setObjectName("year_check2")
        self.verticalLayout_11.addWidget(self.year_check2)
        self.year_check3 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check3.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check3.setObjectName("year_check3")
        self.verticalLayout_11.addWidget(self.year_check3)
        self.year_check4 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check4.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check4.setObjectName("year_check4")
        self.verticalLayout_11.addWidget(self.year_check4)
        self.year_check5 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check5.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check5.setObjectName("year_check5")
        self.verticalLayout_11.addWidget(self.year_check5)
        self.year_check6 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check6.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check6.setObjectName("year_check6")
        self.verticalLayout_11.addWidget(self.year_check6)
        self.year_check7 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check7.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check7.setObjectName("year_check7")
        self.verticalLayout_11.addWidget(self.year_check7)
        self.year_check8 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check8.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check8.setObjectName("year_check8")
        self.verticalLayout_11.addWidget(self.year_check8)
        self.year_check9 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check9.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check9.setObjectName("year_check9")
        self.verticalLayout_11.addWidget(self.year_check9)
        self.year_check10 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check10.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check10.setObjectName("year_check10")
        self.verticalLayout_11.addWidget(self.year_check10)
        self.year_check11 = QtWidgets.QCheckBox(self.year_frame)
        self.year_check11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.year_check11.setStyleSheet("QCheckBox::indicator{ \n"
"    width:25px;\n"
"    height:25px; \n"
"    background-color:white;\n"
"    border-radius: 8px; \n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    spacing:15px;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-family: Open Sans; \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 108, 235)\n"
"}")
        self.year_check11.setObjectName("year_check11")
        self.verticalLayout_11.addWidget(self.year_check11)
        self.verticalLayout_8.addWidget(self.year_frame)
        self.year_brand_dropdown.addItem(self.year_title, "")
        self.verticalLayout_16.addWidget(self.year_brand_dropdown)
        self.verticalLayout_6.addWidget(self.drop_down_frame)
        self.verticalLayout_15.addWidget(self.inside_filter_frame)
        self.verticalLayout_2.addWidget(self.filter_frame)
        self.horizontalLayout.addWidget(self.left_main_frame)
        self.right_main_frame = QtWidgets.QFrame(self.background_frame)
        self.right_main_frame.setMaximumSize(QtCore.QSize(10000, 800))
        self.right_main_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.right_main_frame.setStyleSheet("QFrame{\n"
"    background-color: #27062D;\n"
"}")
        self.right_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_main_frame.setObjectName("right_main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.right_main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upper_frame = QtWidgets.QFrame(self.right_main_frame)
        self.upper_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.upper_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.upper_frame.setStyleSheet("QFrame{\n"
"    background-color: #27062D;\n"
"}")
        self.upper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upper_frame.setObjectName("upper_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.upper_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filter_button = QtWidgets.QPushButton(self.upper_frame)
        self.filter_button.setMinimumSize(QtCore.QSize(38, 38))
        self.filter_button.setSizeIncrement(QtCore.QSize(16, 16))
        self.filter_button.setBaseSize(QtCore.QSize(16, 16))
        self.filter_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filter_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(181, 84, 215);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(181, 84, 215,150);\n"
"}")
        self.filter_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/checkbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter_button.setIcon(icon)
        self.filter_button.setIconSize(QtCore.QSize(38, 38))
        self.filter_button.setObjectName("filter_button")
        self.horizontalLayout_2.addWidget(self.filter_button, 0, QtCore.Qt.AlignRight)
        self.search_bar = QtWidgets.QLineEdit(self.upper_frame)
        self.search_bar.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(144,104,140);\n"
"    border-radius: 8px;\n"
"    font-size: 30px;\n"
"    color:white    ;\n"
"    font-family: Open Sans;\n"
"}\n"
"\n"
"")
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_2.addWidget(self.search_bar)
        self.search_button = QtWidgets.QPushButton(self.upper_frame)
        self.search_button.setMinimumSize(QtCore.QSize(38, 38))
        self.search_button.setSizeIncrement(QtCore.QSize(16, 16))
        self.search_button.setBaseSize(QtCore.QSize(16, 16))
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(181, 84, 215);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(181, 84, 215,150);\n"
"}")
        self.search_button.setText("")
        self.search_button.setIconSize(QtCore.QSize(30, 30))
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_2.addWidget(self.search_button)
        self.refresh_button = QtWidgets.QPushButton(self.upper_frame)
        self.refresh_button.setMinimumSize(QtCore.QSize(38, 38))
        self.refresh_button.setSizeIncrement(QtCore.QSize(16, 16))
        self.refresh_button.setBaseSize(QtCore.QSize(16, 16))
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(181, 84, 215);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(181, 84, 215,150);\n"
"}")
        self.refresh_button.setText("")
        self.refresh_button.setIconSize(QtCore.QSize(32, 32))
        self.refresh_button.setObjectName("refresh_button")
        self.horizontalLayout_2.addWidget(self.refresh_button)
        self.quit_button = QtWidgets.QPushButton(self.upper_frame)
        self.quit_button.setMinimumSize(QtCore.QSize(16, 16))
        self.quit_button.setMaximumSize(QtCore.QSize(17, 17))
        self.quit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.quit_button.setAutoFillBackground(False)
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
        self.horizontalLayout_2.addWidget(self.quit_button, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.upper_frame)
        self.car_infor_frame = QtWidgets.QFrame(self.right_main_frame)
        self.car_infor_frame.setStyleSheet("QFrame{ \n"
"    background-color: rgb(140, 104, 152);\n"
"}")
        self.car_infor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.car_infor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.car_infor_frame.setObjectName("car_infor_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.car_infor_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cdt = QtWidgets.QTableWidget(self.car_infor_frame)
        self.cdt.setObjectName("cdt")
        self.cdt.setColumnCount(0)
        self.cdt.setRowCount(0)
        self.verticalLayout_3.addWidget(self.cdt)
        self.verticalLayout.addWidget(self.car_infor_frame)
        self.horizontalLayout.addWidget(self.right_main_frame)
        self.background_frame_2.addWidget(self.background_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.year_brand_dropdown.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Hbutton.setText(_translate("MainWindow", "UCR"))
        self.label.setText(_translate("MainWindow", "               FILTER"))
        self.filter_Button.setText(_translate("MainWindow", "Filter"))
        self.price_bar.setText(_translate("MainWindow", " PRICE"))
        self.price_label.setText(_translate("MainWindow", "$ 0"))
        self.miles_bar.setText(_translate("MainWindow", " MILES DRIVEN"))
        self.mile_label.setText(_translate("MainWindow", "0 Miles"))
        self.nis_check.setText(_translate("MainWindow", "Nissan"))
        self.lex_check.setText(_translate("MainWindow", "Lexus"))
        self.chev_check.setText(_translate("MainWindow", "Chevrolet"))
        self.ford_check.setText(_translate("MainWindow", "Ford"))
        self.tesla_check.setText(_translate("MainWindow", "Tesla"))
        self.bmw_check.setText(_translate("MainWindow", "BMW"))
        self.cad_check.setText(_translate("MainWindow", "Cadillac"))
        self.honda_check.setText(_translate("MainWindow", "Honda"))
        self.year_brand_dropdown.setItemText(self.year_brand_dropdown.indexOf(self.brand_title), _translate("MainWindow", "BRAND"))
        self.year_check.setText(_translate("MainWindow", "2000"))
        self.year_check1.setText(_translate("MainWindow", "2001"))
        self.year_check2.setText(_translate("MainWindow", "2002"))
        self.year_check3.setText(_translate("MainWindow", "2003"))
        self.year_check4.setText(_translate("MainWindow", "2004"))
        self.year_check5.setText(_translate("MainWindow", "2005"))
        self.year_check6.setText(_translate("MainWindow", "2006"))
        self.year_check7.setText(_translate("MainWindow", "2007"))
        self.year_check8.setText(_translate("MainWindow", "2008"))
        self.year_check9.setText(_translate("MainWindow", "2009"))
        self.year_check10.setText(_translate("MainWindow", "2010"))
        self.year_check11.setText(_translate("MainWindow", "2011"))
        self.year_brand_dropdown.setItemText(self.year_brand_dropdown.indexOf(self.year_title), _translate("MainWindow", "YEAR"))
