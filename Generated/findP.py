# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'findP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_findP(object):
    def setupUi(self, findP):
        if not findP.objectName():
            findP.setObjectName(u"findP")
        findP.resize(421, 568)
        palette = QPalette()
        brush = QBrush(QColor(251, 248, 190, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(35, 78, 112, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(251, 248, 190, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(251, 248, 190, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(251, 248, 190, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        findP.setPalette(palette)
        findP.setStyleSheet(u"background-color: rgb(35, 78, 112);\n"
"color: rgb(251, 248, 190);")
        self.centralwidget = QWidget(findP)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table_P = QTableWidget(self.centralwidget)
        self.table_P.setObjectName(u"table_P")
        self.table_P.setGeometry(QRect(45, 160, 361, 192))
        self.table_P.setStyleSheet(u"color: rgb(251, 248, 190);")
        self.table_P.horizontalHeader().setStretchLastSection(True)
        self.table_P.verticalHeader().setStretchLastSection(False)
        self.main_Button = QPushButton(self.centralwidget)
        self.main_Button.setObjectName(u"main_Button")
        self.main_Button.setGeometry(QRect(120, 440, 201, 51))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_Button.setFont(font)
        self.main_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.select_Button = QPushButton(self.centralwidget)
        self.select_Button.setObjectName(u"select_Button")
        self.select_Button.setGeometry(QRect(120, 370, 201, 51))
        palette1 = QPalette()
        brush5 = QBrush(QColor(30, 39, 97, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        brush6 = QBrush(QColor(30, 39, 97, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush7 = QBrush(QColor(30, 39, 97, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush8 = QBrush(QColor(30, 39, 97, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.select_Button.setPalette(palette1)
        self.select_Button.setFont(font)
        self.select_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 30, 278, 91))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.L_id = QLabel(self.layoutWidget)
        self.L_id.setObjectName(u"L_id")
        self.L_id.setFont(font)

        self.verticalLayout.addWidget(self.L_id)

        self.lineEdit_id = QLineEdit(self.layoutWidget)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_id)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.L_name = QLabel(self.layoutWidget)
        self.L_name.setObjectName(u"L_name")
        self.L_name.setFont(font)

        self.verticalLayout_2.addWidget(self.L_name)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_name)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.pushButton_submit = QPushButton(self.layoutWidget)
        self.pushButton_submit.setObjectName(u"pushButton_submit")
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_submit, 1, 0, 1, 2)

        findP.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(findP)
        self.statusbar.setObjectName(u"statusbar")
        findP.setStatusBar(self.statusbar)

        self.retranslateUi(findP)

        QMetaObject.connectSlotsByName(findP)
    # setupUi

    def retranslateUi(self, findP):
        findP.setWindowTitle(QCoreApplication.translate("findP", u"find Patient", None))
        self.main_Button.setText(QCoreApplication.translate("findP", u"Return to Main Window", None))
        self.select_Button.setText(QCoreApplication.translate("findP", u"Select Patient", None))
        self.L_id.setText(QCoreApplication.translate("findP", u"<html><head/><body><p align=\"center\">Search by id</p></body></html>", None))
        self.L_name.setText(QCoreApplication.translate("findP", u"<html><head/><body><p align=\"center\">Search by Name</p></body></html>", None))
        self.pushButton_submit.setText(QCoreApplication.translate("findP", u"Search", None))
    # retranslateUi

