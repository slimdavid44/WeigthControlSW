# pyside2 imports
import PySide2
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets
# Ui imports
from Generated.log_in_form import Ui_log_in_form





class login_window(QWidget, Ui_log_in_form):
    # constructor to this window
    def __init__(self, main, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_window1 = main
        self.setupUi(self)
        self.password_edit.returnPressed.connect(self.login_button.click)  # after pressing Enter try to log in
        self.login_button.clicked.connect(self.password_verification)
        self.setWindowTitle('Login')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.Message_fail_log_in = 'Try again'

    def password_verification(self):
        # get user id and password from user
        insert_name = self.user_edit.text()
        insert_password = self.password_edit.text()
        # check if user id and password are correct
        if (insert_name == '1' and insert_password == '1'):
            self.close()
            self.move_to_main_window()
        else:
            QtWidgets.QMessageBox.information(self, 'Fail', self.Message_fail_log_in)

    def move_to_main_window(self):
        self.main_window1.show()
