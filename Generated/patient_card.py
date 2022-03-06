# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_card.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Patient_card(object):
    def setupUi(self, Patient_card):
        if not Patient_card.objectName():
            Patient_card.setObjectName(u"Patient_card")
        Patient_card.resize(1302, 654)
        self.centralwidget = QWidget(Patient_card)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1331, 1971))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(251, 248, 190, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(35, 78, 112, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(160, 160, 160, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(251, 248, 190, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush4 = QBrush(QColor(251, 248, 190, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush5 = QBrush(QColor(100, 100, 100, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        brush6 = QBrush(QColor(102, 102, 102, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(251, 248, 190, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.tabWidget.setPalette(palette)
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(35, 78, 112);\n"
"")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.tab_7.setFont(font1)
        self.first_titel_2 = QLabel(self.tab_7)
        self.first_titel_2.setObjectName(u"first_titel_2")
        self.first_titel_2.setGeometry(QRect(0, 0, 1281, 31))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.first_titel_2.setFont(font2)
        self.first_titel_2.setAlignment(Qt.AlignCenter)
        self.L_surgery_deatils = QLabel(self.tab_7)
        self.L_surgery_deatils.setObjectName(u"L_surgery_deatils")
        self.L_surgery_deatils.setGeometry(QRect(370, 70, 261, 31))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.L_surgery_deatils.setFont(font3)
        self.L_surgery_deatils.setAlignment(Qt.AlignCenter)
        self.L_first_details = QLabel(self.tab_7)
        self.L_first_details.setObjectName(u"L_first_details")
        self.L_first_details.setGeometry(QRect(37, 71, 211, 31))
        self.L_first_details.setFont(font3)
        self.L_first_details.setAlignment(Qt.AlignCenter)
        self.L_BMI25 = QLabel(self.tab_7)
        self.L_BMI25.setObjectName(u"L_BMI25")
        self.L_BMI25.setGeometry(QRect(59, 259, 111, 31))
        self.L_BMI25.setFont(font3)
        self.L_BMI25.setAlignment(Qt.AlignCenter)
        self.L_BMI23 = QLabel(self.tab_7)
        self.L_BMI23.setObjectName(u"L_BMI23")
        self.L_BMI23.setGeometry(QRect(59, 388, 111, 30))
        self.L_BMI23.setFont(font3)
        self.L_BMI23.setAlignment(Qt.AlignCenter)
        self.main_button = QPushButton(self.tab_7)
        self.main_button.setObjectName(u"main_button")
        self.main_button.setGeometry(QRect(740, 530, 211, 31))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.main_button.setFont(font4)
        self.main_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.search_button = QPushButton(self.tab_7)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(440, 530, 211, 31))
        self.search_button.setFont(font4)
        self.search_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.Update_button_T1 = QPushButton(self.tab_7)
        self.Update_button_T1.setObjectName(u"Update_button_T1")
        self.Update_button_T1.setGeometry(QRect(370, 430, 81, 31))
        self.Update_button_T1.setFont(font4)
        self.Update_button_T1.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.submit_Button_T1 = QPushButton(self.tab_7)
        self.submit_Button_T1.setObjectName(u"submit_Button_T1")
        self.submit_Button_T1.setGeometry(QRect(510, 430, 81, 31))
        self.submit_Button_T1.setFont(font4)
        self.submit_Button_T1.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.delete_button_T1 = QPushButton(self.tab_7)
        self.delete_button_T1.setObjectName(u"delete_button_T1")
        self.delete_button_T1.setGeometry(QRect(650, 430, 81, 31))
        self.delete_button_T1.setFont(font4)
        self.delete_button_T1.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.show_comp_button = QPushButton(self.tab_7)
        self.show_comp_button.setObjectName(u"show_comp_button")
        self.show_comp_button.setGeometry(QRect(470, 230, 121, 31))
        self.show_comp_button.setFont(font4)
        self.show_comp_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.Comp_label = QLabel(self.tab_7)
        self.Comp_label.setObjectName(u"Comp_label")
        self.Comp_label.setGeometry(QRect(340, 270, 401, 21))
        self.Comp_label.setFont(font3)
        self.Comp_label.setAlignment(Qt.AlignCenter)
        self.calendarWidget_P_card = QCalendarWidget(self.tab_7)
        self.calendarWidget_P_card.setObjectName(u"calendarWidget_P_card")
        self.calendarWidget_P_card.setGeometry(QRect(990, 122, 301, 191))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(9)
        self.calendarWidget_P_card.setFont(font5)
        self.calendarWidget_P_card.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(199, 199, 199);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.calendarWidget_P_card.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.calendarWidget_P_card.setGridVisible(True)
        self.Cancel_Update_button_T1 = QPushButton(self.tab_7)
        self.Cancel_Update_button_T1.setObjectName(u"Cancel_Update_button_T1")
        self.Cancel_Update_button_T1.setGeometry(QRect(340, 470, 141, 31))
        self.Cancel_Update_button_T1.setFont(font4)
        self.Cancel_Update_button_T1.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.hide_comp_button = QPushButton(self.tab_7)
        self.hide_comp_button.setObjectName(u"hide_comp_button")
        self.hide_comp_button.setGeometry(QRect(470, 230, 121, 31))
        self.hide_comp_button.setFont(font4)
        self.hide_comp_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.Waiting_date_check = QCheckBox(self.tab_7)
        self.Waiting_date_check.setObjectName(u"Waiting_date_check")
        self.Waiting_date_check.setGeometry(QRect(1060, 100, 171, 20))
        self.Waiting_date_check.setFont(font4)
        self.Waiting_date_check.setLayoutDirection(Qt.LeftToRight)
        self.Waiting_date_check.setStyleSheet(u"QCheckBox{color: #FBF8BE;}")
        self.Waiting_date_check.setTristate(False)
        self.Update_date_check = QCheckBox(self.tab_7)
        self.Update_date_check.setObjectName(u"Update_date_check")
        self.Update_date_check.setGeometry(QRect(1060, 80, 171, 20))
        self.Update_date_check.setFont(font4)
        self.Update_date_check.setStyleSheet(u"QCheckBox{color: #FBF8BE;}")
        self.layoutWidget = QWidget(self.tab_7)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 37, 1141, 29))
        self.Personal_Layout = QHBoxLayout(self.layoutWidget)
        self.Personal_Layout.setObjectName(u"Personal_Layout")
        self.Personal_Layout.setContentsMargins(0, 0, 0, 0)
        self.L_id_6 = QLabel(self.layoutWidget)
        self.L_id_6.setObjectName(u"L_id_6")
        self.L_id_6.setFont(font4)

        self.Personal_Layout.addWidget(self.L_id_6)

        self.Id_label_edit_T1 = QLabel(self.layoutWidget)
        self.Id_label_edit_T1.setObjectName(u"Id_label_edit_T1")
        self.Id_label_edit_T1.setMinimumSize(QSize(154, 0))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(13)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.Id_label_edit_T1.setFont(font6)
        self.Id_label_edit_T1.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.Personal_Layout.addWidget(self.Id_label_edit_T1)

        self.L_name = QLabel(self.layoutWidget)
        self.L_name.setObjectName(u"L_name")
        self.L_name.setFont(font4)

        self.Personal_Layout.addWidget(self.L_name)

        self.name_edit = QLineEdit(self.layoutWidget)
        self.name_edit.setObjectName(u"name_edit")
        font7 = QFont()
        font7.setFamily(u"Calibri")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.name_edit.setFont(font7)
        self.name_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.name_edit.setReadOnly(True)

        self.Personal_Layout.addWidget(self.name_edit)

        self.L_email = QLabel(self.layoutWidget)
        self.L_email.setObjectName(u"L_email")
        self.L_email.setFont(font4)

        self.Personal_Layout.addWidget(self.L_email)

        self.email_edit = QLineEdit(self.layoutWidget)
        self.email_edit.setObjectName(u"email_edit")
        self.email_edit.setFont(font7)
        self.email_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.email_edit.setReadOnly(True)

        self.Personal_Layout.addWidget(self.email_edit)

        self.L_phone = QLabel(self.layoutWidget)
        self.L_phone.setObjectName(u"L_phone")
        self.L_phone.setFont(font4)

        self.Personal_Layout.addWidget(self.L_phone)

        self.phone_edit = QLineEdit(self.layoutWidget)
        self.phone_edit.setObjectName(u"phone_edit")
        self.phone_edit.setFont(font7)
        self.phone_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.phone_edit.setReadOnly(True)

        self.Personal_Layout.addWidget(self.phone_edit)

        self.L_Date_of_birth = QLabel(self.layoutWidget)
        self.L_Date_of_birth.setObjectName(u"L_Date_of_birth")
        self.L_Date_of_birth.setFont(font4)

        self.Personal_Layout.addWidget(self.L_Date_of_birth)

        self.Date_of_birth_edit = QLineEdit(self.layoutWidget)
        self.Date_of_birth_edit.setObjectName(u"Date_of_birth_edit")
        self.Date_of_birth_edit.setFont(font7)
        self.Date_of_birth_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.Date_of_birth_edit.setReadOnly(True)

        self.Personal_Layout.addWidget(self.Date_of_birth_edit)

        self.layoutWidget1 = QWidget(self.tab_7)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 110, 224, 166))
        self.First_details_Layout = QFormLayout(self.layoutWidget1)
        self.First_details_Layout.setObjectName(u"First_details_Layout")
        self.First_details_Layout.setContentsMargins(0, 0, 0, 0)
        self.L_age = QLabel(self.layoutWidget1)
        self.L_age.setObjectName(u"L_age")
        self.L_age.setFont(font4)

        self.First_details_Layout.setWidget(0, QFormLayout.LabelRole, self.L_age)

        self.age_lable_edit = QLabel(self.layoutWidget1)
        self.age_lable_edit.setObjectName(u"age_lable_edit")
        self.age_lable_edit.setFont(font6)
        self.age_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.First_details_Layout.setWidget(0, QFormLayout.FieldRole, self.age_lable_edit)

        self.L_Origen = QLabel(self.layoutWidget1)
        self.L_Origen.setObjectName(u"L_Origen")
        self.L_Origen.setFont(font4)

        self.First_details_Layout.setWidget(1, QFormLayout.LabelRole, self.L_Origen)

        self.Origen_CB = QComboBox(self.layoutWidget1)
        self.Origen_CB.setObjectName(u"Origen_CB")
        self.Origen_CB.setEnabled(False)
        self.Origen_CB.setFont(font7)
        self.Origen_CB.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);")

        self.First_details_Layout.setWidget(1, QFormLayout.FieldRole, self.Origen_CB)

        self.L_height = QLabel(self.layoutWidget1)
        self.L_height.setObjectName(u"L_height")
        self.L_height.setFont(font4)

        self.First_details_Layout.setWidget(2, QFormLayout.LabelRole, self.L_height)

        self.height_edit = QLineEdit(self.layoutWidget1)
        self.height_edit.setObjectName(u"height_edit")
        self.height_edit.setFont(font7)
        self.height_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.height_edit.setReadOnly(True)

        self.First_details_Layout.setWidget(2, QFormLayout.FieldRole, self.height_edit)

        self.L_weight = QLabel(self.layoutWidget1)
        self.L_weight.setObjectName(u"L_weight")
        self.L_weight.setFont(font4)

        self.First_details_Layout.setWidget(3, QFormLayout.LabelRole, self.L_weight)

        self.weight_edit = QLineEdit(self.layoutWidget1)
        self.weight_edit.setObjectName(u"weight_edit")
        self.weight_edit.setFont(font7)
        self.weight_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.weight_edit.setReadOnly(True)

        self.First_details_Layout.setWidget(3, QFormLayout.FieldRole, self.weight_edit)

        self.L_BMI = QLabel(self.layoutWidget1)
        self.L_BMI.setObjectName(u"L_BMI")
        self.L_BMI.setFont(font4)

        self.First_details_Layout.setWidget(4, QFormLayout.LabelRole, self.L_BMI)

        self.bmi_lable_edit = QLabel(self.layoutWidget1)
        self.bmi_lable_edit.setObjectName(u"bmi_lable_edit")
        self.bmi_lable_edit.setFont(font7)
        self.bmi_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.First_details_Layout.setWidget(4, QFormLayout.FieldRole, self.bmi_lable_edit)

        self.layoutWidget2 = QWidget(self.tab_7)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(370, 110, 267, 144))
        self.Surgery_details_layout = QFormLayout(self.layoutWidget2)
        self.Surgery_details_layout.setObjectName(u"Surgery_details_layout")
        self.Surgery_details_layout.setContentsMargins(0, 0, 0, 0)
        self.L_date = QLabel(self.layoutWidget2)
        self.L_date.setObjectName(u"L_date")
        self.L_date.setFont(font4)

        self.Surgery_details_layout.setWidget(0, QFormLayout.LabelRole, self.L_date)

        self.date_lable_edit_2 = QLabel(self.layoutWidget2)
        self.date_lable_edit_2.setObjectName(u"date_lable_edit_2")
        self.date_lable_edit_2.setFont(font6)
        self.date_lable_edit_2.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.Surgery_details_layout.setWidget(0, QFormLayout.FieldRole, self.date_lable_edit_2)

        self.L_type = QLabel(self.layoutWidget2)
        self.L_type.setObjectName(u"L_type")
        self.L_type.setFont(font4)

        self.Surgery_details_layout.setWidget(1, QFormLayout.LabelRole, self.L_type)

        self.Type_CB = QComboBox(self.layoutWidget2)
        self.Type_CB.setObjectName(u"Type_CB")
        self.Type_CB.setEnabled(False)
        self.Type_CB.setFont(font7)
        self.Type_CB.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);")

        self.Surgery_details_layout.setWidget(1, QFormLayout.FieldRole, self.Type_CB)

        self.L_hernia = QLabel(self.layoutWidget2)
        self.L_hernia.setObjectName(u"L_hernia")
        self.L_hernia.setFont(font4)

        self.Surgery_details_layout.setWidget(2, QFormLayout.LabelRole, self.L_hernia)

        self.L_comp = QLabel(self.layoutWidget2)
        self.L_comp.setObjectName(u"L_comp")
        self.L_comp.setFont(font4)

        self.Surgery_details_layout.setWidget(3, QFormLayout.LabelRole, self.L_comp)

        self.hernia_checkBox = QCheckBox(self.layoutWidget2)
        self.hernia_checkBox.setObjectName(u"hernia_checkBox")
        self.hernia_checkBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hernia_checkBox.sizePolicy().hasHeightForWidth())
        self.hernia_checkBox.setSizePolicy(sizePolicy1)
        self.hernia_checkBox.setMinimumSize(QSize(0, 28))
        self.hernia_checkBox.setMaximumSize(QSize(119, 13))
        font8 = QFont()
        font8.setPointSize(15)
        font8.setBold(True)
        font8.setWeight(75)
        self.hernia_checkBox.setFont(font8)
        self.hernia_checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.hernia_checkBox.setIconSize(QSize(40, 40))

        self.Surgery_details_layout.setWidget(2, QFormLayout.FieldRole, self.hernia_checkBox)

        self.Complications_checkBox = QCheckBox(self.layoutWidget2)
        self.Complications_checkBox.setObjectName(u"Complications_checkBox")
        self.Complications_checkBox.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Complications_checkBox.sizePolicy().hasHeightForWidth())
        self.Complications_checkBox.setSizePolicy(sizePolicy1)
        self.Complications_checkBox.setMinimumSize(QSize(0, 28))
        self.Complications_checkBox.setMaximumSize(QSize(119, 13))
        self.Complications_checkBox.setFont(font8)
        self.Complications_checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Complications_checkBox.setIconSize(QSize(40, 40))

        self.Surgery_details_layout.setWidget(3, QFormLayout.FieldRole, self.Complications_checkBox)

        self.layoutWidget3 = QWidget(self.tab_7)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 300, 191, 83))
        self.BMI25_layout = QFormLayout(self.layoutWidget3)
        self.BMI25_layout.setObjectName(u"BMI25_layout")
        self.BMI25_layout.setContentsMargins(0, 0, 0, 0)
        self.L_Ideal_w25 = QLabel(self.layoutWidget3)
        self.L_Ideal_w25.setObjectName(u"L_Ideal_w25")
        self.L_Ideal_w25.setFont(font4)

        self.BMI25_layout.setWidget(0, QFormLayout.LabelRole, self.L_Ideal_w25)

        self.bmi25_lable_edit = QLabel(self.layoutWidget3)
        self.bmi25_lable_edit.setObjectName(u"bmi25_lable_edit")
        self.bmi25_lable_edit.setFont(font6)
        self.bmi25_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.BMI25_layout.setWidget(0, QFormLayout.FieldRole, self.bmi25_lable_edit)

        self.L_over25 = QLabel(self.layoutWidget3)
        self.L_over25.setObjectName(u"L_over25")
        self.L_over25.setFont(font4)

        self.BMI25_layout.setWidget(1, QFormLayout.LabelRole, self.L_over25)

        self.over25_lable_edit = QLabel(self.layoutWidget3)
        self.over25_lable_edit.setObjectName(u"over25_lable_edit")
        self.over25_lable_edit.setFont(font6)
        self.over25_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.BMI25_layout.setWidget(1, QFormLayout.FieldRole, self.over25_lable_edit)

        self.L_overP25 = QLabel(self.layoutWidget3)
        self.L_overP25.setObjectName(u"L_overP25")
        self.L_overP25.setFont(font4)

        self.BMI25_layout.setWidget(2, QFormLayout.LabelRole, self.L_overP25)

        self.over25per_lable_edit = QLabel(self.layoutWidget3)
        self.over25per_lable_edit.setObjectName(u"over25per_lable_edit")
        self.over25per_lable_edit.setFont(font6)
        self.over25per_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.BMI25_layout.setWidget(2, QFormLayout.FieldRole, self.over25per_lable_edit)

        self.layoutWidget4 = QWidget(self.tab_7)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(30, 420, 191, 83))
        self.BMI23_layout = QFormLayout(self.layoutWidget4)
        self.BMI23_layout.setObjectName(u"BMI23_layout")
        self.BMI23_layout.setContentsMargins(0, 0, 0, 0)
        self.L_Ideal_w23 = QLabel(self.layoutWidget4)
        self.L_Ideal_w23.setObjectName(u"L_Ideal_w23")
        self.L_Ideal_w23.setFont(font4)

        self.BMI23_layout.setWidget(0, QFormLayout.LabelRole, self.L_Ideal_w23)

        self.bmi23_lable_edit = QLabel(self.layoutWidget4)
        self.bmi23_lable_edit.setObjectName(u"bmi23_lable_edit")
        self.bmi23_lable_edit.setFont(font6)
        self.bmi23_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.BMI23_layout.setWidget(0, QFormLayout.FieldRole, self.bmi23_lable_edit)

        self.L_over23 = QLabel(self.layoutWidget4)
        self.L_over23.setObjectName(u"L_over23")
        self.L_over23.setFont(font4)

        self.BMI23_layout.setWidget(1, QFormLayout.LabelRole, self.L_over23)

        self.over23_lable_edit = QLabel(self.layoutWidget4)
        self.over23_lable_edit.setObjectName(u"over23_lable_edit")
        self.over23_lable_edit.setFont(font6)
        self.over23_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.BMI23_layout.setWidget(1, QFormLayout.FieldRole, self.over23_lable_edit)

        self.L_overP23 = QLabel(self.layoutWidget4)
        self.L_overP23.setObjectName(u"L_overP23")
        self.L_overP23.setFont(font4)

        self.BMI23_layout.setWidget(2, QFormLayout.LabelRole, self.L_overP23)

        self.over23per_lable_edit = QLabel(self.layoutWidget4)
        self.over23per_lable_edit.setObjectName(u"over23per_lable_edit")
        self.over23per_lable_edit.setFont(font6)
        self.over23per_lable_edit.setStyleSheet(u"color: rgb(251, 248, 190);")

        self.BMI23_layout.setWidget(2, QFormLayout.FieldRole, self.over23per_lable_edit)

        self.layoutWidget5 = QWidget(self.tab_7)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(340, 300, 401, 91))
        self.Comp_layout = QFormLayout(self.layoutWidget5)
        self.Comp_layout.setObjectName(u"Comp_layout")
        self.Comp_layout.setContentsMargins(0, 0, 0, 0)
        self.L_during_comp = QLabel(self.layoutWidget5)
        self.L_during_comp.setObjectName(u"L_during_comp")
        self.L_during_comp.setFont(font4)

        self.Comp_layout.setWidget(0, QFormLayout.LabelRole, self.L_during_comp)

        self.during_comp_edit = QLineEdit(self.layoutWidget5)
        self.during_comp_edit.setObjectName(u"during_comp_edit")
        self.during_comp_edit.setFont(font7)
        self.during_comp_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.during_comp_edit.setReadOnly(True)

        self.Comp_layout.setWidget(0, QFormLayout.FieldRole, self.during_comp_edit)

        self.L_post_comp = QLabel(self.layoutWidget5)
        self.L_post_comp.setObjectName(u"L_post_comp")
        self.L_post_comp.setFont(font4)

        self.Comp_layout.setWidget(1, QFormLayout.LabelRole, self.L_post_comp)

        self.post_comp_edit = QLineEdit(self.layoutWidget5)
        self.post_comp_edit.setObjectName(u"post_comp_edit")
        self.post_comp_edit.setFont(font7)
        self.post_comp_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")

        self.Comp_layout.setWidget(1, QFormLayout.FieldRole, self.post_comp_edit)

        self.L_additional_surgery = QLabel(self.layoutWidget5)
        self.L_additional_surgery.setObjectName(u"L_additional_surgery")
        self.L_additional_surgery.setFont(font4)

        self.Comp_layout.setWidget(2, QFormLayout.LabelRole, self.L_additional_surgery)

        self.additional_edit = QLineEdit(self.layoutWidget5)
        self.additional_edit.setObjectName(u"additional_edit")
        self.additional_edit.setFont(font7)
        self.additional_edit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.additional_edit.setReadOnly(True)

        self.Comp_layout.setWidget(2, QFormLayout.FieldRole, self.additional_edit)

        self.go_to_diseases_button = QPushButton(self.tab_7)
        self.go_to_diseases_button.setObjectName(u"go_to_diseases_button")
        self.go_to_diseases_button.setGeometry(QRect(820, 370, 141, 31))
        self.go_to_diseases_button.setFont(font4)
        self.go_to_diseases_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.diseases_list = QListWidget(self.tab_7)
        self.diseases_list.setObjectName(u"diseases_list")
        self.diseases_list.setGeometry(QRect(810, 120, 161, 231))
        font9 = QFont()
        font9.setFamily(u"Calibri")
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(50)
        self.diseases_list.setFont(font9)
        self.diseases_list.setStyleSheet(u"color: rgb(251, 248, 190);")
        self.delete_d = QPushButton(self.tab_7)
        self.delete_d.setObjectName(u"delete_d")
        self.delete_d.setGeometry(QRect(820, 410, 141, 31))
        self.delete_d.setFont(font4)
        self.delete_d.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.label_5 = QLabel(self.tab_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(817, 90, 151, 20))
        self.tabWidget.addTab(self.tab_7, "")
        self.layoutWidget3.raise_()
        self.layoutWidget3.raise_()
        self.layoutWidget3.raise_()
        self.layoutWidget3.raise_()
        self.first_titel_2.raise_()
        self.L_first_details.raise_()
        self.L_BMI25.raise_()
        self.L_BMI23.raise_()
        self.main_button.raise_()
        self.search_button.raise_()
        self.layoutWidget3.raise_()
        self.Update_button_T1.raise_()
        self.submit_Button_T1.raise_()
        self.delete_button_T1.raise_()
        self.layoutWidget3.raise_()
        self.show_comp_button.raise_()
        self.Comp_label.raise_()
        self.calendarWidget_P_card.raise_()
        self.L_surgery_deatils.raise_()
        self.Cancel_Update_button_T1.raise_()
        self.hide_comp_button.raise_()
        self.Waiting_date_check.raise_()
        self.Update_date_check.raise_()
        self.go_to_diseases_button.raise_()
        self.diseases_list.raise_()
        self.delete_d.raise_()
        self.label_5.raise_()
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.progress_table = QTableWidget(self.tab_8)
        if (self.progress_table.columnCount() < 7):
            self.progress_table.setColumnCount(7)
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setBold(True)
        font10.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font10);
        self.progress_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font10);
        self.progress_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font10);
        self.progress_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font10);
        self.progress_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font10);
        self.progress_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font10);
        self.progress_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font10);
        self.progress_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.progress_table.setObjectName(u"progress_table")
        self.progress_table.setGeometry(QRect(235, 70, 841, 171))
        sizePolicy.setHeightForWidth(self.progress_table.sizePolicy().hasHeightForWidth())
        self.progress_table.setSizePolicy(sizePolicy)
        self.progress_table.setFont(font7)
        self.progress_table.setLayoutDirection(Qt.LeftToRight)
        self.progress_table.setAutoFillBackground(False)
        self.progress_table.setStyleSheet(u"color: rgb(251, 248, 190);")
        self.progress_table.setFrameShadow(QFrame.Sunken)
        self.progress_table.horizontalHeader().setCascadingSectionResizes(False)
        self.progress_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.progress_table.horizontalHeader().setStretchLastSection(True)
        self.progress_table.verticalHeader().setVisible(False)
        self.progress_table.verticalHeader().setCascadingSectionResizes(False)
        self.progress_table.verticalHeader().setMinimumSectionSize(23)
        self.progress_table.verticalHeader().setDefaultSectionSize(30)
        self.progress_table.verticalHeader().setHighlightSections(True)
        self.progress_table.verticalHeader().setProperty("showSortIndicator", True)
        self.Anot_text = QTextEdit(self.tab_8)
        self.Anot_text.setObjectName(u"Anot_text")
        self.Anot_text.setGeometry(QRect(340, 340, 601, 71))
        font11 = QFont()
        font11.setFamily(u"Calibri")
        font11.setPointSize(14)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.Anot_text.setFont(font11)
        self.main_button_T2 = QPushButton(self.tab_8)
        self.main_button_T2.setObjectName(u"main_button_T2")
        self.main_button_T2.setGeometry(QRect(360, 482, 201, 41))
        self.main_button_T2.setFont(font4)
        self.main_button_T2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.search_button_T2 = QPushButton(self.tab_8)
        self.search_button_T2.setObjectName(u"search_button_T2")
        self.search_button_T2.setGeometry(QRect(690, 480, 181, 41))
        self.search_button_T2.setFont(font4)
        self.search_button_T2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.label_3 = QLabel(self.tab_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 305, 601, 31))
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.tab_8)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(3, 0, 1291, 31))
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.Add_Button_T2 = QPushButton(self.tab_8)
        self.Add_Button_T2.setObjectName(u"Add_Button_T2")
        self.Add_Button_T2.setGeometry(QRect(416, 250, 91, 31))
        self.Add_Button_T2.setFont(font4)
        self.Add_Button_T2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.Update_button_T2 = QPushButton(self.tab_8)
        self.Update_button_T2.setObjectName(u"Update_button_T2")
        self.Update_button_T2.setGeometry(QRect(591, 250, 91, 31))
        self.Update_button_T2.setFont(font4)
        self.Update_button_T2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.Delete_button_T2 = QPushButton(self.tab_8)
        self.Delete_button_T2.setObjectName(u"Delete_button_T2")
        self.Delete_button_T2.setGeometry(QRect(764, 250, 91, 31))
        self.Delete_button_T2.setFont(font4)
        self.Delete_button_T2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.layoutWidget6 = QWidget(self.tab_8)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(120, 40, 1051, 22))
        self.Personal_layout2 = QHBoxLayout(self.layoutWidget6)
        self.Personal_layout2.setObjectName(u"Personal_layout2")
        self.Personal_layout2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Personal_layout2.setContentsMargins(0, 0, 0, 0)
        self.L_id_T2 = QLabel(self.layoutWidget6)
        self.L_id_T2.setObjectName(u"L_id_T2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.L_id_T2.sizePolicy().hasHeightForWidth())
        self.L_id_T2.setSizePolicy(sizePolicy2)
        font12 = QFont()
        font12.setFamily(u"Calibri")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setItalic(False)
        font12.setWeight(75)
        self.L_id_T2.setFont(font12)

        self.Personal_layout2.addWidget(self.L_id_T2)

        self.Id_label_edit_T2 = QLabel(self.layoutWidget6)
        self.Id_label_edit_T2.setObjectName(u"Id_label_edit_T2")
        self.Id_label_edit_T2.setFont(font9)

        self.Personal_layout2.addWidget(self.Id_label_edit_T2)

        self.label_2 = QLabel(self.layoutWidget6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font12)

        self.Personal_layout2.addWidget(self.label_2)

        self.name_label_edit_T2 = QLabel(self.layoutWidget6)
        self.name_label_edit_T2.setObjectName(u"name_label_edit_T2")
        self.name_label_edit_T2.setFont(font9)

        self.Personal_layout2.addWidget(self.name_label_edit_T2)

        self.L_email_T2 = QLabel(self.layoutWidget6)
        self.L_email_T2.setObjectName(u"L_email_T2")
        sizePolicy2.setHeightForWidth(self.L_email_T2.sizePolicy().hasHeightForWidth())
        self.L_email_T2.setSizePolicy(sizePolicy2)
        self.L_email_T2.setFont(font12)

        self.Personal_layout2.addWidget(self.L_email_T2)

        self.email_label_edit_T2 = QLabel(self.layoutWidget6)
        self.email_label_edit_T2.setObjectName(u"email_label_edit_T2")
        self.email_label_edit_T2.setFont(font9)

        self.Personal_layout2.addWidget(self.email_label_edit_T2)

        self.L_phone_T2 = QLabel(self.layoutWidget6)
        self.L_phone_T2.setObjectName(u"L_phone_T2")
        sizePolicy2.setHeightForWidth(self.L_phone_T2.sizePolicy().hasHeightForWidth())
        self.L_phone_T2.setSizePolicy(sizePolicy2)
        self.L_phone_T2.setFont(font12)

        self.Personal_layout2.addWidget(self.L_phone_T2)

        self.phone_label_edit_T2 = QLabel(self.layoutWidget6)
        self.phone_label_edit_T2.setObjectName(u"phone_label_edit_T2")
        self.phone_label_edit_T2.setFont(font9)

        self.Personal_layout2.addWidget(self.phone_label_edit_T2)

        self.L_Age_T2 = QLabel(self.layoutWidget6)
        self.L_Age_T2.setObjectName(u"L_Age_T2")
        sizePolicy2.setHeightForWidth(self.L_Age_T2.sizePolicy().hasHeightForWidth())
        self.L_Age_T2.setSizePolicy(sizePolicy2)
        self.L_Age_T2.setFont(font12)

        self.Personal_layout2.addWidget(self.L_Age_T2)

        self.age_label_edit_T2 = QLabel(self.layoutWidget6)
        self.age_label_edit_T2.setObjectName(u"age_label_edit_T2")
        self.age_label_edit_T2.setFont(font9)

        self.Personal_layout2.addWidget(self.age_label_edit_T2)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget_2 = QWidget(self.tab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(100, 40, 1161, 25))
        self.Personal_layout2_2 = QHBoxLayout(self.layoutWidget_2)
        self.Personal_layout2_2.setObjectName(u"Personal_layout2_2")
        self.Personal_layout2_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Personal_layout2_2.setContentsMargins(0, 0, 0, 0)
        self.L_id_T3 = QLabel(self.layoutWidget_2)
        self.L_id_T3.setObjectName(u"L_id_T3")
        sizePolicy2.setHeightForWidth(self.L_id_T3.sizePolicy().hasHeightForWidth())
        self.L_id_T3.setSizePolicy(sizePolicy2)
        self.L_id_T3.setFont(font12)

        self.Personal_layout2_2.addWidget(self.L_id_T3)

        self.Id_label_edit_T3 = QLabel(self.layoutWidget_2)
        self.Id_label_edit_T3.setObjectName(u"Id_label_edit_T3")
        self.Id_label_edit_T3.setFont(font9)

        self.Personal_layout2_2.addWidget(self.Id_label_edit_T3)

        self.L_name_T3 = QLabel(self.layoutWidget_2)
        self.L_name_T3.setObjectName(u"L_name_T3")
        sizePolicy2.setHeightForWidth(self.L_name_T3.sizePolicy().hasHeightForWidth())
        self.L_name_T3.setSizePolicy(sizePolicy2)
        self.L_name_T3.setFont(font12)

        self.Personal_layout2_2.addWidget(self.L_name_T3)

        self.name_label_edit_T3 = QLabel(self.layoutWidget_2)
        self.name_label_edit_T3.setObjectName(u"name_label_edit_T3")
        self.name_label_edit_T3.setFont(font9)

        self.Personal_layout2_2.addWidget(self.name_label_edit_T3)

        self.L_email_T3 = QLabel(self.layoutWidget_2)
        self.L_email_T3.setObjectName(u"L_email_T3")
        sizePolicy2.setHeightForWidth(self.L_email_T3.sizePolicy().hasHeightForWidth())
        self.L_email_T3.setSizePolicy(sizePolicy2)
        self.L_email_T3.setFont(font12)

        self.Personal_layout2_2.addWidget(self.L_email_T3)

        self.email_label_edit_T3 = QLabel(self.layoutWidget_2)
        self.email_label_edit_T3.setObjectName(u"email_label_edit_T3")
        self.email_label_edit_T3.setFont(font9)

        self.Personal_layout2_2.addWidget(self.email_label_edit_T3)

        self.L_phone_T3 = QLabel(self.layoutWidget_2)
        self.L_phone_T3.setObjectName(u"L_phone_T3")
        sizePolicy2.setHeightForWidth(self.L_phone_T3.sizePolicy().hasHeightForWidth())
        self.L_phone_T3.setSizePolicy(sizePolicy2)
        self.L_phone_T3.setFont(font12)

        self.Personal_layout2_2.addWidget(self.L_phone_T3)

        self.phone_label_edit_T3 = QLabel(self.layoutWidget_2)
        self.phone_label_edit_T3.setObjectName(u"phone_label_edit_T3")
        self.phone_label_edit_T3.setFont(font9)

        self.Personal_layout2_2.addWidget(self.phone_label_edit_T3)

        self.L_Age_T3 = QLabel(self.layoutWidget_2)
        self.L_Age_T3.setObjectName(u"L_Age_T3")
        sizePolicy2.setHeightForWidth(self.L_Age_T3.sizePolicy().hasHeightForWidth())
        self.L_Age_T3.setSizePolicy(sizePolicy2)
        self.L_Age_T3.setFont(font12)

        self.Personal_layout2_2.addWidget(self.L_Age_T3)

        self.age_label_edit_T3 = QLabel(self.layoutWidget_2)
        self.age_label_edit_T3.setObjectName(u"age_label_edit_T3")
        self.age_label_edit_T3.setFont(font9)

        self.Personal_layout2_2.addWidget(self.age_label_edit_T3)

        self.main_button_T3 = QPushButton(self.tab)
        self.main_button_T3.setObjectName(u"main_button_T3")
        self.main_button_T3.setGeometry(QRect(310, 510, 241, 41))
        font13 = QFont()
        font13.setFamily(u"Calibri")
        font13.setPointSize(16)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setWeight(75)
        self.main_button_T3.setFont(font13)
        self.main_button_T3.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.search_button_T3 = QPushButton(self.tab)
        self.search_button_T3.setObjectName(u"search_button_T3")
        self.search_button_T3.setGeometry(QRect(600, 510, 181, 41))
        self.search_button_T3.setFont(font13)
        self.search_button_T3.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(3, 0, 1281, 41))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.save_button = QPushButton(self.tab)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(830, 510, 131, 41))
        self.save_button.setFont(font13)
        self.save_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.tabWidget.addTab(self.tab, "")
        Patient_card.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Patient_card)
        self.statusbar.setObjectName(u"statusbar")
        Patient_card.setStatusBar(self.statusbar)

        self.retranslateUi(Patient_card)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Patient_card)
    # setupUi

    def retranslateUi(self, Patient_card):
        Patient_card.setWindowTitle(QCoreApplication.translate("Patient_card", u"MainWindow", None))
        self.first_titel_2.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Personal Information</span></p></body></html>", None))
        self.L_surgery_deatils.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Surgery details</span></p></body></html>", None))
        self.L_first_details.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">First meeting details</span></p></body></html>", None))
        self.L_BMI25.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">BMI 25</span></p></body></html>", None))
        self.L_BMI23.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">BMI 23</span></p></body></html>", None))
        self.main_button.setText(QCoreApplication.translate("Patient_card", u"Return to Main Window", None))
        self.search_button.setText(QCoreApplication.translate("Patient_card", u"Return to Search", None))
        self.Update_button_T1.setText(QCoreApplication.translate("Patient_card", u"Update", None))
        self.submit_Button_T1.setText(QCoreApplication.translate("Patient_card", u"Submit", None))
        self.delete_button_T1.setText(QCoreApplication.translate("Patient_card", u"Delete", None))
        self.show_comp_button.setText(QCoreApplication.translate("Patient_card", u"Show Comp", None))
        self.Comp_label.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Complications</span></p></body></html>", None))
        self.Cancel_Update_button_T1.setText(QCoreApplication.translate("Patient_card", u"Cancel Update", None))
        self.hide_comp_button.setText(QCoreApplication.translate("Patient_card", u"Hide Comp", None))
        self.Waiting_date_check.setText(QCoreApplication.translate("Patient_card", u"Waiting for date?", None))
        self.Update_date_check.setText(QCoreApplication.translate("Patient_card", u"Update Date?", None))
        self.L_id_6.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">ID</span></p></body></html>", None))
        self.Id_label_edit_T1.setText("")
        self.L_name.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Name</span></p></body></html>", None))
        self.L_email.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">E-mail</span></p></body></html>", None))
        self.L_phone.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Phone</span></p></body></html>", None))
        self.L_Date_of_birth.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Date Of Birth</span></p></body></html>", None))
        self.L_age.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Age</span></p></body></html>", None))
        self.age_lable_edit.setText("")
        self.L_Origen.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Origen</span></p></body></html>", None))
        self.L_height.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Height [m]</span></p></body></html>", None))
        self.L_weight.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Weight [kg]</span></p></body></html>", None))
        self.L_BMI.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">BMI</span></p></body></html>", None))
        self.bmi_lable_edit.setText("")
        self.L_date.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Date</span></p></body></html>", None))
        self.date_lable_edit_2.setText("")
        self.L_type.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Type</span></p></body></html>", None))
        self.L_hernia.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Repair of a hernia</span></p></body></html>", None))
        self.L_comp.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Complications</span></p></body></html>", None))
        self.hernia_checkBox.setText("")
        self.Complications_checkBox.setText("")
        self.L_Ideal_w25.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Ideal weight [kg]</span></p></body></html>", None))
        self.bmi25_lable_edit.setText("")
        self.L_over25.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Overweight [kg]</span></p></body></html>", None))
        self.over25_lable_edit.setText("")
        self.L_overP25.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Overweight [%]</span></p></body></html>", None))
        self.over25per_lable_edit.setText("")
        self.L_Ideal_w23.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Ideal weight [kg]</span></p></body></html>", None))
        self.bmi23_lable_edit.setText("")
        self.L_over23.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Overweight [kg]</span></p></body></html>", None))
        self.over23_lable_edit.setText("")
        self.L_overP23.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Overweight  [%]</span></p></body></html>", None))
        self.over23per_lable_edit.setText("")
        self.L_during_comp.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">During-comp</span></p></body></html>", None))
        self.L_post_comp.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Post-comp </span></p></body></html>", None))
        self.L_additional_surgery.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Additional surgeries</span></p></body></html>", None))
        self.go_to_diseases_button.setText(QCoreApplication.translate("Patient_card", u"Add Diseases", None))
        self.delete_d.setText(QCoreApplication.translate("Patient_card", u"Delete Diseases", None))
        self.label_5.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#fbf8be;\">Other Diseases</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("Patient_card", u"Personal Info", None))
        ___qtablewidgetitem = self.progress_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Patient_card", u"Date of meeting", None));
        ___qtablewidgetitem1 = self.progress_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Patient_card", u"Difference [months]", None));
        ___qtablewidgetitem2 = self.progress_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Patient_card", u"Current weight", None));
        ___qtablewidgetitem3 = self.progress_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Patient_card", u"BMI", None));
        ___qtablewidgetitem4 = self.progress_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Patient_card", u"Weight lost [kg]", None));
        ___qtablewidgetitem5 = self.progress_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Patient_card", u"Weight lost [%]", None));
        ___qtablewidgetitem6 = self.progress_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Patient_card", u"Anot.", None));
        self.main_button_T2.setText(QCoreApplication.translate("Patient_card", u"Return to main window", None))
        self.search_button_T2.setText(QCoreApplication.translate("Patient_card", u"Return to search", None))
        self.label_3.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Anot.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Follow-Up Information</span></p></body></html>", None))
        self.Add_Button_T2.setText(QCoreApplication.translate("Patient_card", u"ADD", None))
        self.Update_button_T2.setText(QCoreApplication.translate("Patient_card", u"UPDATE", None))
        self.Delete_button_T2.setText(QCoreApplication.translate("Patient_card", u"DELETE", None))
        self.L_id_T2.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">ID</span></p></body></html>", None))
        self.Id_label_edit_T2.setText("")
        self.label_2.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Name</span></p></body></html>", None))
        self.name_label_edit_T2.setText("")
        self.L_email_T2.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">E-mail</span></p></body></html>", None))
        self.email_label_edit_T2.setText("")
        self.L_phone_T2.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Phone</span></p></body></html>", None))
        self.phone_label_edit_T2.setText("")
        self.L_Age_T2.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Age</span></p></body></html>", None))
        self.age_label_edit_T2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("Patient_card", u"Follow-up Info", None))
        self.L_id_T3.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">ID</span></p></body></html>", None))
        self.Id_label_edit_T3.setText("")
        self.L_name_T3.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Name</span></p></body></html>", None))
        self.name_label_edit_T3.setText("")
        self.L_email_T3.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">E-mail</span></p></body></html>", None))
        self.email_label_edit_T3.setText("")
        self.L_phone_T3.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Phone</span></p></body></html>", None))
        self.phone_label_edit_T3.setText("")
        self.L_Age_T3.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Age</span></p></body></html>", None))
        self.age_label_edit_T3.setText("")
        self.main_button_T3.setText(QCoreApplication.translate("Patient_card", u"Return to Main Window", None))
        self.search_button_T3.setText(QCoreApplication.translate("Patient_card", u"Return to Search", None))
        self.label_4.setText(QCoreApplication.translate("Patient_card", u"<html><head/><body><p><span style=\" color:#fbf8be;\">Follow-Up Graphs</span></p></body></html>", None))
        self.save_button.setText(QCoreApplication.translate("Patient_card", u"Save Pic", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Patient_card", u"Patient Graphs", None))
    # retranslateUi

