# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_FU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_update_FU(object):
    def setupUi(self, update_FU):
        if not update_FU.objectName():
            update_FU.setObjectName(u"update_FU")
        update_FU.resize(635, 542)
        update_FU.setStyleSheet(u"background-color:#234E70;\n"
"color: #FBF8BE;")
        self.centralwidget = QWidget(update_FU)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 170, 241, 21))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.cancel_button_2 = QPushButton(self.centralwidget)
        self.cancel_button_2.setObjectName(u"cancel_button_2")
        self.cancel_button_2.setGeometry(QRect(360, 430, 91, 31))
        self.cancel_button_2.setFont(font)
        self.cancel_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(410, 90, 135, 59))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.weight_label_2 = QLabel(self.layoutWidget)
        self.weight_label_2.setObjectName(u"weight_label_2")
        self.weight_label_2.setFont(font)
        self.weight_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.weight_label_2)

        self.weight_edit_2 = QLineEdit(self.layoutWidget)
        self.weight_edit_2.setObjectName(u"weight_edit_2")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        self.weight_edit_2.setFont(font1)
        self.weight_edit_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.weight_edit_2)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(21, 31, 551, 28))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.title_label_2 = QLabel(self.layoutWidget_2)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setFont(font)
        self.title_label_2.setFrameShadow(QFrame.Plain)
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.title_label_2)

        self.name_label = QLabel(self.layoutWidget_2)
        self.name_label.setObjectName(u"name_label")
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.name_label.setFont(font2)
        self.name_label.setFrameShadow(QFrame.Plain)
        self.name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.name_label)

        self.anoc_edit = QTextEdit(self.centralwidget)
        self.anoc_edit.setObjectName(u"anoc_edit")
        self.anoc_edit.setGeometry(QRect(360, 200, 241, 111))
        self.anoc_edit.setFont(font1)
        self.anoc_edit.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")
        self.sumbit_button = QPushButton(self.centralwidget)
        self.sumbit_button.setObjectName(u"sumbit_button")
        self.sumbit_button.setGeometry(QRect(170, 430, 91, 31))
        self.sumbit_button.setFont(font)
        self.sumbit_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.update_fu_calendarWidget = QCalendarWidget(self.centralwidget)
        self.update_fu_calendarWidget.setObjectName(u"update_fu_calendarWidget")
        self.update_fu_calendarWidget.setGeometry(QRect(10, 170, 312, 183))
        self.update_fu_calendarWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(199, 199, 199);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.update_fu_calendarWidget.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(70, 120, 175, 19))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.date_label.setFont(font3)
        self.date_label.setAlignment(Qt.AlignCenter)
        self.today_CB_3 = QCheckBox(self.centralwidget)
        self.today_CB_3.setObjectName(u"today_CB_3")
        self.today_CB_3.setGeometry(QRect(200, 78, 78, 31))
        self.today_CB_3.setFont(font)
        self.deat_label_3 = QLabel(self.centralwidget)
        self.deat_label_3.setObjectName(u"deat_label_3")
        self.deat_label_3.setGeometry(QRect(38, 78, 121, 31))
        self.deat_label_3.setFont(font)
        self.deat_label_3.setAlignment(Qt.AlignCenter)
        update_FU.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(update_FU)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 635, 21))
        update_FU.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(update_FU)
        self.statusbar.setObjectName(u"statusbar")
        update_FU.setStatusBar(self.statusbar)

        self.retranslateUi(update_FU)

        QMetaObject.connectSlotsByName(update_FU)
    # setupUi

    def retranslateUi(self, update_FU):
        update_FU.setWindowTitle(QCoreApplication.translate("update_FU", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("update_FU", u"Anot.", None))
        self.cancel_button_2.setText(QCoreApplication.translate("update_FU", u"Cancel", None))
        self.weight_label_2.setText(QCoreApplication.translate("update_FU", u"Weight [kg]", None))
        self.title_label_2.setText(QCoreApplication.translate("update_FU", u"Update folow-Up meeting for:", None))
        self.name_label.setText("")
        self.sumbit_button.setText(QCoreApplication.translate("update_FU", u"Submit", None))
        self.date_label.setText("")
        self.today_CB_3.setText(QCoreApplication.translate("update_FU", u"Today?", None))
        self.deat_label_3.setText(QCoreApplication.translate("update_FU", u"Meeting Date", None))
    # retranslateUi

