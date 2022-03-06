# general imports
from datetime import datetime, timedelta
# pyside2 imports
import PySide2
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Qt
from PySide2.QtGui import QIntValidator
from PySide2 import QtWidgets
# Ui imports
from Generated.add_follow_m import Ui_add_follow_m
# classes imports
from data_handler import *


class addFollow_m(QMainWindow, Ui_add_follow_m):
    def __init__(self, parent, handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.setupUi(self)
        self.handler = handler
        weight_validator = QIntValidator(50, 250, self)
        self.weight_edit.setValidator(weight_validator)
        self.get_date()
        self.setWindowTitle('Add Follow-Up Meeting')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.Messages()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.cancel_button_2.clicked.connect(self.close_this_window)
        self.sumbit_button.clicked.connect(self.submit_followUp)
        self.today_CB.stateChanged.connect(self.state_changed)
        self.add_m_calendarWidget.selectionChanged.connect(self.set_calender_date)

    def get_date(self):
        self.add_m_calendarWidget.hide()
        row_data = [self.handler.df_first_meeting.query('Cedula == @self.handler.R_id')]
        self.date_of_procedure = row_data[0].iloc[0][9]
        self.name = row_data[0].iloc[0][1]
        self.name_lable.setText(str(self.name))
        self.today_CB.setChecked(True)
        self.set_today_date()

    def set_today_date(self):
        today = datetime.now().date()
        formatted_today = pd.to_datetime(today).date()
        formatted_today = formatted_today.strftime("%d/%m/%Y")
        self.date_label.setText(str(formatted_today))

    def state_changed(self, int):
        if self.today_CB.isChecked():
            self.add_m_calendarWidget.hide()
            self.set_today_date()
        else:
            self.add_m_calendarWidget.show()
            self.set_calender_date()

    def set_calender_date(self):
        cal_date = self.add_m_calendarWidget.selectedDate()
        self.new_date = cal_date.toPython()
        self.new_date = self.new_date.strftime("%d/%m/%Y")
        self.date_label.setText(str(self.new_date))

    def submit_followUp(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.date = self.date_label.text()
        self.date = pd.to_datetime(self.date, format="%d/%m/%Y")
        if self.date > pd.Timestamp(self.date_of_procedure):
            self.date = self.date.strftime("%d/%m/%Y")
            self.weight = self.weight_edit.text()
            self.name = \
                list(self.handler.df_first_meeting.loc[self.handler.df_first_meeting['Cedula'] == self.handler.R_id][
                         'Nombre'])[
                    0]
            self.anoc = self.anoc_edit.toPlainText()
            new_row = [self.handler.R_id, self.name, self.date, self.weight, self.anoc]
            new_row[2] = pd.to_datetime(new_row[2], format="%d/%m/%Y")
            df_followUp2 = self.handler.df_followUp.copy()
            a_series = pd.Series(new_row, index=df_followUp2.columns)
            df_followUp2 = df_followUp2.append(a_series, ignore_index=True)
            for index in df_followUp2.index:
                if df_followUp2.iat[index, 2] is pd.NaT or isinstance(df_followUp2.iat[index, 2], float):
                    df_followUp2.iat[index, 2] = ''
                else:
                    df_followUp2.iat[index, 2] = df_followUp2.iat[index, 2].strftime("%d/%m/%Y")
            self.handler.write_follow_up(df_followUp2)
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_new_meeting_added)
            self.parent.progress_table.selectionModel().clear()
            self.close()
            self.parent.re_open_this_window_T2()
        else:
            QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_insert_before_procedure)

    def close_this_window(self):
        self.close()
        self.parent.ShowFollowUp()

    def Messages(self):
        self.Message_new_meeting_added = 'new meeting added'
        self.Message_insert_before_procedure = "Can't insert meeting before the procedure"
        self.Message_Success = 'Success'
        self.Message_Fail = 'Fail'