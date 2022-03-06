# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'other_diseases.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_other_diseases(object):
    def setupUi(self, other_diseases):
        if not other_diseases.objectName():
            other_diseases.setObjectName(u"other_diseases")
        other_diseases.resize(499, 521)
        self.layoutWidget = QWidget(other_diseases)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 120, 401, 29))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.HTA_CB = QCheckBox(self.layoutWidget)
        self.HTA_CB.setObjectName(u"HTA_CB")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.HTA_CB.setFont(font)

        self.horizontalLayout_5.addWidget(self.HTA_CB)

        self.Dislipidemia_CB = QCheckBox(self.layoutWidget)
        self.Dislipidemia_CB.setObjectName(u"Dislipidemia_CB")
        self.Dislipidemia_CB.setFont(font)

        self.horizontalLayout_5.addWidget(self.Dislipidemia_CB)

        self.Reflujo_CB = QCheckBox(self.layoutWidget)
        self.Reflujo_CB.setObjectName(u"Reflujo_CB")
        self.Reflujo_CB.setFont(font)

        self.horizontalLayout_5.addWidget(self.Reflujo_CB)

        self.layoutWidget_2 = QWidget(other_diseases)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 170, 441, 241))
        self.formLayout = QFormLayout(self.layoutWidget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Diabetes_CB = QCheckBox(self.layoutWidget_2)
        self.Diabetes_CB.setObjectName(u"Diabetes_CB")
        self.Diabetes_CB.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Diabetes_CB)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pre_CB = QCheckBox(self.layoutWidget_2)
        self.pre_CB.setObjectName(u"pre_CB")
        self.pre_CB.setEnabled(False)
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(10)
        self.pre_CB.setFont(font1)
        self.pre_CB.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pre_CB)

        self.insulin_CB = QCheckBox(self.layoutWidget_2)
        self.insulin_CB.setObjectName(u"insulin_CB")
        self.insulin_CB.setEnabled(False)
        self.insulin_CB.setFont(font1)
        self.insulin_CB.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.insulin_CB)

        self.no_insulin_CB = QCheckBox(self.layoutWidget_2)
        self.no_insulin_CB.setObjectName(u"no_insulin_CB")
        self.no_insulin_CB.setEnabled(False)
        self.no_insulin_CB.setFont(font1)
        self.no_insulin_CB.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.no_insulin_CB)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.Sahos_CB = QCheckBox(self.layoutWidget_2)
        self.Sahos_CB.setObjectName(u"Sahos_CB")
        self.Sahos_CB.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Sahos_CB)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.con_CB = QCheckBox(self.layoutWidget_2)
        self.con_CB.setObjectName(u"con_CB")
        self.con_CB.setEnabled(False)
        self.con_CB.setFont(font1)
        self.con_CB.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.con_CB)

        self.sin_CB = QCheckBox(self.layoutWidget_2)
        self.sin_CB.setObjectName(u"sin_CB")
        self.sin_CB.setEnabled(False)
        self.sin_CB.setFont(font1)
        self.sin_CB.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.sin_CB)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.Hernia_CB = QCheckBox(self.layoutWidget_2)
        self.Hernia_CB.setObjectName(u"Hernia_CB")
        self.Hernia_CB.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Hernia_CB)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.less_3cm_CB = QCheckBox(self.layoutWidget_2)
        self.less_3cm_CB.setObjectName(u"less_3cm_CB")
        self.less_3cm_CB.setEnabled(False)
        self.less_3cm_CB.setFont(font1)
        self.less_3cm_CB.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.less_3cm_CB)

        self.between_CB = QCheckBox(self.layoutWidget_2)
        self.between_CB.setObjectName(u"between_CB")
        self.between_CB.setEnabled(False)
        self.between_CB.setFont(font1)
        self.between_CB.setStyleSheet(u"")
        self.between_CB.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.between_CB)

        self.larger_5_CB = QCheckBox(self.layoutWidget_2)
        self.larger_5_CB.setObjectName(u"larger_5_CB")
        self.larger_5_CB.setEnabled(False)
        self.larger_5_CB.setFont(font1)
        self.larger_5_CB.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.larger_5_CB)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.Esofagitis_CB = QCheckBox(self.layoutWidget_2)
        self.Esofagitis_CB.setObjectName(u"Esofagitis_CB")
        self.Esofagitis_CB.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Esofagitis_CB)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.A_CB = QCheckBox(self.layoutWidget_2)
        self.A_CB.setObjectName(u"A_CB")
        self.A_CB.setEnabled(False)
        self.A_CB.setFont(font1)
        self.A_CB.setCheckable(True)

        self.horizontalLayout.addWidget(self.A_CB)

        self.B_CB = QCheckBox(self.layoutWidget_2)
        self.B_CB.setObjectName(u"B_CB")
        self.B_CB.setEnabled(False)
        self.B_CB.setFont(font1)
        self.B_CB.setCheckable(True)

        self.horizontalLayout.addWidget(self.B_CB)

        self.C_CB = QCheckBox(self.layoutWidget_2)
        self.C_CB.setObjectName(u"C_CB")
        self.C_CB.setEnabled(False)
        self.C_CB.setFont(font1)
        self.C_CB.setCheckable(True)

        self.horizontalLayout.addWidget(self.C_CB)

        self.D_CB = QCheckBox(self.layoutWidget_2)
        self.D_CB.setObjectName(u"D_CB")
        self.D_CB.setEnabled(False)
        self.D_CB.setFont(font1)
        self.D_CB.setCheckable(True)

        self.horizontalLayout.addWidget(self.D_CB)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.other_comboBox = QComboBox(self.layoutWidget_2)
        self.other_comboBox.setObjectName(u"other_comboBox")
        self.other_comboBox.setEnabled(False)
        self.other_comboBox.setFont(font1)
        self.other_comboBox.setEditable(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.other_comboBox)

        self.others_CB = QCheckBox(self.layoutWidget_2)
        self.others_CB.setObjectName(u"others_CB")
        self.others_CB.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.others_CB)

        self.layoutWidget_3 = QWidget(other_diseases)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 40, 341, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_6.addWidget(self.label)

        self.ID_label = QLabel(self.layoutWidget_3)
        self.ID_label.setObjectName(u"ID_label")

        self.horizontalLayout_6.addWidget(self.ID_label)

        self.label_2 = QLabel(self.layoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.Name_label = QLabel(self.layoutWidget_3)
        self.Name_label.setObjectName(u"Name_label")

        self.horizontalLayout_6.addWidget(self.Name_label)

        self.cancel_button = QPushButton(other_diseases)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(270, 450, 101, 23))
        self.cancel_button.setFont(font)
        self.submit_button = QPushButton(other_diseases)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(96, 450, 111, 23))
        self.submit_button.setFont(font)

        self.retranslateUi(other_diseases)

        QMetaObject.connectSlotsByName(other_diseases)
    # setupUi

    def retranslateUi(self, other_diseases):
        other_diseases.setWindowTitle(QCoreApplication.translate("other_diseases", u"Dialog", None))
        self.HTA_CB.setText(QCoreApplication.translate("other_diseases", u"HTA", None))
        self.Dislipidemia_CB.setText(QCoreApplication.translate("other_diseases", u"Dislipidemia", None))
        self.Reflujo_CB.setText(QCoreApplication.translate("other_diseases", u"Reflujo", None))
        self.Diabetes_CB.setText(QCoreApplication.translate("other_diseases", u"Diabetes Mellitus", None))
        self.pre_CB.setText(QCoreApplication.translate("other_diseases", u"pre", None))
        self.insulin_CB.setText(QCoreApplication.translate("other_diseases", u"insulin", None))
        self.no_insulin_CB.setText(QCoreApplication.translate("other_diseases", u"no insulin", None))
        self.Sahos_CB.setText(QCoreApplication.translate("other_diseases", u"Sahos", None))
        self.con_CB.setText(QCoreApplication.translate("other_diseases", u"con", None))
        self.sin_CB.setText(QCoreApplication.translate("other_diseases", u"sin", None))
        self.Hernia_CB.setText(QCoreApplication.translate("other_diseases", u"Hernia Hiatal", None))
        self.less_3cm_CB.setText(QCoreApplication.translate("other_diseases", u"<3 cm", None))
        self.between_CB.setText(QCoreApplication.translate("other_diseases", u"3 cm < x < 5 cm", None))
        self.larger_5_CB.setText(QCoreApplication.translate("other_diseases", u"> 5 cm", None))
        self.Esofagitis_CB.setText(QCoreApplication.translate("other_diseases", u"Esofagitis", None))
        self.A_CB.setText(QCoreApplication.translate("other_diseases", u"A", None))
        self.B_CB.setText(QCoreApplication.translate("other_diseases", u"B", None))
        self.C_CB.setText(QCoreApplication.translate("other_diseases", u"C", None))
        self.D_CB.setText(QCoreApplication.translate("other_diseases", u"D", None))
        self.others_CB.setText(QCoreApplication.translate("other_diseases", u"Others", None))
        self.label.setText(QCoreApplication.translate("other_diseases", u"ID", None))
        self.ID_label.setText("")
        self.label_2.setText(QCoreApplication.translate("other_diseases", u"Name", None))
        self.Name_label.setText("")
        self.cancel_button.setText(QCoreApplication.translate("other_diseases", u"Cancel", None))
        self.submit_button.setText(QCoreApplication.translate("other_diseases", u"Submit", None))
    # retranslateUi

