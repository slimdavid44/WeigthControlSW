# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_P.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_P(object):
    def setupUi(self, add_P):
        if not add_P.objectName():
            add_P.setObjectName(u"add_P")
        add_P.resize(858, 499)
        add_P.setStyleSheet(u"background-color: rgb(35, 78, 112);\n"
"color: rgb(251, 248, 190);")
        self.submit_button = QPushButton(add_P)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(260, 430, 101, 23))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet(u"background-color: rgb(251, 248, 190);\n"
"color: rgb(35, 78, 112);")
        self.main_button = QPushButton(add_P)
        self.main_button.setObjectName(u"main_button")
        self.main_button.setGeometry(QRect(489, 430, 191, 23))
        self.main_button.setFont(font)
        self.main_button.setStyleSheet(u"background-color: rgb(251, 248, 190);\n"
"color: rgb(35, 78, 112);")
        self.layoutWidget = QWidget(add_P)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 50, 742, 341))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.name_edit = QLineEdit(self.layoutWidget)
        self.name_edit.setObjectName(u"name_edit")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        self.name_edit.setFont(font1)
        self.name_edit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(238, 238, 238);\n"
"}")

        self.gridLayout.addWidget(self.name_edit, 1, 1, 1, 1)

        self.origen_l = QLabel(self.layoutWidget)
        self.origen_l.setObjectName(u"origen_l")
        self.origen_l.setFont(font)

        self.gridLayout.addWidget(self.origen_l, 1, 2, 1, 1)

        self.date_l = QLabel(self.layoutWidget)
        self.date_l.setObjectName(u"date_l")
        self.date_l.setFont(font)

        self.gridLayout.addWidget(self.date_l, 5, 0, 1, 1)

        self.age_edit = QLineEdit(self.layoutWidget)
        self.age_edit.setObjectName(u"age_edit")
        self.age_edit.setFont(font1)
        self.age_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.age_edit, 0, 3, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 5, 2, 1, 1)

        self.Email_l = QLabel(self.layoutWidget)
        self.Email_l.setObjectName(u"Email_l")
        self.Email_l.setFont(font)

        self.gridLayout.addWidget(self.Email_l, 3, 0, 1, 1)

        self.waiting_for_date_CB = QCheckBox(self.layoutWidget)
        self.waiting_for_date_CB.setObjectName(u"waiting_for_date_CB")
        self.waiting_for_date_CB.setFont(font)

        self.gridLayout.addWidget(self.waiting_for_date_CB, 5, 1, 1, 1)

        self.origen_comboBox = QComboBox(self.layoutWidget)
        self.origen_comboBox.setObjectName(u"origen_comboBox")
        self.origen_comboBox.setFont(font1)
        self.origen_comboBox.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.origen_comboBox, 1, 3, 1, 1)

        self.height_l = QLabel(self.layoutWidget)
        self.height_l.setObjectName(u"height_l")
        self.height_l.setFont(font)

        self.gridLayout.addWidget(self.height_l, 3, 2, 1, 1)

        self.height_edit = QLineEdit(self.layoutWidget)
        self.height_edit.setObjectName(u"height_edit")
        self.height_edit.setFont(font1)
        self.height_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.height_edit, 3, 3, 1, 1)

        self.Phone_l = QLabel(self.layoutWidget)
        self.Phone_l.setObjectName(u"Phone_l")
        self.Phone_l.setFont(font)

        self.gridLayout.addWidget(self.Phone_l, 2, 0, 1, 1)

        self.other_diseases_CB = QCheckBox(self.layoutWidget)
        self.other_diseases_CB.setObjectName(u"other_diseases_CB")
        self.other_diseases_CB.setFont(font1)

        self.gridLayout.addWidget(self.other_diseases_CB, 5, 3, 1, 1)

        self.herinia_L = QLabel(self.layoutWidget)
        self.herinia_L.setObjectName(u"herinia_L")
        self.herinia_L.setFont(font)

        self.gridLayout.addWidget(self.herinia_L, 4, 2, 1, 1)

        self.id_l = QLabel(self.layoutWidget)
        self.id_l.setObjectName(u"id_l")
        self.id_l.setFont(font)

        self.gridLayout.addWidget(self.id_l, 0, 0, 1, 1)

        self.weight_edit = QLineEdit(self.layoutWidget)
        self.weight_edit.setObjectName(u"weight_edit")
        self.weight_edit.setFont(font1)
        self.weight_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.weight_edit, 2, 3, 1, 1)

        self.phone_edit = QLineEdit(self.layoutWidget)
        self.phone_edit.setObjectName(u"phone_edit")
        self.phone_edit.setFont(font1)
        self.phone_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.phone_edit, 2, 1, 1, 1)

        self.procedure_comboBox = QComboBox(self.layoutWidget)
        self.procedure_comboBox.setObjectName(u"procedure_comboBox")
        self.procedure_comboBox.setFont(font1)
        self.procedure_comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(238, 238, 238);\n"
"color:rgb(0, 0, 0)\n"
"}")

        self.gridLayout.addWidget(self.procedure_comboBox, 4, 1, 1, 1)

        self.weight_l = QLabel(self.layoutWidget)
        self.weight_l.setObjectName(u"weight_l")
        self.weight_l.setFont(font)

        self.gridLayout.addWidget(self.weight_l, 2, 2, 1, 1)

        self.hernia_CB = QCheckBox(self.layoutWidget)
        self.hernia_CB.setObjectName(u"hernia_CB")
        self.hernia_CB.setFont(font1)

        self.gridLayout.addWidget(self.hernia_CB, 4, 3, 1, 1)

        self.id_edit = QLineEdit(self.layoutWidget)
        self.id_edit.setObjectName(u"id_edit")
        self.id_edit.setFont(font1)
        self.id_edit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(238, 238, 238);\n"
"}")

        self.gridLayout.addWidget(self.id_edit, 0, 1, 1, 1)

        self.Procedimiento_l = QLabel(self.layoutWidget)
        self.Procedimiento_l.setObjectName(u"Procedimiento_l")
        self.Procedimiento_l.setFont(font)

        self.gridLayout.addWidget(self.Procedimiento_l, 4, 0, 1, 1)

        self.name_l = QLabel(self.layoutWidget)
        self.name_l.setObjectName(u"name_l")
        self.name_l.setFont(font)

        self.gridLayout.addWidget(self.name_l, 1, 0, 1, 1)

        self.email_edit = QLineEdit(self.layoutWidget)
        self.email_edit.setObjectName(u"email_edit")
        self.email_edit.setFont(font1)
        self.email_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.email_edit, 3, 1, 1, 1)

        self.age_l = QLabel(self.layoutWidget)
        self.age_l.setObjectName(u"age_l")
        self.age_l.setFont(font)

        self.gridLayout.addWidget(self.age_l, 0, 2, 1, 1)

        self.calendarWidget = QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.calendarWidget.setFont(font2)
        self.calendarWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(199, 199, 199);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.calendarWidget.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.calendarWidget.setGridVisible(True)

        self.gridLayout.addWidget(self.calendarWidget, 6, 1, 1, 2)

        self.add_new_titel = QLabel(add_P)
        self.add_new_titel.setObjectName(u"add_new_titel")
        self.add_new_titel.setGeometry(QRect(70, 10, 741, 31))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.add_new_titel.setFont(font3)

        self.retranslateUi(add_P)

        QMetaObject.connectSlotsByName(add_P)
    # setupUi

    def retranslateUi(self, add_P):
        add_P.setWindowTitle(QCoreApplication.translate("add_P", u"Form", None))
        self.submit_button.setText(QCoreApplication.translate("add_P", u"Submit", None))
        self.main_button.setText(QCoreApplication.translate("add_P", u"Returm to Main Window", None))
        self.origen_l.setText(QCoreApplication.translate("add_P", u"Origen", None))
        self.date_l.setText(QCoreApplication.translate("add_P", u"Date Of Surgery  ", None))
        self.label.setText(QCoreApplication.translate("add_P", u"Other Diseases   ", None))
        self.Email_l.setText(QCoreApplication.translate("add_P", u"E-mail", None))
        self.waiting_for_date_CB.setText(QCoreApplication.translate("add_P", u"Waitnig For Date", None))
        self.height_l.setText(QCoreApplication.translate("add_P", u"Height [m]", None))
        self.Phone_l.setText(QCoreApplication.translate("add_P", u"Phone", None))
        self.other_diseases_CB.setText(QCoreApplication.translate("add_P", u"Is there other diseases?", None))
        self.herinia_L.setText(QCoreApplication.translate("add_P", u"Hernia", None))
        self.id_l.setText(QCoreApplication.translate("add_P", u"ID", None))
        self.weight_l.setText(QCoreApplication.translate("add_P", u"Weight [kg]", None))
        self.hernia_CB.setText(QCoreApplication.translate("add_P", u"Is there a hernia?", None))
        self.Procedimiento_l.setText(QCoreApplication.translate("add_P", u"Procedimiento", None))
        self.name_l.setText(QCoreApplication.translate("add_P", u"Name", None))
        self.age_l.setText(QCoreApplication.translate("add_P", u"Date Of Birth", None))
        self.add_new_titel.setText(QCoreApplication.translate("add_P", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Add New Patient</span></p></body></html>", None))
    # retranslateUi

