# general imports
from datetime import datetime
# pyside2 imports
import PySide2
from PySide2.QtCore import QRegExp, Qt
from PySide2.QtGui import QIcon, QIntValidator, QRegExpValidator
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtWidgets
# Ui imports
from Generated.add_P import Ui_add_P
# classes imports
from other_diseases import other_diseases
from data_handler import *


class add_P(QMainWindow, Ui_add_P):
    def __init__(self, parent, handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.parent = parent
        self.handler = handler
        self.set_validation()
        self.setOrder()
        origen_list = ['Privado', 'H.U.S.I', 'Pre-Pagada', 'Sin Especificar']
        self.origen_comboBox.addItems(origen_list)
        procedure = ['BAGUA', 'Balón', 'Manga', 'By-pass', 'Otros', 'Re-Operación', 'Procedimiento Pendiente']
        self.procedure_comboBox.addItems(procedure)
        self.age_edit.setText('dd/mm/yyyy')
        self.flag = True
        self.setWindowTitle('Add Patient')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.Messages()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.submit_button.clicked.connect(self.insert_data)
        self.main_button.clicked.connect(self.move_main)

    def setOrder(self):
        self.setTabOrder(self.id_edit, self.name_edit)
        self.setTabOrder(self.name_edit, self.phone_edit)
        self.setTabOrder(self.phone_edit, self.email_edit)
        self.setTabOrder(self.email_edit, self.procedure_comboBox)
        self.setTabOrder(self.procedure_comboBox, self.age_edit)
        self.setTabOrder(self.age_edit, self.origen_comboBox)
        self.setTabOrder(self.origen_comboBox, self.weight_edit)
        self.setTabOrder(self.weight_edit, self.height_edit)
        self.setTabOrder(self.height_edit, self.hernia_CB)

    def set_validation(self):
        weight_validator = QIntValidator(50, 250, self)
        height_validator = QRegExpValidator(QRegExp(r'([1]?\.[0-9]+)|(2\.[0-3])'))
        email_validator = QRegExpValidator(QRegExp(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'))
        phone_validator = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.weight_edit.setValidator(weight_validator)
        self.height_edit.setValidator(height_validator)
        self.email_edit.setValidator(email_validator)
        self.phone_edit.setValidator(phone_validator)

    def insert_data(self):
        self.id = self.id_edit.text()
        self.name = self.name_edit.text()
        self.other_d_window = other_diseases(self, self.handler)
        self.telephone = self.phone_edit.text()
        self.email = self.email_edit.text()
        self.date_of_birth = self.age_edit.text()
        self.origen = str(self.origen_comboBox.currentText())
        self.weight = self.weight_edit.text()
        self.height = self.height_edit.text()
        self.type = str(self.procedure_comboBox.currentText())
        exists = self.id in str(self.handler.df_first_meeting.Cedula)
        format_date_of_birth = "%d/%m/%Y"
        QApplication.setOverrideCursor(Qt.WaitCursor)

        if self.id == '':  # check if the user didn't insert ID
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_enter_ID)
        elif exists:  # check if already exists
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_enter_new_ID)
        else:
            self.handler.R_id = self.id
            try:
                flag_date_of_birth = bool(datetime.strptime(self.date_of_birth,
                                                            format_date_of_birth))  # check if the user insert DOB currently
            except ValueError:
                flag_date_of_birth = False
            check_year = self.date_of_birth[-4:]
            if '/' in check_year or 'y' in check_year:
                flag_date_of_birth = False
            else:
                check_year = int(self.date_of_birth[-4:])
                if check_year < 1930:
                    flag_date_of_birth = False
            if not flag_date_of_birth:
                QApplication.restoreOverrideCursor()
                QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_enter_DOB)
            else:
                self.date_of_birth = pd.to_datetime(self.date_of_birth, format="%d/%m/%Y")
                self.date_of_birth = self.date_of_birth.strftime("%d/%m/%Y")
                if self.weight == '':  # check if the user didn't insert weight
                    QApplication.restoreOverrideCursor()
                    QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_weight)
                else:
                    if self.height == '':  # check if the user didn't insert height
                        QApplication.restoreOverrideCursor()
                        QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_height)
                    else:
                        if self.hernia_CB.isChecked():
                            self.hernia = 1
                        else:
                            self.hernia = 0
                        if self.waiting_for_date_CB.isChecked():
                            self.date = pd.NaT
                        else:
                            date = self.calendarWidget.selectedDate()
                            self.date = date.toPython()
                            self.date = self.date.strftime("%d/%m/%Y")

                        new_row = [self.id, self.name, self.telephone, self.email, self.date_of_birth, self.origen,
                                   self.weight, self.height,
                                   self.type, self.date, self.hernia, '', '', '']
                        new_row[9] = pd.to_datetime(new_row[9], format="%d/%m/%Y").date()
                        new_row[4] = pd.to_datetime(new_row[4], format="%d/%m/%Y").date()

                        df_first_meeting2 = self.handler.df_first_meeting.copy()
                        a_series = pd.Series(new_row, index=df_first_meeting2.columns)
                        df_first_meeting2 = df_first_meeting2.append(a_series, ignore_index=True)
                        # looping on all rows, the columns 4 and 9 (date of birth, date of procedure) changes to strftime
                        for index in df_first_meeting2.index: # for on all
                            df_first_meeting2.iat[index, 4] = df_first_meeting2.iat[index, 4].strftime("%d/%m/%Y")
                            if df_first_meeting2.iat[index, 9] is pd.NaT or isinstance(df_first_meeting2.iat[index, 9],
                                                                                       float):
                                continue
                            else:

                                df_first_meeting2.iat[index, 9] = df_first_meeting2.iat[index, 9].strftime("%d/%m/%Y")

                        self.handler.write_first_meeting_data_frame(df_first_meeting2)
                        new_row = [self.id, self.name, '', self.weight, '']
                        df_followUp2 = self.handler.df_followUp.copy()
                        a_series = pd.Series(new_row, index=df_followUp2.columns)
                        df_followUp2 = df_followUp2.append(a_series, ignore_index=True)
                        for index in df_followUp2.index:
                            if df_followUp2.iat[index, 2] is pd.NaT or isinstance(df_followUp2.iat[index, 2], float) or \
                                    isinstance(df_followUp2.iat[index, 2], str):
                                df_followUp2.iat[index, 2] = ''
                            else:
                                df_followUp2.iat[index, 2] = df_followUp2.iat[index, 2].strftime("%d/%m/%Y")
                        self.handler.write_follow_up(df_followUp2)
                        QApplication.restoreOverrideCursor()
                        if self.other_diseases_CB.isChecked():
                            self.move_to_other_diseases()

                        else:
                            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_new_P)
                            self.close()
                            self.parent.go_to_p_card()

    def move_to_other_diseases(self):
        self.setDisabled(True)
        self.other_d_window = other_diseases(self, self.handler)
        self.other_d_window.show()

    def move_main(self):
        self.close()
        self.parent.show()

    def finish_diseases(self):
        self.parent.go_to_p_card()
        self.close()

    def Messages(self):
        self.Message_enter_ID = 'Please enter ID'
        self.Message_enter_new_ID = 'ID already exists'
        self.Message_enter_DOB = 'Please enter date of birth'
        self.Message_new_P = 'New patient added'
        self.Message_weight = 'Please enter weight'
        self.Message_height = 'Please enter height'
        self.Message_Success = 'Success'
        self.Message_Fail = 'Fail'
