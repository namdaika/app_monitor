# Author Nam Nguyen Hoai
import sys

import gui
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    monitor_app = QtWidgets.QMainWindow()
    ui = gui.MonitorApp()
    ui.setup(monitor_app)
    monitor_app.show()
    sys.exit(app.exec_())
