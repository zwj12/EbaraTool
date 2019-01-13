# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui',
# licensing of 'Ui_MainWindow.ui' applies.
#
# Created: Sun Jan 13 16:20:28 2019
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1542405709
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_Controller = QtWidgets.QMenu(self.menubar)
        self.menu_Controller.setObjectName("menu_Controller")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_AddController = QtWidgets.QAction(MainWindow)
        self.action_AddController.setObjectName("action_AddController")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_View_statusbar = QtWidgets.QAction(MainWindow)
        self.action_View_statusbar.setCheckable(True)
        self.action_View_statusbar.setChecked(True)
        self.action_View_statusbar.setObjectName("action_View_statusbar")
        self.menu_Controller.addAction(self.action_AddController)
        self.menu_Controller.addAction(self.action_Exit)
        self.menu_View.addAction(self.action_View_statusbar)
        self.menubar.addAction(self.menu_Controller.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.toolBar.addAction(self.action_AddController)
        self.toolBar.addAction(self.action_Exit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Exit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.menu_Controller.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Controller", None, -1))
        self.menu_View.setTitle(QtWidgets.QApplication.translate("MainWindow", "&View", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.action_AddController.setText(QtWidgets.QApplication.translate("MainWindow", "&Add Controller", None, -1))
        self.action_AddController.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+A", None, -1))
        self.action_Exit.setText(QtWidgets.QApplication.translate("MainWindow", "&Exit", None, -1))
        self.action_Exit.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Exit application", None, -1))
        self.action_Exit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.action_View_statusbar.setText(QtWidgets.QApplication.translate("MainWindow", "View statusbar", None, -1))
        self.action_View_statusbar.setToolTip(QtWidgets.QApplication.translate("MainWindow", "View statusbar", None, -1))

