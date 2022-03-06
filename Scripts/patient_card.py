# general imports
import inspect
import os
from datetime import datetime
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
# pyside2 imports
import PySide2
from PySide2.QtWidgets import QMainWindow, QAbstractItemView, QHeaderView, QTableView, QApplication
from PySide2.QtGui import QIcon, QColor, QIntValidator, QRegExpValidator
from PySide2.QtCore import QRegExp, Qt
from PySide2 import QtWidgets
# Ui imports
from Generated.patient_card import Ui_Patient_card
# classes imports
from add_follow_m import addFollow_m
from update_fu import update_FU
from other_diseases import other_diseases
from data_handler import *


class Patient_card(QMainWindow, Ui_Patient_card):
    def __init__(self, parent, handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.path = os.path.dirname(os.path.abspath(__file__)).split("\\")
        self.path = self.path[:-1]
        self.path = '\\'.join(self.path)
        self.parent = parent
        self.handler = handler
        self.Messages()
        self.tabWidget.tabBar().setTabTextColor(0, QColor(251, 248, 190))
        self.tabWidget.tabBar().setTabTextColor(1, QColor(251, 248, 190))
        self.tabWidget.tabBar().setTabTextColor(2, QColor(251, 248, 190))
        self.add_follow_m = 0
        self.update_FU = 0
        origen_list = ['Privado', 'H.U.S.I', 'Pre-Pagada', 'Sin Especificar']
        self.Origen_CB.addItems(origen_list)
        procedure = ['BAGUA', 'Balón', 'Manga', 'By-pass', 'Otros', 'Re-Operación', 'Procedimiento Pendiente']
        self.Type_CB.addItems(procedure)
        self.Complications_checkBox.setDisabled(True)
        self.get_data()
        self.setWindowTitle('Patient Card')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.main_button.clicked.connect(self.move_main)
        self.search_button.clicked.connect(self.move_to_findP)
        self.Update_button_T1.clicked.connect(self.update_T1)
        self.submit_Button_T1.clicked.connect(self.create_the_row)
        self.delete_button_T1.clicked.connect(self.delete_T1)
        self.Add_Button_T2.clicked.connect(self.move_add_follow)
        self.progress_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Delete_button_T2.clicked.connect(self.delete_T2)
        self.main_button_T2.clicked.connect(self.move_main)
        self.search_button_T2.clicked.connect(self.move_to_findP)
        self.main_button_T3.clicked.connect(self.move_main)
        self.search_button_T3.clicked.connect(self.move_to_findP)
        self.Update_button_T2.clicked.connect(self.update_T2)
        self.show_comp_button.clicked.connect(self.show_comp)
        self.hide_comp_button.clicked.connect(self.hide_comp)
        self.Cancel_Update_button_T1.clicked.connect(self.get_data)
        self.go_to_diseases_button.clicked.connect(self.go_to_diseases)
        self.save_button.clicked.connect(self.save_image)
        self.delete_d.clicked.connect(self.Delete_D)

    def set_validation(self):
        weight_validator = QIntValidator(50, 250, self)
        height_validator = QRegExpValidator(QRegExp(r'([1]?\.[0-9]+)|(2\.[0-3])'))
        email_validator = QRegExpValidator(QRegExp(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'))
        phone_validator = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.weight_edit.setValidator(weight_validator)
        self.height_edit.setValidator(height_validator)
        self.email_edit.setValidator(email_validator)
        self.phone_edit.setValidator(phone_validator)

    def save_image(self):
        desired_folder = os.path.join(self.path, 'pics\\personal info')
        today = datetime.now().date()
        name = str(self.name) + "_" + str(today)
        full_path = os.path.join(desired_folder, name)
        try:
            self.plt.savefig(full_path)
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_image_saved)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_folder_not_exist)

    def get_data(self):
        self.Dont_update()
        self.diseases_list.clear()
        row_data = [self.handler.df_first_meeting.query('Cedula == @self.handler.R_id')]
        today = datetime.now().date()
        formatted_today = pd.to_datetime(today).date()
        self.id = self.handler.R_id
        self.name = row_data[0].iloc[0][1]
        self.telephone = row_data[0].iloc[0][2]
        self.email = row_data[0].iloc[0][3]
        self.date_of_birth = row_data[0].iloc[0][4].strftime("%d/%m/%Y")
        self.age = len(pd.date_range(start=row_data[0].iloc[0][4], end=formatted_today, freq='Y'))
        self.origen = row_data[0].iloc[0][5]
        self.weight = row_data[0].iloc[0][6]
        self.height = row_data[0].iloc[0][7]
        self.type = row_data[0].iloc[0][8]
        self.hernia = row_data[0].iloc[0][10]
        self.comp_during = row_data[0].iloc[0][11]
        self.comp_post = row_data[0].iloc[0][12]
        self.comp_additional = row_data[0].iloc[0][13]
        if str(row_data[0].iloc[0][9]) == 'NaT':
            self.date = 'Pendiente'
        else:
            self.date = row_data[0].iloc[0][9].strftime("%d/%m/%Y")
        self.tabWidget.setCurrentIndex(0)

        self.Anot_text.setEnabled(False)
        self.submit_Button_T1.hide()
        self.hide_comp_button.hide()
        self.calendarWidget_P_card.hide()
        self.Comp_label.hide()
        self.L_during_comp.hide()
        self.L_post_comp.hide()
        self.L_additional_surgery.hide()
        self.during_comp_edit.hide()
        self.post_comp_edit.hide()
        self.additional_edit.hide()
        self.set_diseases_list()
        self.set_personal_details()
        self.set_progress_deatails()
        self.create_graph2()

    def set_diseases_list(self):
        row_data2 = self.handler.df_other_diseases.loc[
            self.handler.df_other_diseases['Cedula'] == self.handler.R_id, ['Enfermedad asociada']]

        for row in range(len(row_data2)):
            self.diseases_list.addItem(QtWidgets.QListWidgetItem(str(row_data2.iloc[row, 0])))

    def set_personal_details(self):
        if self.hernia == 1:
            flag = True
        else:
            flag = False
        self.name_edit.setText(str(self.name))
        bmi_25 = self.getBMInum(self.weight, 25)
        bmi_23 = self.getBMInum(self.weight, 23)
        self.Id_label_edit_T1.setText(str(self.handler.R_id))
        self.email_edit.setText(str(self.email))
        self.phone_edit.setText(str(self.telephone))

        self.Origen_CB.setCurrentText(str(self.origen))
        self.Type_CB.setCurrentText(str(self.type))
        self.Date_of_birth_edit.setText(str(self.date_of_birth))
        self.age_lable_edit.setText(str(self.age))
        self.height_edit.setText(str(self.height))
        self.weight_edit.setText(str(self.weight))
        self.hernia_checkBox.setChecked(flag)
        self.originalBMI = float(self.getBMI(self.weight))
        self.bmi_lable_edit.setText(str(self.getBMI(self.weight)))
        self.date_lable_edit_2.setText(str(self.date))
        self.init_ideal_W25 = float(bmi_25[0])
        self.bmi25_lable_edit.setText(str(bmi_25[0]))
        self.over25_lable_edit.setText(str(bmi_25[1]))
        self.over25per_lable_edit.setText(str(bmi_25[2]))
        self.bmi23_lable_edit.setText(str(bmi_23[0]))
        self.over23_lable_edit.setText(str(bmi_23[1]))
        self.over23per_lable_edit.setText(str(bmi_23[2]))
        if isinstance(self.comp_during, str) or isinstance(self.comp_post, str) or isinstance(self.comp_additional,
                                                                                              str):
            self.Complications_checkBox.setChecked(True)
            self.during_comp_edit.setText(str(self.comp_during))
            self.post_comp_edit.setText(str(self.comp_post))
            self.additional_edit.setText(str(self.comp_additional))
        else:
            self.Complications_checkBox.setChecked(False)
            self.during_comp_edit.setText(str(self.comp_during))
            self.post_comp_edit.setText(str(self.comp_post))
            self.additional_edit.setText(str(self.comp_additional))

    def set_progress_deatails(self):
        self.progress_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.progress_table.setSelectionBehavior(QTableView.SelectRows)
        self.progress_table.setColumnCount(7)
        row_data2 = self.handler.df_followUp.loc[
            self.handler.df_followUp['Cedula'] == self.handler.R_id, ['Fecha', 'Peso', 'Anotaciones']]
        row_data2 = row_data2.sort_values(by='Fecha', na_position='first')
        self.progress_table.setRowCount(len(row_data2.index))  # set row number as the len of results
        self.Id_label_edit_T2.setText(str(self.handler.R_id))
        self.name_label_edit_T2.setText(str(self.name))
        self.email_label_edit_T2.setText(str(self.email))
        self.phone_label_edit_T2.setText(str(self.telephone))
        self.age_label_edit_T2.setText(str(self.age))
        self.Id_label_edit_T3.setText(str(self.handler.R_id))
        self.name_label_edit_T3.setText(str(self.name))
        self.email_label_edit_T3.setText(str(self.email))
        self.phone_label_edit_T3.setText(str(self.telephone))
        self.age_label_edit_T3.setText(str(self.age))
        for row in range(self.progress_table.rowCount()):
            if str(row_data2.iloc[row].at['Fecha']) == "NaT":

                self.progress_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str('Pre-Qx')))
                self.progress_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str('-')))
            else:
                start_date = pd.to_datetime(self.date, format="%d/%m/%Y")
                end_date = row_data2.iloc[row]['Fecha']
                diff_month = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                row_data2.iloc[row, 0] = pd.to_datetime(row_data2.iloc[row, 0], format="%Y/%m/%d").date()
                row_data2.iloc[row, 0] = row_data2.iloc[row, 0].strftime("%d/%m/%Y")
                self.progress_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row_data2.iloc[row, 0])))
                self.progress_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(diff_month)))
            if row != 0:
                self.progress_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(row_data2.iloc[row, 1])))
            else:
                row_data2.iloc[row, 1] = self.weight
                self.progress_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(row_data2.iloc[row, 1])))
            results = self.getBMInum(self.weight, 25)
            self.progress_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.getBMI(row_data2.iloc[row, 1]))))
            weight_dropped = self.weight - row_data2.iloc[row, 1]
            self.progress_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(weight_dropped)))
            weight_dropped_pres = weight_dropped / (self.weight - results[3])
            formatted_overweight = "{:.0%}".format(weight_dropped_pres)
            self.progress_table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(formatted_overweight)))
            if pd.isna(row_data2.iloc[row, 2]):
                self.progress_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(0)))
            else:
                self.progress_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(1)))
        self.progress_table.cellClicked.connect(self.get_anoc)

    def show_comp(self):
        self.hide_comp_button.show()
        self.show_comp_button.hide()
        self.Comp_label.show()
        self.L_during_comp.show()
        self.L_post_comp.show()
        self.L_additional_surgery.show()
        self.during_comp_edit.show()
        self.post_comp_edit.show()
        self.additional_edit.show()

    def hide_comp(self):
        self.hide_comp_button.hide()
        self.show_comp_button.show()
        self.Comp_label.hide()
        self.L_during_comp.hide()
        self.L_post_comp.hide()
        self.L_additional_surgery.hide()
        self.during_comp_edit.hide()
        self.post_comp_edit.hide()
        self.additional_edit.hide()

    def get_anoc(self):
        index = (self.progress_table.selectionModel().currentIndex())
        self.handler.Update_R_date(index.sibling(index.row(), 0).data())
        index = self.handler.df_followUp.index
        condition = self.handler.df_followUp["Cedula"] == self.handler.R_id
        relevent_rows = index[condition]
        relevent_rows_list = relevent_rows.tolist()
        for index in relevent_rows_list:
            if str(self.handler.df_followUp.at[index, 'Fecha']) == 'NaT':
                if self.handler.R_date == 'Pre-Qx':
                    self.Anot_text.setText(str(self.handler.df_followUp.at[index, 'Anotaciones']))
                    break
            elif self.handler.df_followUp.at[index, 'Fecha'].strftime("%d/%m/%Y") == self.handler.R_date:
                self.Anot_text.setText(str(self.handler.df_followUp.at[index, 'Anotaciones']))
                break

    def update_T1(self):
        self.set_validation()
        self.Update_button_T1.hide()
        self.Cancel_Update_button_T1.show()
        self.name_edit.setReadOnly(False)
        self.name_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.email_edit.setReadOnly(False)
        self.email_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.phone_edit.setReadOnly(False)
        self.phone_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.hernia_checkBox.setEnabled(True)
        self.Origen_CB.setEnabled(True)
        self.Type_CB.setEnabled(True)
        self.height_edit.setReadOnly(False)
        self.height_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.weight_edit.setReadOnly(False)
        self.weight_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.during_comp_edit.setReadOnly(False)
        self.during_comp_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.post_comp_edit.setReadOnly(False)
        self.post_comp_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.additional_edit.setReadOnly(False)
        self.additional_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.Date_of_birth_edit.setReadOnly(False)
        self.Date_of_birth_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(255,255,255);""}")
        self.submit_Button_T1.show()
        self.Update_date_check.setChecked(False)
        self.Waiting_date_check.setChecked(False)
        self.Update_date_check.show()
        self.Update_date_check.stateChanged.connect(self.state_changed)

    def state_changed(self):
        if self.Update_date_check.isChecked():
            self.Waiting_date_check.show()
            self.calendarWidget_P_card.show()
        else:
            self.Waiting_date_check.setChecked(False)
            self.Waiting_date_check.hide()
            self.calendarWidget_P_card.hide()

    def Dont_update(self):
        self.Cancel_Update_button_T1.hide()
        self.Update_button_T1.show()
        self.show_comp_button.show()
        self.Update_date_check.hide()
        self.Waiting_date_check.hide()
        self.calendarWidget_P_card.hide()
        self.hernia_checkBox.setEnabled(False)
        self.name_edit.setReadOnly(True)
        self.name_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.email_edit.setReadOnly(True)
        self.email_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.phone_edit.setReadOnly(True)
        self.phone_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.Date_of_birth_edit.setReadOnly(True)
        self.Date_of_birth_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.Origen_CB.setEnabled(False)
        self.Type_CB.setEnabled(False)
        self.height_edit.setReadOnly(True)
        self.height_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.weight_edit.setReadOnly(True)
        self.weight_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.during_comp_edit.setReadOnly(True)
        self.during_comp_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.post_comp_edit.setReadOnly(True)
        self.post_comp_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.additional_edit.setReadOnly(True)
        self.additional_edit.setStyleSheet("QLineEdit" "{" "background-color : rgb(238,238,238);""}")
        self.submit_Button_T1.hide()

    def create_the_row(self):
        if self.hernia_checkBox.isChecked():
            hernia_flag = 1
        else:
            hernia_flag = 0
        self.date_of_birth = self.Date_of_birth_edit.text()
        QApplication.setOverrideCursor(Qt.WaitCursor)
        format_date_of_birth = "%d/%m/%Y"
        try:
            flag_date_of_birth = bool(datetime.strptime(self.date_of_birth, format_date_of_birth))
        except ValueError:
            flag_date_of_birth = False
        if not flag_date_of_birth:
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_enter_DOT_again)
            self.get_data()
        else:
            if self.Update_date_check.isChecked():
                if self.Waiting_date_check.isChecked():
                    new_row = [self.handler.R_id, str(self.name_edit.text()), str(self.phone_edit.text()),
                               str(self.email_edit.text()), str(self.date_of_birth),
                               str(self.Origen_CB.currentText()), str(self.weight_edit.text()),
                               str(self.height_edit.text()),
                               str(self.Type_CB.currentText()), str('Pendiente'),
                               str(hernia_flag), str(self.during_comp_edit.text()),
                               str(self.post_comp_edit.text()), str(self.additional_edit.text())]

                    if new_row[9] == 'Pendiente' or new_row[9] == 'pendiente':
                        new_row[9] = ''
                    if new_row[9] != '':
                        new_row[9] = pd.to_datetime(new_row[9], format="%d/%m/%Y")
                    new_row[4] = pd.to_datetime(new_row[4], format="%d/%m/%Y")
                else:
                    date = self.calendarWidget_P_card.selectedDate()
                    self.new_date = date.toPython()
                    self.new_date = self.new_date.strftime("%d/%m/%Y")
                    new_row = [self.handler.R_id, str(self.name_edit.text()), str(self.phone_edit.text()),
                               str(self.email_edit.text()), str(self.date_of_birth),
                               str(self.Origen_CB.currentText()), str(self.weight_edit.text()),
                               str(self.height_edit.text()),
                               str(self.Type_CB.currentText()), str(self.new_date),
                               str(hernia_flag), str(self.during_comp_edit.text()),
                               str(self.post_comp_edit.text()), str(self.additional_edit.text())]

                    new_row[9] = pd.to_datetime(new_row[9], format="%d/%m/%Y")
                    new_row[4] = pd.to_datetime(new_row[4], format="%d/%m/%Y")

            else:
                new_row = [self.handler.R_id, str(self.name_edit.text()), str(self.phone_edit.text()),
                           str(self.email_edit.text()), str(self.date_of_birth),
                           str(self.Origen_CB.currentText()), str(self.weight_edit.text()),
                           str(self.height_edit.text()),
                           str(self.Type_CB.currentText()), str(self.date_lable_edit_2.text()),
                           str(hernia_flag), str(self.during_comp_edit.text()),
                           str(self.post_comp_edit.text()), str(self.additional_edit.text())]

                if new_row[9] == 'Pendiente' or new_row[9] == 'pendiente':
                    new_row[9] = ''
                if new_row[9] != '':
                    new_row[9] = pd.to_datetime(new_row[9], format="%d/%m/%Y")
                new_row[4] = pd.to_datetime(new_row[4], format="%d/%m/%Y")

            self.submit_the_row_T1(new_row)

    def submit_the_row_T1(self, row):

        df_first_meeting2 = self.handler.df_first_meeting.copy()
        df_first_meeting2 = df_first_meeting2[df_first_meeting2.Cedula != self.handler.R_id]
        a_series = pd.Series(row, index=df_first_meeting2.columns)
        df_first_meeting2 = df_first_meeting2.append(a_series, ignore_index=True)
        for index in df_first_meeting2.index:
            df_first_meeting2.iat[index, 4] = df_first_meeting2.iat[index, 4].strftime("%d/%m/%Y")
            if df_first_meeting2.iat[index, 9] is pd.NaT or isinstance(df_first_meeting2.iat[index, 9], float) or \
                    df_first_meeting2.iat[index, 9] == '' or isinstance(df_first_meeting2.iat[index, 9], str):
                df_first_meeting2.iat[index, 9] == ''
            else:
                df_first_meeting2.iat[index, 9] = df_first_meeting2.iat[index, 9].strftime("%d/%m/%Y")
        QApplication.restoreOverrideCursor()
        QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_patient_update)
        self.handler.write_first_meeting_data_frame(df_first_meeting2)
        self.close()
        self.get_data()
        self.Dont_update()
        self.show()

    def delete_T1(self):
        reply = QtWidgets.QMessageBox.warning(self, self.titel_for_remove_patient, self.Message_remove_patient,
                                              QtWidgets.QMessageBox.Ok,
                                              QtWidgets.QMessageBox.Cancel)
        if reply == 1024:  # 1024 is what QtWidgets.QMessageBox.Ok return
            QApplication.setOverrideCursor(Qt.WaitCursor)
            df_first_meeting2 = self.handler.df_first_meeting.copy()
            df_first_meeting2 = df_first_meeting2[df_first_meeting2.Cedula != self.handler.R_id]
            df_first_meeting2 = df_first_meeting2.reset_index(drop=True)

            for index in (df_first_meeting2.index):
                df_first_meeting2.iat[index, 4] = df_first_meeting2.iat[index, 4].strftime("%d/%m/%Y")
                if df_first_meeting2.iat[index, 9] is pd.NaT or isinstance(df_first_meeting2.iat[index, 9], float) or \
                        df_first_meeting2.iat[index, 9] == '' or isinstance(df_first_meeting2.iat[index, 9], str):
                    df_first_meeting2.iat[index, 9] == 'Pendiente'

                else:
                    df_first_meeting2.iat[index, 9] = df_first_meeting2.iat[index, 9].strftime("%d/%m/%Y")

            df_followUp2 = self.handler.df_followUp.copy()

            for index1 in (df_followUp2.index):
                if df_followUp2.iat[index1, 2] is pd.NaT or isinstance(df_followUp2.iat[index1, 2], float) or \
                        df_followUp2.iat[index1, 2] == '':
                    df_followUp2.iat[index1, 2] == ''
                else:
                    df_followUp2.iat[index1, 2] = df_followUp2.iat[index1, 2].strftime("%d/%m/%Y")

            indexNames = df_followUp2[(df_followUp2['Cedula'] == self.handler.R_id)].index
            df_followUp2 = df_followUp2.drop(indexNames)

            df_other_diseases2 = self.handler.df_other_diseases.copy()
            indexNames = df_other_diseases2[(df_other_diseases2['Cedula'] == self.handler.R_id)].index
            df_other_diseases2 = df_other_diseases2.drop(indexNames)

            self.handler.write_first_meeting_data_frame(df_first_meeting2)
            self.handler.write_follow_up(df_followUp2)
            self.handler.write_other_diseases_data_frame(df_other_diseases2)

            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_delete_patient_Success)
            self.move_main()
        else:
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_patient_stay)

    def delete_T2(self):
        index = (self.progress_table.selectionModel().currentIndex())
        self.handler.Update_R_date(index.sibling(index.row(), 0).data())

        if self.handler.R_date:
            if self.handler.R_date != 'Pre-Qx':
                reply = QtWidgets.QMessageBox.warning(self, self.titel_for_remove_meeting, self.Message_remove_meeting,
                                                      QtWidgets.QMessageBox.Ok,
                                                      QtWidgets.QMessageBox.Cancel)

                if reply == 1024:  # 1024 is what QtWidgets.QMessageBox.Ok return
                    QApplication.setOverrideCursor(Qt.WaitCursor)
                    df_followUp2 = self.handler.df_followUp.copy()

                    for index in (df_followUp2.index):
                        if df_followUp2.iat[index, 2] is pd.NaT or isinstance(df_followUp2.iat[index, 2], float) or \
                                df_followUp2.iat[index, 2] == '':
                            df_followUp2.iat[index, 2] == ''
                        else:
                            df_followUp2.iat[index, 2] = df_followUp2.iat[index, 2].strftime("%d/%m/%Y")

                    indexNames = df_followUp2[
                        (df_followUp2['Cedula'] == self.handler.R_id) & (
                                df_followUp2['Fecha'] == self.handler.R_date)].index
                    df_followUp2 = df_followUp2.drop(indexNames)
                    self.handler.write_follow_up(df_followUp2)
                    QApplication.restoreOverrideCursor()
                    QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_delete_Fu_Success)
                    self.close()
                    self.wid_graphs.close()
                    self.p_card = Patient_card(self.parent, self.handler)
                    self.p_card.tabWidget.setCurrentIndex(1)
                    self.p_card.show()
                else:
                    QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_meeting_stay)
            else:
                QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_cant_delete_row)
        else:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_select_row)

    def Delete_D(self):
        item = self.diseases_list.currentItem()
        if not item:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_select_row)
        else:
            diseases_df = self.handler.df_other_diseases.copy()
            indexNames = diseases_df[(diseases_df["Enfermedad asociada"] == item.text()) & (
                    diseases_df['Cedula'] == self.handler.R_id)].index
            diseases_df = diseases_df.drop(index=indexNames[0])
            self.handler.write_other_diseases_data_frame(diseases_df)
            self.get_data()
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_disease_deleted)

    def update_T2(self):
        index = (self.progress_table.selectionModel().currentIndex())
        self.handler.Update_R_date(index.sibling(index.row(), 0).data())
        if self.handler.R_date:
            if self.handler.R_date != 'Pre-Qx':
                self.close()
                if inspect.isclass(self.update_FU):
                    self.update_FU.show()
                else:
                    self.update_FU = update_FU(self, self.handler)
                    self.update_FU.show()
            else:
                QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_only_change_in_personal_info)

        else:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_select_row)

    def getBMI(self, weight):
        bmi = (weight / (self.height ** 2))
        formatted_bmi = "{:.2f}".format(bmi)
        return formatted_bmi

    def getBMInum(self, weight, BMI):
        ideal_weight = BMI * (self.height ** 2)
        formatted_ideal_weight = "{:.0f}".format(ideal_weight)
        overweight = weight - ideal_weight
        formatted_overweight = "{:.0f}".format(overweight)
        overweight_percentage = ((weight / ideal_weight) - 1)
        formatted_overweight_percentage = "{:.2f}".format(overweight_percentage)
        results = [formatted_ideal_weight, formatted_overweight, formatted_overweight_percentage, ideal_weight]
        return results

    def create_graph2(self):
        self.wid_graphs = QtWidgets.QWidget(self.tab)
        self.wid_graphs.setGeometry(0, 90, 1300, 400)
        grid_graphs = QtWidgets.QGridLayout(self.wid_graphs)
        x_data = []
        weight_y_data = []
        weightLost_y_data = []
        BMI_y_data = []
        weightLostPresent_y_data = []
        for row in range(self.progress_table.rowCount()):
            if row == 0:
                x_data.append(0)
                dif_start_ideal = self.weight - self.init_ideal_W25
                weight_y_data.append(self.weight)
                weightLost_y_data.append(0)
                BMI_y_data.append(float(self.progress_table.item(row, 3).text()))
                weightLostPresent_y_data.append(0)
            else:
                x_data.append(int(self.progress_table.item(row, 1).text()))
                weight_y_data.append(float(self.progress_table.item(row, 2).text()))
                weightLost_y_data.append(float(self.progress_table.item(row, 4).text()))
                BMI_y_data.append(float(self.progress_table.item(row, 3).text()))

                dif_start_current = float(self.progress_table.item(row, 4).text())
                weightLostPresent_y_data.append(round(dif_start_current / dif_start_ideal, 2))
        fig_graphs = plt.figure(tight_layout=True)
        number_of_mounth = len(x_data)
        ind = np.arange(number_of_mounth)
        width = 0.5
        ax_weight, ax_BMI, ax_lost = fig_graphs.subplots(1, 3)

        rectsWeight = ax_weight.bar(ind, weight_y_data, width, edgecolor="white", color='tab:blue')
        rectsWeightLost = ax_weight.bar(ind + width, weightLost_y_data, width, edgecolor="white", color='tab:green')
        ax_weight.set_xlabel("Month From Procedure")
        ax_weight.set_ylabel("Weight [kg]")
        ax_weight.set_title(f'Weight Over Month')
        ax_weight.set_xticks(ind + width / 2)
        ax_weight.set_xticklabels(x_data)
        ax_weight.legend((rectsWeight[0], rectsWeightLost[0]), ('weight', 'weight lost'))

        ax_BMI.plot(x_data, BMI_y_data, '-o', color='tab:blue')
        ax_BMI.axhline(25, color='r')
        ax_BMI.set_xlabel("Month From Procedure")
        ax_BMI.set_ylabel("BMI")
        ax_BMI.set_title(f'BMI Over Month')
        ax_BMI.set_ylim([0, 70])

        rectsLostPer = ax_lost.bar(ind, weightLostPresent_y_data, width, edgecolor="white", color='tab:blue')
        ax_lost.set_ylim([-0.5, 1.5])
        ax_lost.set_xlabel("Month From Procedure")
        ax_lost.set_ylabel("Weight Lost [%]")
        ax_lost.set_title(f'Lost Weight Over Month')
        ax_lost.set_xticks(ind + width / 2)
        ax_lost.set_xticklabels(x_data)

        self.autolabel(rectsWeight, ax_weight)
        self.autolabel(rectsWeightLost, ax_weight)
        self.autolabel(rectsLostPer, ax_lost)

        self.plt = fig_graphs
        canvas_weight = FigureCanvas(fig_graphs)
        grid_graphs.addWidget(canvas_weight, 0, 0)
        self.wid_graphs.show()

    def autolabel(self, rects, ax):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                    float(height), backgroundcolor='0.85', fontsize='xx-small',
                    ha='center', va='bottom')

    def ShowFollowUp(self):
        self.progress_table.selectionModel().clear()
        self.set_progress_deatails()
        self.show()

    def re_open_this_window(self):
        self.get_data()
        super(Patient_card, self).show()

    def re_open_this_window_T2(self):
        self.get_data()
        self.tabWidget.setCurrentIndex(1)
        super(Patient_card, self).show()

    def move_main(self):
        self.close()
        self.wid_graphs.close()
        self.parent.parent.re_show()

    def move_to_findP(self):
        self.close()
        self.wid_graphs.close()
        self.parent.re_show()

    def move_add_follow(self):
        if str(self.date) != 'Pendiente':
            self.wid_graphs.close()
            self.close()
            if inspect.isclass(self.add_follow_m):
                self.add_follow_m.show()
            else:
                self.add_follow_m = addFollow_m(self, self.handler)
                self.add_follow_m.show()
        else:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_patient_still_waiting)

    def go_to_diseases(self):
        self.setDisabled(True)
        self.other_d_window = other_diseases(self, self.handler)
        self.other_d_window.show()

    def finish_diseases(self):
        self.setDisabled(False)
        self.get_data()

    def Messages(self):
        self.Message_select_row = 'First select a row please'
        self.Message_cant_delete_row = 'You cant delete this row'
        self.Message_meeting_stay = 'Meeting still in system'
        self.Message_delete_Fu_Success = 'You delete this meeting successfully'
        self.Message_delete_patient_Success = 'Patient deleted fron the system'
        self.Message_patient_stay = 'Patient still in system'
        self.Message_patient_update = 'Patient card is updated'
        self.Message_enter_DOT_again = 'Please enter date of birth'
        self.Message_image_saved = 'Image has been saved!!'
        self.Message_folder_not_exist = 'Folder does not exist'
        self.Message_only_change_in_personal_info = 'This row can only be change in personal info'
        self.Message_patient_still_waiting = 'Cant add meeting if patient still waiting for surgery'
        self.Message_disease_deleted = 'The disease deleted'
        self.Message_remove_patient = 'Are you sure you want to remove this patient?'
        self.titel_for_remove_patient = 'Remove User List?'
        self.Message_remove_meeting = 'Are you sure you want to remove this meeting?'
        self.titel_for_remove_meeting = 'Remove meeting List?'
        self.Message_Success = 'Success'
        self.Message_Fail = 'Fail'
