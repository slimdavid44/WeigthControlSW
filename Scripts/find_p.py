# pyside2 imports
import PySide2
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QTableView, QAbstractItemView, QGraphicsColorizeEffect
from PySide2 import QtWidgets
# Ui imports
from Generated.findP import Ui_findP
# classes imports
from patient_card import Patient_card


class findP(QMainWindow, Ui_findP):

    def __init__(self, parent, handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.handler = handler
        self.p_card = 0
        self.setupUi(self)
        self.select_Button.hide()
        self.table_P.setColumnCount(2)
        self.table_P.setHorizontalHeaderItem(0, QTableWidgetItem('id'))
        self.table_P.setHorizontalHeaderItem(1, QTableWidgetItem('name'))
        self.table_P.setRowCount(1)
        self.table_P.setSelectionBehavior(QTableView.SelectRows)  # set select all row in the table by clicking
        self.table_P.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Prevent user from changing values
        self.setWindowTitle('Find Patient')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.Messages()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.lineEdit_id.returnPressed.connect(self.pushButton_submit.click)
        self.lineEdit_name.returnPressed.connect(self.pushButton_submit.click)
        self.pushButton_submit.clicked.connect(self.search)
        self.main_Button.clicked.connect(self.move_main)
        self.table_P.itemClicked.connect(self.enabled_select)
        self.select_Button.clicked.connect(self.Get_requested_id)

    def search(self):
        self.select_Button.hide()
        self.color_effect = QGraphicsColorizeEffect()
        self.table_P.clear()
        self.table_P.setHorizontalHeaderItem(0, QTableWidgetItem('id'))
        self.table_P.setHorizontalHeaderItem(1, QTableWidgetItem('name'))
        # get id and name from user
        id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        self.lineEdit_id.clear()
        self.lineEdit_name.clear()
        # check if the user insert id number
        if id != '':
            result = self.handler.df_first_meeting.loc[
                self.handler.df_first_meeting['Cedula'] == id, ['Cedula', 'Nombre']]
            if result.empty:
                self.lineEdit_id.clear()
                QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_ID_not_exist )
            else:
                for column in range(self.table_P.columnCount()):
                    self.table_P.setItem(0, column, QtWidgets.QTableWidgetItem(str(result.iloc[0, column])))
        else:
            result = self.handler.df_first_meeting[
                self.handler.df_first_meeting['Nombre'].str.contains(name, case=False, na=False)]
            result = result[['Cedula', 'Nombre']]
            # In case the user entered a name that does not exist in the system
            if len(result) == 0:
                QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_name_not_exist)
                self.lineEdit_name.clear()
                self.table_P.setRowCount(1)
            else:
                self.table_P.setRowCount(len(result.index))  # set row number as the len og results
                for row in range(self.table_P.rowCount()):
                    for column in range(self.table_P.columnCount()):
                        self.table_P.setItem(row, column, QtWidgets.QTableWidgetItem(str(result.iloc[row, column])))
        self.table_P.doubleClicked.connect(self.Get_requested_id)

    def enabled_select(self):
        self.select_Button.show()

    def Get_requested_id(self):
        index = (self.table_P.selectionModel().currentIndex())
        if index.sibling(index.row(), 0).data():
            self.handler.Update_R_id(index.sibling(index.row(), 0).data())
            self.select_Button.hide()
            self.move_to_P_card()
        else:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_select_row)

    def move_to_P_card(self):
        self.close()
        if isinstance(self.p_card, Patient_card):
            self.p_card.re_open_this_window()

        else:
            self.p_card = Patient_card(self, self.handler)
            self.p_card.show()

    def move_main(self):
        self.close()
        self.parent.show()

    def re_show(self):
        self.show()

    def Messages(self):
        self.Message_select_row = 'First select a row please'
        self.Message_name_not_exist = 'the name does not exist in the system'
        self.Message_ID_not_exist = 'the id does not exist in the system'
        self.Message_Fail = 'Fail'