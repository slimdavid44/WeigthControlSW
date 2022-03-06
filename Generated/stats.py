# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Stats(object):
    def setupUi(self, Stats):
        if not Stats.objectName():
            Stats.setObjectName(u"Stats")
        Stats.resize(1558, 692)
        self.centralwidget = QWidget(Stats)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1561, 681))
        self.tabWidget.setStyleSheet(u"background-color:#234E70;\n"
"\n"
"color:#FBF8BE;\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.return_to_main_button = QPushButton(self.tab)
        self.return_to_main_button.setObjectName(u"return_to_main_button")
        self.return_to_main_button.setGeometry(QRect(830, 600, 231, 41))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.return_to_main_button.setFont(font)
        self.return_to_main_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.save_pic_button1 = QPushButton(self.tab)
        self.save_pic_button1.setObjectName(u"save_pic_button1")
        self.save_pic_button1.setEnabled(True)
        self.save_pic_button1.setGeometry(QRect(540, 600, 131, 41))
        self.save_pic_button1.setFont(font)
        self.save_pic_button1.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.save_pic_button1.setCheckable(False)
        self.save_pic_button1.setChecked(False)
        self.titel_Tab1 = QLabel(self.tab)
        self.titel_Tab1.setObjectName(u"titel_Tab1")
        self.titel_Tab1.setGeometry(QRect(310, 10, 901, 41))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.titel_Tab1.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.return_to_main_button_2 = QPushButton(self.tab_2)
        self.return_to_main_button_2.setObjectName(u"return_to_main_button_2")
        self.return_to_main_button_2.setGeometry(QRect(830, 600, 231, 41))
        self.return_to_main_button_2.setFont(font)
        self.return_to_main_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.save_pic_button_2 = QPushButton(self.tab_2)
        self.save_pic_button_2.setObjectName(u"save_pic_button_2")
        self.save_pic_button_2.setGeometry(QRect(540, 600, 131, 41))
        self.save_pic_button_2.setFont(font)
        self.save_pic_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.titel_tab2 = QLabel(self.tab_2)
        self.titel_tab2.setObjectName(u"titel_tab2")
        self.titel_tab2.setGeometry(QRect(310, 10, 901, 41))
        self.titel_tab2.setFont(font1)
        self.range_of_years_comboBox = QComboBox(self.tab_2)
        self.range_of_years_comboBox.setObjectName(u"range_of_years_comboBox")
        self.range_of_years_comboBox.setGeometry(QRect(1400, 180, 131, 22))
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1382, 140, 161, 21))
        self.update_tab2 = QPushButton(self.tab_2)
        self.update_tab2.setObjectName(u"update_tab2")
        self.update_tab2.setGeometry(QRect(1410, 220, 101, 31))
        self.update_tab2.setFont(font)
        self.update_tab2.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.return_to_main_button_3 = QPushButton(self.tab_3)
        self.return_to_main_button_3.setObjectName(u"return_to_main_button_3")
        self.return_to_main_button_3.setGeometry(QRect(800, 600, 231, 41))
        self.return_to_main_button_3.setFont(font)
        self.return_to_main_button_3.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.save_pic_button_3 = QPushButton(self.tab_3)
        self.save_pic_button_3.setObjectName(u"save_pic_button_3")
        self.save_pic_button_3.setGeometry(QRect(510, 600, 131, 41))
        self.save_pic_button_3.setFont(font)
        self.save_pic_button_3.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.titel_tab2_2 = QLabel(self.tab_3)
        self.titel_tab2_2.setObjectName(u"titel_tab2_2")
        self.titel_tab2_2.setGeometry(QRect(280, 10, 901, 41))
        self.titel_tab2_2.setFont(font1)
        self.Obesity_grade_label = QLabel(self.tab_3)
        self.Obesity_grade_label.setObjectName(u"Obesity_grade_label")
        self.Obesity_grade_label.setGeometry(QRect(160, 80, 71, 21))
        self.Age_groups_label = QLabel(self.tab_3)
        self.Age_groups_label.setObjectName(u"Age_groups_label")
        self.Age_groups_label.setGeometry(QRect(300, 80, 71, 21))
        self.Procedure_label = QLabel(self.tab_3)
        self.Procedure_label.setObjectName(u"Procedure_label")
        self.Procedure_label.setGeometry(QRect(500, 80, 71, 21))
        self.Months_after_label = QLabel(self.tab_3)
        self.Months_after_label.setObjectName(u"Months_after_label")
        self.Months_after_label.setGeometry(QRect(750, 90, 171, 21))
        self.Obesity_grade_comboBox = QComboBox(self.tab_3)
        self.Obesity_grade_comboBox.setObjectName(u"Obesity_grade_comboBox")
        self.Obesity_grade_comboBox.setGeometry(QRect(160, 110, 91, 22))
        self.Age_groups_comboBox = QComboBox(self.tab_3)
        self.Age_groups_comboBox.setObjectName(u"Age_groups_comboBox")
        self.Age_groups_comboBox.setGeometry(QRect(290, 110, 81, 22))
        self.Procedure_comboBox = QComboBox(self.tab_3)
        self.Procedure_comboBox.setObjectName(u"Procedure_comboBox")
        self.Procedure_comboBox.setGeometry(QRect(490, 110, 81, 22))
        self.Months_after_comboBox = QComboBox(self.tab_3)
        self.Months_after_comboBox.setObjectName(u"Months_after_comboBox")
        self.Months_after_comboBox.setGeometry(QRect(770, 110, 81, 22))
        self.update_tab3 = QPushButton(self.tab_3)
        self.update_tab3.setObjectName(u"update_tab3")
        self.update_tab3.setGeometry(QRect(1000, 110, 75, 23))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.Age_groups_label_2 = QLabel(self.tab_4)
        self.Age_groups_label_2.setObjectName(u"Age_groups_label_2")
        self.Age_groups_label_2.setGeometry(QRect(370, 80, 71, 21))
        self.save_pic_button_4 = QPushButton(self.tab_4)
        self.save_pic_button_4.setObjectName(u"save_pic_button_4")
        self.save_pic_button_4.setGeometry(QRect(580, 600, 131, 41))
        self.save_pic_button_4.setFont(font)
        self.save_pic_button_4.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.Obesity_grade_comboBox_tab4 = QComboBox(self.tab_4)
        self.Obesity_grade_comboBox_tab4.setObjectName(u"Obesity_grade_comboBox_tab4")
        self.Obesity_grade_comboBox_tab4.setGeometry(QRect(230, 110, 91, 22))
        self.titel_tab2_3 = QLabel(self.tab_4)
        self.titel_tab2_3.setObjectName(u"titel_tab2_3")
        self.titel_tab2_3.setGeometry(QRect(350, 10, 901, 41))
        self.titel_tab2_3.setFont(font1)
        self.Procedure_label_2 = QLabel(self.tab_4)
        self.Procedure_label_2.setObjectName(u"Procedure_label_2")
        self.Procedure_label_2.setGeometry(QRect(570, 80, 71, 21))
        self.update_tab4 = QPushButton(self.tab_4)
        self.update_tab4.setObjectName(u"update_tab4")
        self.update_tab4.setGeometry(QRect(1070, 110, 75, 23))
        self.return_to_main_button_4 = QPushButton(self.tab_4)
        self.return_to_main_button_4.setObjectName(u"return_to_main_button_4")
        self.return_to_main_button_4.setGeometry(QRect(870, 600, 231, 41))
        self.return_to_main_button_4.setFont(font)
        self.return_to_main_button_4.setStyleSheet(u"QPushButton{\n"
"	background-color: #FBF8BE;\n"
"\n"
"   color:#1E2761;\n"
"}")
        self.Age_groups_comboBox_tab4 = QComboBox(self.tab_4)
        self.Age_groups_comboBox_tab4.setObjectName(u"Age_groups_comboBox_tab4")
        self.Age_groups_comboBox_tab4.setGeometry(QRect(360, 110, 81, 22))
        self.Obesity_grade_label_2 = QLabel(self.tab_4)
        self.Obesity_grade_label_2.setObjectName(u"Obesity_grade_label_2")
        self.Obesity_grade_label_2.setGeometry(QRect(230, 80, 71, 21))
        self.Procedure_comboBox_tab4 = QComboBox(self.tab_4)
        self.Procedure_comboBox_tab4.setObjectName(u"Procedure_comboBox_tab4")
        self.Procedure_comboBox_tab4.setGeometry(QRect(560, 110, 81, 22))
        self.tabWidget.addTab(self.tab_4, "")
        Stats.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Stats)
        self.statusbar.setObjectName(u"statusbar")
        Stats.setStatusBar(self.statusbar)

        self.retranslateUi(Stats)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Stats)
    # setupUi

    def retranslateUi(self, Stats):
        Stats.setWindowTitle(QCoreApplication.translate("Stats", u"MainWindow", None))
        self.return_to_main_button.setText(QCoreApplication.translate("Stats", u"Return to Main Menu", None))
        self.save_pic_button1.setText(QCoreApplication.translate("Stats", u"Save Pic", None))
        self.titel_Tab1.setText(QCoreApplication.translate("Stats", u"<html><head/><body><p align=\"center\">Statistics for all patients</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Stats", u"Tab 1", None))
        self.return_to_main_button_2.setText(QCoreApplication.translate("Stats", u"Return to Main Menu", None))
        self.save_pic_button_2.setText(QCoreApplication.translate("Stats", u"Save Pic", None))
        self.titel_tab2.setText(QCoreApplication.translate("Stats", u"<html><head/><body><p align=\"center\">Statistics for all patients</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Stats", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">range of years</span></p></body></html>", None))
        self.update_tab2.setText(QCoreApplication.translate("Stats", u"Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Stats", u"Tab 2", None))
        self.return_to_main_button_3.setText(QCoreApplication.translate("Stats", u"Return to Main Menu", None))
        self.save_pic_button_3.setText(QCoreApplication.translate("Stats", u"Save Pic", None))
        self.titel_tab2_2.setText(QCoreApplication.translate("Stats", u"<html><head/><body><p align=\"center\">Statistics for all patients</p></body></html>", None))
        self.Obesity_grade_label.setText(QCoreApplication.translate("Stats", u"Obesity grade", None))
        self.Age_groups_label.setText(QCoreApplication.translate("Stats", u"Age groups", None))
        self.Procedure_label.setText(QCoreApplication.translate("Stats", u"Procedure", None))
        self.Months_after_label.setText(QCoreApplication.translate("Stats", u"Months after the surgery", None))
        self.update_tab3.setText(QCoreApplication.translate("Stats", u"Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Stats", u"tab_3", None))
        self.Age_groups_label_2.setText(QCoreApplication.translate("Stats", u"Age groups", None))
        self.save_pic_button_4.setText(QCoreApplication.translate("Stats", u"Save Pic", None))
        self.titel_tab2_3.setText(QCoreApplication.translate("Stats", u"<html><head/><body><p align=\"center\">Statistics for all patients</p></body></html>", None))
        self.Procedure_label_2.setText(QCoreApplication.translate("Stats", u"Procedure", None))
        self.update_tab4.setText(QCoreApplication.translate("Stats", u"Update", None))
        self.return_to_main_button_4.setText(QCoreApplication.translate("Stats", u"Return to Main Menu", None))
        self.Obesity_grade_label_2.setText(QCoreApplication.translate("Stats", u"Obesity grade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Stats", u"Tab 4", None))
    # retranslateUi

