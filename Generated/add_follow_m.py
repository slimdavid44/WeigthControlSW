# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_follow_m.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_follow_m(object):
    def setupUi(self, add_follow_m):
        if not add_follow_m.objectName():
            add_follow_m.setObjectName(u"add_follow_m")
        add_follow_m.resize(649, 527)
        add_follow_m.setStyleSheet(u"background-color:#234E70;\n"
"color: #FBF8BE;")
        self.centralwidget = QWidget(add_follow_m)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sumbit_button = QPushButton(self.centralwidget)
        self.sumbit_button.setObjectName(u"sumbit_button")
        self.sumbit_button.setGeometry(QRect(170, 420, 91, 31))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sumbit_button.setFont(font)
        self.sumbit_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.anoc_edit = QTextEdit(self.centralwidget)
        self.anoc_edit.setObjectName(u"anoc_edit")
        self.anoc_edit.setGeometry(QRect(360, 200, 271, 71))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        self.anoc_edit.setFont(font1)
        self.anoc_edit.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 170, 271, 21))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(430, 70, 135, 56))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.weight_label = QLabel(self.layoutWidget)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setFont(font2)
        self.weight_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.weight_label)

        self.weight_edit = QLineEdit(self.layoutWidget)
        self.weight_edit.setObjectName(u"weight_edit")
        self.weight_edit.setFont(font1)
        self.weight_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.weight_edit)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(31, 21, 551, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.layoutWidget1)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setFont(font2)
        self.title_label.setFrameShadow(QFrame.Plain)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title_label)

        self.name_lable = QLabel(self.layoutWidget1)
        self.name_lable.setObjectName(u"name_lable")
        self.name_lable.setFont(font2)
        self.name_lable.setFrameShadow(QFrame.Plain)
        self.name_lable.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.name_lable)

        self.cancel_button_2 = QPushButton(self.centralwidget)
        self.cancel_button_2.setObjectName(u"cancel_button_2")
        self.cancel_button_2.setGeometry(QRect(360, 420, 91, 31))
        self.cancel_button_2.setFont(font)
        self.cancel_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.add_m_calendarWidget = QCalendarWidget(self.centralwidget)
        self.add_m_calendarWidget.setObjectName(u"add_m_calendarWidget")
        self.add_m_calendarWidget.setGeometry(QRect(10, 140, 312, 183))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.add_m_calendarWidget.setFont(font3)
        self.add_m_calendarWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(199, 199, 199);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.add_m_calendarWidget.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(100, 100, 141, 16))
        self.date_label.setFont(font2)
        self.deat_label = QLabel(self.centralwidget)
        self.deat_label.setObjectName(u"deat_label")
        self.deat_label.setGeometry(QRect(42, 62, 109, 19))
        self.deat_label.setFont(font2)
        self.deat_label.setAlignment(Qt.AlignCenter)
        self.today_CB = QCheckBox(self.centralwidget)
        self.today_CB.setObjectName(u"today_CB")
        self.today_CB.setGeometry(QRect(190, 60, 78, 23))
        self.today_CB.setFont(font2)
        self.today_CB.setCheckable(True)
        add_follow_m.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(add_follow_m)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 649, 21))
        add_follow_m.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(add_follow_m)
        self.statusbar.setObjectName(u"statusbar")
        add_follow_m.setStatusBar(self.statusbar)

        self.retranslateUi(add_follow_m)

        QMetaObject.connectSlotsByName(add_follow_m)
    # setupUi

    def retranslateUi(self, add_follow_m):
        add_follow_m.setWindowTitle(QCoreApplication.translate("add_follow_m", u"MainWindow", None))
        self.sumbit_button.setText(QCoreApplication.translate("add_follow_m", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("add_follow_m", u"Anot.", None))
        self.weight_label.setText(QCoreApplication.translate("add_follow_m", u"Weight [kg]", None))
        self.title_label.setText(QCoreApplication.translate("add_follow_m", u"Add New Folow-Up Meeting For:", None))
        self.name_lable.setText("")
        self.cancel_button_2.setText(QCoreApplication.translate("add_follow_m", u"Cancel", None))
        self.date_label.setText("")
        self.deat_label.setText(QCoreApplication.translate("add_follow_m", u"Meeting Date", None))
        self.today_CB.setText(QCoreApplication.translate("add_follow_m", u"Today?", None))
    # retranslateUi

