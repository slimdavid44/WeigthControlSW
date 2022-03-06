# general imports
import sys
import os
# pyside2 imports
import PySide2
from PySide2.QtWidgets import *
# classes imports
from login import login_window
from main_window import MainWindow

# access to plugin
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    main = MainWindow()
    login_window = login_window(main)
    login_window.show()
    sys.exit(app.exec_())
