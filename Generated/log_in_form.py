# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_log_in_form(object):
    def setupUi(self, log_in_form):
        if not log_in_form.objectName():
            log_in_form.setObjectName(u"log_in_form")
        log_in_form.resize(443, 213)
        log_in_form.setStyleSheet(u"background-color:#234E70;\n"
"color:#FBF8BE;")
        self.welcome_label = QLabel(log_in_form)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(9, 9, 413, 42))
        font = QFont()
        font.setFamily(u"Garamond")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.welcome_label.setFont(font)
        self.welcome_label.setLayoutDirection(Qt.LeftToRight)
        self.welcome_label.setStyleSheet(u"font: italic 28pt \"Garamond\";")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.log_in_lable = QLabel(log_in_form)
        self.log_in_lable.setObjectName(u"log_in_lable")
        self.log_in_lable.setGeometry(QRect(9, 62, 411, 25))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.log_in_lable.setFont(font1)
        self.log_in_lable.setAlignment(Qt.AlignCenter)
        self.login_button = QPushButton(log_in_form)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(150, 170, 141, 32))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.login_button.setFont(font2)
        self.login_button.setAutoFillBackground(False)
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.login_button.setAutoDefault(False)
        self.login_button.setFlat(False)
        self.layoutWidget = QWidget(log_in_form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 100, 242, 56))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.user_label = QLabel(self.layoutWidget)
        self.user_label.setObjectName(u"user_label")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        self.user_label.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.user_label)

        self.user_edit = QLineEdit(self.layoutWidget)
        self.user_edit.setObjectName(u"user_edit")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(10)
        self.user_edit.setFont(font4)
        self.user_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0,0,0);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.user_edit)

        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")
        font5 = QFont()
        font5.setPointSize(12)
        self.password_label.setFont(font5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.password_label)

        self.password_edit = QLineEdit(self.layoutWidget)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setFont(font4)
        self.password_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0,0,0)\n"
"}\n"
"")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_edit)


        self.retranslateUi(log_in_form)

        self.login_button.setDefault(False)


        QMetaObject.connectSlotsByName(log_in_form)
    # setupUi

    def retranslateUi(self, log_in_form):
        log_in_form.setWindowTitle(QCoreApplication.translate("log_in_form", u"Form", None))
        self.welcome_label.setText(QCoreApplication.translate("log_in_form", u"<html><head/><body><p><span style=\" font-weight:600; color:#fbf8be;\">Welcome Dr. Rami Mikler</span></p></body></html>", None))
        self.log_in_lable.setText(QCoreApplication.translate("log_in_form", u"<html><head/><body><p><span style=\" font-size:16pt; color:#fbf8be;\">Plaese Login</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.login_button.setToolTip(QCoreApplication.translate("log_in_form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.login_button.setText(QCoreApplication.translate("log_in_form", u"Login", None))
        self.user_label.setText(QCoreApplication.translate("log_in_form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#fbf8be;\">User Name</span></p></body></html>", None))
        self.password_label.setText(QCoreApplication.translate("log_in_form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#fbf8be;\">Password</span></p></body></html>", None))
    # retranslateUi

