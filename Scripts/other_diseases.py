# Pyside2 imports
import PySide2
import numpy as np
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets
# Ui imports
from Generated.other_diseases import Ui_other_diseases
# classes imports
from data_handler import *


class other_diseases(QMainWindow, Ui_other_diseases):
    def __init__(self, parent, handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.parent = parent
        self.handler = handler
        distinct_D = handler.df_other_diseases['Enfermedad asociada'].unique()
        self.other_comboBox.addItems(distinct_D)
        self.name = self.parent.name
        self.Name_label.setText(str(self.name))
        self.ID_label.setText(str(self.parent.id))
        self.rows_to_insert = pd.DataFrame(columns=self.handler.df_other_diseases.columns)
        self.Diabetes_options_group = QtWidgets.QButtonGroup(self)
        self.Sahos_options_group = QtWidgets.QButtonGroup(self)
        self.Hernia_options_group = QtWidgets.QButtonGroup(self)
        self.Esofagitis_options_group = QtWidgets.QButtonGroup(self)
        self.Diabetes_CB.stateChanged.connect(self.Diabetes_options)
        self.Sahos_CB.stateChanged.connect(self.Sahos_options)
        self.Hernia_CB.stateChanged.connect(self.Hernia_CB_options)
        self.Esofagitis_CB.stateChanged.connect(self.Esofagitis_options)
        self.others_CB.stateChanged.connect(self.others_options)
        self.other_comboBox.showPopup()
        self.setWindowTitle('Other Diseases')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.Messages()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.submit_button.clicked.connect(self.get_data)
        self.cancel_button.clicked.connect(self.return_to_add_p)

    def get_data(self):
        if isinstance(self.name, float):
            self.name = 'NaN'
        if self.HTA_CB.isChecked():
            a_series = pd.Series([str(self.parent.id), str(self.name), 'HTA'],
                                 index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        if self.Dislipidemia_CB.isChecked():
            a_series = pd.Series([str(self.parent.id), str(self.name), 'Dislipidemia'],
                                 index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        if self.Reflujo_CB.isChecked():
            a_series = pd.Series([str(self.parent.id), str(self.name), 'Reflujo'],
                                 index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        if self.Diabetes_CB.isChecked():
            if self.pre_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Diabetes pre'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.insulin_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Diabetes insulin'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.insulin_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Diabetes no insulin'],
                                     index=self.handler.df_other_diseases.columns)
            else:
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Diabetes'],
                                     index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        if self.Sahos_CB.isChecked():
            if self.con_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Sahos con'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.sin_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Sahos sin'],
                                     index=self.handler.df_other_diseases.columns)
            else:
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Sahos'],
                                     index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        if self.Hernia_CB.isChecked():
            if self.less_3cm_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Hernia less than 3cm'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.between_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Hernia between 3cm and 5cm'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.between_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Hernia greater than 5cm'],
                                     index=self.handler.df_other_diseases.columns)
            else:
                a_series = pd.Series([str(self.parent.id), str(self.name), 'Hernia'],
                                     index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        if self.Esofagitis_CB.isChecked():
            if self.A_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.parent.name), 'Esofagitis A'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.B_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.parent.name), 'Esofagitis B'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.C_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.parent.name), 'Esofagitis C'],
                                     index=self.handler.df_other_diseases.columns)
            elif self.D_CB.isChecked():
                a_series = pd.Series([str(self.parent.id), str(self.parent.name), 'Esofagitis D'],
                                     index=self.handler.df_other_diseases.columns)
            else:
                a_series = pd.Series([str(self.parent.id), str(self.parent.name), 'Esofagitis'],
                                     index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        if self.others_CB.isChecked():
            a_series = pd.Series([str(self.parent.id), str(self.parent.name), str(self.other_comboBox.currentText())],
                                 index=self.handler.df_other_diseases.columns)
            self.rows_to_insert = self.rows_to_insert.append(a_series, ignore_index=True)
        self.insert_data_to_df()

    def insert_data_to_df(self):
        df_other_diseases2 = self.handler.df_other_diseases.copy()
        df_other_diseases2 = df_other_diseases2.append(self.rows_to_insert, ignore_index=True)
        df_other_diseases2 = df_other_diseases2.drop_duplicates()
        df_other_diseases2 = df_other_diseases2.reset_index(drop=True)
        self.handler.write_other_diseases_data_frame(df_other_diseases2)
        QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_new_D )
        self.parent.finish_diseases()
        self.close()

    def Diabetes_options(self):
        if not (self.Diabetes_CB.isChecked()):
            self.Diabetes_options_group.removeButton(self.pre_CB)
            self.Diabetes_options_group.removeButton(self.insulin_CB)
            self.Diabetes_options_group.removeButton(self.no_insulin_CB)
            self.pre_CB.setChecked(False)
            self.insulin_CB.setChecked(False)
            self.no_insulin_CB.setChecked(False)

        else:
            self.Diabetes_options_group.addButton(self.pre_CB)
            self.Diabetes_options_group.addButton(self.insulin_CB)
            self.Diabetes_options_group.addButton(self.no_insulin_CB)

        self.pre_CB.setDisabled(not (self.Diabetes_CB.isChecked()))
        self.insulin_CB.setDisabled(not (self.Diabetes_CB.isChecked()))
        self.no_insulin_CB.setDisabled(not (self.Diabetes_CB.isChecked()))

    def Sahos_options(self):
        if not (self.Sahos_CB.isChecked()):
            self.Sahos_options_group.removeButton(self.con_CB)
            self.Sahos_options_group.removeButton(self.sin_CB)
            self.con_CB.setChecked(False)
            self.sin_CB.setChecked(False)
        else:
            self.Sahos_options_group.addButton(self.con_CB)
            self.Sahos_options_group.addButton(self.sin_CB)
        self.con_CB.setDisabled(not (self.Sahos_CB.isChecked()))
        self.sin_CB.setDisabled(not (self.Sahos_CB.isChecked()))

    def Hernia_CB_options(self):
        if not (self.Hernia_CB.isChecked()):
            self.Hernia_options_group.removeButton(self.less_3cm_CB)
            self.Hernia_options_group.removeButton(self.between_CB)
            self.Hernia_options_group.removeButton(self.larger_5_CB)
            self.less_3cm_CB.setChecked(False)
            self.between_CB.setChecked(False)
            self.larger_5_CB.setChecked(False)

        else:
            self.Hernia_options_group.addButton(self.less_3cm_CB)
            self.Hernia_options_group.addButton(self.between_CB)
            self.Hernia_options_group.addButton(self.larger_5_CB)

        self.less_3cm_CB.setDisabled(not (self.Hernia_CB.isChecked()))
        self.between_CB.setDisabled(not (self.Hernia_CB.isChecked()))
        self.larger_5_CB.setDisabled(not (self.Hernia_CB.isChecked()))

    def Esofagitis_options(self):
        if not (self.Esofagitis_CB.isChecked()):
            self.Esofagitis_options_group.removeButton(self.A_CB)
            self.Esofagitis_options_group.removeButton(self.B_CB)
            self.Esofagitis_options_group.removeButton(self.C_CB)
            self.Esofagitis_options_group.removeButton(self.D_CB)
            self.A_CB.setChecked(False)
            self.B_CB.setChecked(False)
            self.C_CB.setChecked(False)
            self.D_CB.setChecked(False)

        else:
            self.Esofagitis_options_group.addButton(self.A_CB)
            self.Esofagitis_options_group.addButton(self.B_CB)
            self.Esofagitis_options_group.addButton(self.C_CB)
            self.Esofagitis_options_group.addButton(self.D_CB)

        self.A_CB.setDisabled(not (self.Esofagitis_CB.isChecked()))
        self.B_CB.setDisabled(not (self.Esofagitis_CB.isChecked()))
        self.C_CB.setDisabled(not (self.Esofagitis_CB.isChecked()))
        self.D_CB.setDisabled(not (self.Esofagitis_CB.isChecked()))

    def others_options(self):
        if not (self.others_CB.isChecked()):
            self.other_comboBox.setCurrentText('N.A.')
            self.other_comboBox.setDisabled(True)
        else:
            self.other_comboBox.setDisabled(False)

    def return_to_add_p(self):
        self.parent.finish_diseases()
        self.close()

    def Messages(self):
        self.Message_new_D = 'New deceases added'
        self.Message_Success = 'Success'
        self.Message_Fail = 'Fail'