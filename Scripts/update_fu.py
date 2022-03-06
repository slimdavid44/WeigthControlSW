# general imports
from datetime import datetime
# pyside2 imports
import PySide2
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtWidgets
# Ui imports
from Generated.update_FU import Ui_update_FU
# classes imports
from data_handler import *


class update_FU(QMainWindow, Ui_update_FU):
    def __init__(self, parent, handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.handler = handler
        self.parent = parent
        weight_validator = QIntValidator(50, 250, self)
        self.weight_edit_2.setValidator(weight_validator)
        self.set_data()
        self.setWindowTitle('Update Follow-Up Meeting')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.Messages()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.cancel_button_2.clicked.connect(self.close_this_window)
        self.sumbit_button.clicked.connect(self.submit_changes)
        self.today_CB_3.stateChanged.connect(self.state_changed)
        self.update_fu_calendarWidget.selectionChanged.connect(self.set_calender_date)

    def set_data(self):
        df_followUp2 = self.handler.df_followUp.copy()
        pd_R_date = self.handler.R_date
        self.pd_R_date = pd.to_datetime(pd_R_date, dayfirst=True).date()
        row = [df_followUp2.query('Cedula == @self.handler.R_id and Fecha == @self.pd_R_date')]
        row_data = [self.handler.df_first_meeting.query('Cedula == @self.handler.R_id')]
        self.date_of_procedure = row_data[0].iloc[0][9]
        R_date = row[0].iloc[0]['Fecha'].strftime("%d/%m/%Y")
        self.name = str(row[0].iloc[0]['Nombre'])
        self.name_label.setText(str(self.name))
        self.date_label.setText(str(R_date))
        self.weight_edit_2.setText(str(row[0].iloc[0]['Peso']))
        self.anoc_edit.setText(str(row[0].iloc[0]['Anotaciones']))

    def set_today_date(self):
        self.update_fu_calendarWidget.hide()
        today = datetime.now().date()
        formatted_today = pd.to_datetime(today).date()
        formatted_today = formatted_today.strftime("%d/%m/%Y")
        self.date_label.setText(str(formatted_today))

    def state_changed(self):
        if self.today_CB_3.isChecked():
            self.update_fu_calendarWidget.hide()
            self.set_today_date()
        else:
            self.update_fu_calendarWidget.show()
            self.set_calender_date()

    def set_calender_date(self):
        cal_date = self.update_fu_calendarWidget.selectedDate()
        self.new_date = cal_date.toPython()
        self.new_date = self.new_date.strftime("%d/%m/%Y")
        self.date_label.setText(str(self.new_date))

    def submit_changes(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.date = self.date_label.text()
        self.date = pd.to_datetime(self.date, format="%d/%m/%Y")
        if self.date > pd.Timestamp(self.date_of_procedure):
            self.date = self.date.strftime("%d/%m/%Y")
            df_followUp2 = self.handler.df_followUp.copy()
            for x in df_followUp2.index:
                if df_followUp2.iat[x, 2] is pd.NaT or isinstance(df_followUp2.iat[x, 2], float):
                    df_followUp2.iat[x, 2] = ''
                else:
                    df_followUp2.iat[x, 2] = df_followUp2.iat[x, 2].strftime("%d/%m/%Y")
            indexNames = df_followUp2[
                (df_followUp2['Cedula'] == self.handler.R_id) & (df_followUp2['Fecha'] == self.handler.R_date)].index

            df_followUp2.drop(indexNames, inplace=True)

            self.weight = self.weight_edit_2.text()
            self.anoc = self.anoc_edit.toPlainText()
            new_row = [self.handler.R_id, self.name, self.date, self.weight, self.anoc]
            a_series = pd.Series(new_row, index=df_followUp2.columns)
            df_followUp2 = df_followUp2.append(a_series, ignore_index=True)
            self.handler.write_follow_up(df_followUp2)
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_update_successes)
            self.parent.progress_table.selectionModel().clear()
            self.close()
            self.parent.re_open_this_window_T2()
        else:
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_update_before_procedure)



    def close_this_window(self):
        self.close()
        self.parent.ShowFollowUp()


    def Messages(self):
        self.Message_update_successes = 'updating the meeting ends with successes'
        self.Message_update_before_procedure = "Can't update meeting before the procedure"
        self.Message_Success = 'Success'
        self.Message_Fail = 'Fail'