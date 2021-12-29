# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lotfi/Documents/vs-code-projects/Video-Streaming-in-PyQt-uisng-OpenCV/video-streaming.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 468)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/video_streaming.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
" border: none;\n"
"background-color: transparent;\n"
"color: #fff;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #040f13;\n"
"}\n"
"#side_menu{\n"
"    background-color: #071e26;\n"
"    border-radius: 10px;\n"
"}\n"
"#top_bar{\n"
"    background-color: #071e26;\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMinimumSize(QtCore.QSize(0, 70))
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.top_bar)
        self.frame_3.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(45, 45))
        self.label.setMaximumSize(QtCore.QSize(45, 45))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/video_streaming.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.top_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.application_name_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.application_name_label.setFont(font)
        self.application_name_label.setAutoFillBackground(False)
        self.application_name_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.application_name_label.setObjectName("application_name_label")
        self.verticalLayout_5.addWidget(self.application_name_label)
        self.horizontalLayout_3.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.top_bar)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QFrame(self.frame_2)
        self.side_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.side_menu)
        self.frame.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color: rgb(59, 103, 128);\n"
"border: 2px solid blue;\n"
"border-radius: 7px;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.start_stop_btn = QtWidgets.QPushButton(self.frame)
        self.start_stop_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.start_stop_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.start_stop_btn.setStyleSheet("")
        self.start_stop_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/run_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_stop_btn.setIcon(icon1)
        self.start_stop_btn.setIconSize(QtCore.QSize(30, 30))
        self.start_stop_btn.setCheckable(True)
        self.start_stop_btn.setObjectName("start_stop_btn")
        self.verticalLayout_3.addWidget(self.start_stop_btn)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.side_menu, 0, QtCore.Qt.AlignLeft)
        self.body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.body)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.image_label = QtWidgets.QLabel(self.frame_6)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.verticalLayout_7.addWidget(self.image_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.body)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Streaming using OpenCV"))
        self.application_name_label.setText(_translate("MainWindow", "Video Streaming using OpenCV"))
import icons_rc
