# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

import app
import threading
import time
import multiprocessing

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


class MonitorApp(StoppableThread):
    """This app to monitor an service"""
    def setup(self, MonitorApp):
        MonitorApp.setObjectName("MonitorApp")
        MonitorApp.resize(640, 300)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MonitorApp.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MonitorApp)
        self.centralWidget.setObjectName("centralWidget")
        self.ButtonRunning = QtWidgets.QPushButton(self.centralWidget)
        self.ButtonRunning.setGeometry(QtCore.QRect(490, 190, 101, 31))
        self.ButtonRunning.setCheckable(False)
        self.ButtonRunning.setObjectName("ButtonRunning")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 371, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.VerticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.VerticalLayout.setContentsMargins(11, 11, 11, 11)
        self.VerticalLayout.setSpacing(8)
        self.VerticalLayout.setObjectName("VerticalLayout")
        self.HorizontalLayoutPort_2 = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutPort_2.setContentsMargins(11, 11, 11, 11)
        self.HorizontalLayoutPort_2.setSpacing(10)
        self.HorizontalLayoutPort_2.setObjectName("HorizontalLayoutPort_2")
        self.LabelPort = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelPort.setFont(font)
        self.LabelPort.setObjectName("LabelPort")
        self.HorizontalLayoutPort_2.addWidget(self.LabelPort)
        self.LineEditPort = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LineEditPort.setFont(font)
        self.LineEditPort.setObjectName("LineEditPort")
        self.HorizontalLayoutPort_2.addWidget(self.LineEditPort)
        self.VerticalLayout.addLayout(self.HorizontalLayoutPort_2)
        self.HorizontalLayoutName = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutName.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.HorizontalLayoutName.setContentsMargins(0, 11, 0, 0)
        self.HorizontalLayoutName.setSpacing(10)
        self.HorizontalLayoutName.setObjectName("HorizontalLayoutName")
        self.LabelName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelName.setFont(font)
        self.LabelName.setObjectName("LabelName")
        self.HorizontalLayoutName.addWidget(self.LabelName)
        self.LineEditName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LineEditName.setFont(font)
        self.LineEditName.setObjectName("LineEditName")
        self.HorizontalLayoutName.addWidget(self.LineEditName)
        self.VerticalLayout.addLayout(self.HorizontalLayoutName)
        self.layoutWidget.raise_()
        self.ButtonRunning.raise_()
        MonitorApp.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MonitorApp)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menuBar.setObjectName("menuBar")
        self.MainMenuEdit = QtWidgets.QMenu(self.menuBar)
        self.MainMenuEdit.setObjectName("MainMenuEdit")
        MonitorApp.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MonitorApp)
        self.mainToolBar.setObjectName("mainToolBar")
        MonitorApp.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MonitorApp)
        self.statusBar.setObjectName("statusBar")
        MonitorApp.setStatusBar(self.statusBar)
        self.actionPort = QtWidgets.QAction(MonitorApp)
        self.actionPort.setObjectName("actionPort")
        self.MenuExit = QtWidgets.QAction(MonitorApp)
        self.MenuExit.setObjectName("MenuExit")
        self.MainMenuEdit.addAction(self.MenuExit)
        self.menuBar.addAction(self.MainMenuEdit.menuAction())

        self.retranslate(MonitorApp)
        self.MenuExit.triggered.connect(MonitorApp.close)
        QtCore.QMetaObject.connectSlotsByName(MonitorApp)

        self.ButtonRunning.clicked.connect(self.on_click_button)

    def retranslate(self, MonitorApp):
        _translate = QtCore.QCoreApplication.translate
        MonitorApp.setWindowTitle(_translate("MonitorApp", "Monitor Application"))
        self.ButtonRunning.setText(_translate("MonitorApp", "Run"))
        self.LabelPort.setText(_translate("MonitorApp", "Port server"))
        self.LabelName.setText(_translate("MonitorApp", "Name server"))
        self.MainMenuEdit.setTitle(_translate("MonitorApp", "Edit"))
        self.actionPort.setText(_translate("MonitorApp", "Port"))
        self.MenuExit.setText(_translate("MonitorApp", "Exit"))
        self.MenuExit.setShortcut(_translate("MonitorApp", "Ctrl+E"))

    def on_click_button(self):
        foo = self.ButtonRunning.text()
        if foo == 'Run':
            self.start_app()
        else:
            self.stop_app()

    def start_app(self):
        port = self.LineEditPort.text()
        self.app_server = multiprocessing.Process(target=app.run_server,
                                                  args=(port,))
        # self.app_server = threading.Thread(target=app.run_server, args=(port,))
        # self.app_server.daemon = True
        self.app_server.start()
        time.sleep(3)
        self.ButtonRunning.setText('Stop')

    def stop_app(self):
        self.app_server.terminate()
        self.app_server.join()
        time.sleep(3)
        self.ButtonRunning.setText('Run')
