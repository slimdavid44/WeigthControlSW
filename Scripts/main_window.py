# general imports
import inspect
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
# pySide2 imports
import PySide2
from PySide2.QtCore import QTimer, QEvent
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QLCDNumber, QTableView, QAbstractItemView
from PySide2 import QtWidgets
# Ui imports
from Generated.main_window import Ui_MainWindow
# classes imports
from add_p import add_P
from data_handler import data_handler
from find_p import findP
from stats import stats


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.handler = data_handler()
        self.add_window = 0  # use for determine if window already exist
        self.find_window = 0
        self.stats_window = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.clock)
        self.timer.start(1000)
        self.five_serg()
        self.connectSignalsSlots()
        self.setWindowTitle('Main Window')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))

    def connectSignalsSlots(self):
        self.look_for_patient.clicked.connect(self.move_to_findP)
        self.add_newP.clicked.connect(self.move_to_addP)
        self.stats.clicked.connect(self.move_to_stats)

    def clock(self):
        time = datetime.now()
        formatted_time = time.strftime("%H:%M:%S")
        if formatted_time < "12:00:00":
            self.label_hello_dr.setText("Good Morning Dr.")

        elif formatted_time < "18:00:00":
            self.label_hello_dr.setText("Good Afternoon Dr.")
        else:
            self.label_hello_dr.setText("Good Evening Dr.")
        self.label_hello_dr.setStyleSheet("QLabel{color: #FBF8BE;}")
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.display(formatted_time)

    def five_serg(self):
        # display the next five surgeries
        self.tableWidget_S.setSelectionBehavior(QTableView.SelectRows)
        self.tableWidget_S.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_S.horizontalHeader().setStyleSheet("QTableWidget {color: #FBF8BE;}")
        self.tableWidget_S.setRowCount(5)
        self.tableWidget_S.setColumnCount(4)
        df_copy = self.handler.df_first_meeting.copy()
        today = datetime.now().date()
        subset = pd.DataFrame(columns=['Cedula', 'Nombre', 'Telefono', 'date'])  # the column I want to present
        formatted_today = pd.to_datetime(today).date()
        diff = (formatted_today - df_copy.date)
        diff_datetime = diff[(diff <= pd.to_timedelta(0))]
        diff_datetime = diff_datetime.to_frame()
        diff_int = (diff_datetime.iloc[:, 0] / np.timedelta64(1, 'D')).astype(int)
        # checks if there are any next surgeries
        if (any(x <= 0 for x in diff_int)):
            indexmax = (diff[(diff <= pd.to_timedelta(0))].idxmax())  # find the index that represent the closes date
            # create an entry for insert to the subset
            new_entry = {'Cedula': (df_copy.at[indexmax, 'Cedula']),
                         'Nombre': (df_copy.at[indexmax, 'Nombre']),
                         'Telefono': (df_copy.at[indexmax, 'Telefono']),
                         'date': (df_copy.at[indexmax, 'date']).strftime('%d/%m/%Y')}
            subset = subset.append(new_entry, ignore_index=True)
            # do this for 5 more time
            for i in range(1, 5):
                current_date = df_copy.at[indexmax, 'date']
                x = current_date - timedelta(days=10)
                df_copy.at[indexmax, 'date'] = x
                diff = (current_date - df_copy.date)
                diff_datetime = diff[(diff <= pd.to_timedelta(0))]
                diff_datetime = diff_datetime.to_frame()
                diff_int = (diff_datetime.iloc[:, 0] / np.timedelta64(1, 'D')).astype(int)
                if (any(x <= 0 for x in diff_int)):
                    indexmax2 = (diff[(diff <= pd.to_timedelta(0))].idxmax())
                    new_entry = {'Cedula': (df_copy.at[indexmax2, 'Cedula']),
                                 'Nombre': (df_copy.at[indexmax2, 'Nombre']),
                                 'Telefono': (df_copy.at[indexmax2, 'Telefono']),
                                 'date': (df_copy.at[indexmax2, 'date']).strftime('%d/%m/%Y')}
                    subset = subset.append(new_entry, ignore_index=True)
                    indexmax = indexmax2  # fix when there is two surgeries at the same day
                    self.tableWidget_S.setRowCount(i + 1)
                else:
                    self.tableWidget_S.setRowCount(i)
                    break
        else:
            self.tableWidget_S.setRowCount(0)
        # display the subset on table widget
        for row in range(self.tableWidget_S.rowCount()):
            for column in range(4):
                self.tableWidget_S.setItem(row, column, QtWidgets.QTableWidgetItem(str(subset.iloc[row, column])))

    def move_to_findP(self):
        self.close()  # close the main window
        if inspect.isclass(self.find_window):
            self.find_window.show()
        else:
            self.find_window = findP(self, self.handler)
            self.find_window.show()

    def move_to_addP(self):
        self.close()  # close the main window
        if inspect.isclass(self.add_window):
            self.add_window.show()
        else:
            self.add_window = add_P(self, self.handler)
            self.add_window.show()

    def move_to_stats(self):
        self.close()  # close the main window
        if inspect.isclass(self.stats_window):
            self.stats_window.show()
        else:
            self.stats_window = stats(self, self.handler)
            self.stats_window.show()

    def go_to_p_card(self):
        if inspect.isclass(self.find_window):
            self.find_window.move_to_P_card()
        else:
            self.find_window = findP(self, self.handler)
            self.find_window.move_to_P_card()

    def re_show(self):
        self.five_serg()
        self.show()