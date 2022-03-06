# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(709, 488)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color:#234E70;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_hello_dr = QLabel(self.centralwidget)
        self.label_hello_dr.setObjectName(u"label_hello_dr")
        self.label_hello_dr.setGeometry(QRect(200, 20, 301, 51))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_hello_dr.setFont(font)
        self.label_hello_dr.setStyleSheet(u"")
        self.label_hello_dr.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_hello_dr.setLineWidth(10)
        self.label_upcomingS = QLabel(self.centralwidget)
        self.label_upcomingS.setObjectName(u"label_upcomingS")
        self.label_upcomingS.setGeometry(QRect(10, 80, 691, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_upcomingS.setFont(font1)
        self.label_upcomingS.setStyleSheet(u"color: rgb(251, 248, 190);")
        self.tableWidget_S = QTableWidget(self.centralwidget)
        if (self.tableWidget_S.columnCount() < 4):
            self.tableWidget_S.setColumnCount(4)
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget_S.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget_S.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget_S.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget_S.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_S.setObjectName(u"tableWidget_S")
        self.tableWidget_S.setGeometry(QRect(125, 121, 461, 201))
        self.tableWidget_S.setStyleSheet(u"color: rgb(251, 248, 190);")
        self.tableWidget_S.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_S.verticalHeader().setStretchLastSection(False)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(540, 30, 141, 31))
        self.lcdNumber.setStyleSheet(u"QLCDNumber{\n"
"	border-color:#234E70;\n"
"\n"
"	background-color: rgb(100, 100, 100);\n"
"	color:#FCF6F5FF;\n"
"\n"
"}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 390, 671, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 0, 50, 0)
        self.add_newP = QPushButton(self.layoutWidget)
        self.add_newP.setObjectName(u"add_newP")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.add_newP.setFont(font3)
        self.add_newP.setStyleSheet(u"\n"
"color:#234E70;\n"
"background-color: rgb(251, 248, 190);")

        self.horizontalLayout.addWidget(self.add_newP)

        self.look_for_patient = QPushButton(self.layoutWidget)
        self.look_for_patient.setObjectName(u"look_for_patient")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.look_for_patient.sizePolicy().hasHeightForWidth())
        self.look_for_patient.setSizePolicy(sizePolicy)
        self.look_for_patient.setFont(font3)
        self.look_for_patient.setStyleSheet(u"color:#234E70;\n"
"background-color: rgb(251, 248, 190);")

        self.horizontalLayout.addWidget(self.look_for_patient)

        self.stats = QPushButton(self.layoutWidget)
        self.stats.setObjectName(u"stats")
        self.stats.setFont(font3)
        self.stats.setStyleSheet(u"color:#234E70;\n"
"background-color: rgb(251, 248, 190);")

        self.horizontalLayout.addWidget(self.stats)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_hello_dr.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_upcomingS.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic; color:#fbf8be;\">Upcoming Surgeries</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_S.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_S.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget_S.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem3 = self.tableWidget_S.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date of Procedure", None));
        self.add_newP.setText(QCoreApplication.translate("MainWindow", u"Add new Patient", None))
        self.look_for_patient.setText(QCoreApplication.translate("MainWindow", u"Look for a Patient", None))
        self.stats.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
    # retranslateUi

