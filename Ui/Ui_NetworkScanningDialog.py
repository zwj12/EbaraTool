# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_NetworkScanningDialog.ui',
# licensing of 'Ui_NetworkScanningDialog.ui' applies.
#
# Created: Sat Jan 12 21:27:09 2019
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1542405709
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NetworkScanningDialog(object):
    def setupUi(self, NetworkScanningDialog):
        NetworkScanningDialog.setObjectName("NetworkScanningDialog")
        NetworkScanningDialog.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ebara-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NetworkScanningDialog.setWindowIcon(icon)
        self.gridLayout_Dialog = QtWidgets.QGridLayout(NetworkScanningDialog)
        self.gridLayout_Dialog.setObjectName("gridLayout_Dialog")
        self.label = QtWidgets.QLabel(NetworkScanningDialog)
        self.label.setObjectName("label")
        self.gridLayout_Dialog.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_button = QtWidgets.QGridLayout()
        self.gridLayout_button.setObjectName("gridLayout_button")
        self.pushButton_refresh = QtWidgets.QPushButton(NetworkScanningDialog)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout_button.addWidget(self.pushButton_refresh, 0, 0, 1, 1)
        self.checkBox_showVirtual = QtWidgets.QCheckBox(NetworkScanningDialog)
        self.checkBox_showVirtual.setObjectName("checkBox_showVirtual")
        self.gridLayout_button.addWidget(self.checkBox_showVirtual, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(NetworkScanningDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_button.addWidget(self.buttonBox, 0, 2, 1, 1)
        self.gridLayout_Dialog.addLayout(self.gridLayout_button, 3, 0, 1, 1)
        self.tableWidget_controllerInfo = QtWidgets.QTableWidget(NetworkScanningDialog)
        self.tableWidget_controllerInfo.setColumnCount(9)
        self.tableWidget_controllerInfo.setObjectName("tableWidget_controllerInfo")
        self.tableWidget_controllerInfo.setColumnCount(9)
        self.tableWidget_controllerInfo.setRowCount(0)
        self.tableWidget_controllerInfo.horizontalHeader().setMinimumSectionSize(31)
        self.tableWidget_controllerInfo.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_controllerInfo.verticalHeader().setMinimumSectionSize(23)
        self.gridLayout_Dialog.addWidget(self.tableWidget_controllerInfo, 1, 0, 1, 1)
        self.gridLayout_tool = QtWidgets.QGridLayout()
        self.gridLayout_tool.setObjectName("gridLayout_tool")
        self.groupBox_filer = QtWidgets.QGroupBox(NetworkScanningDialog)
        self.groupBox_filer.setObjectName("groupBox_filer")
        self.comboBox_filter = QtWidgets.QComboBox(self.groupBox_filer)
        self.comboBox_filter.setGeometry(QtCore.QRect(30, 20, 150, 25))
        self.comboBox_filter.setCurrentText("")
        self.comboBox_filter.setObjectName("comboBox_filter")
        self.lineEdit_filter = QtWidgets.QLineEdit(self.groupBox_filer)
        self.lineEdit_filter.setGeometry(QtCore.QRect(200, 20, 150, 25))
        self.lineEdit_filter.setText("")
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.gridLayout_tool.addWidget(self.groupBox_filer, 0, 1, 1, 1)
        self.groupBox_IPAddress = QtWidgets.QGroupBox(NetworkScanningDialog)
        self.groupBox_IPAddress.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox_IPAddress.setObjectName("groupBox_IPAddress")
        self.lineEdit_remoteIPAddress = QtWidgets.QLineEdit(self.groupBox_IPAddress)
        self.lineEdit_remoteIPAddress.setGeometry(QtCore.QRect(20, 20, 150, 25))
        self.lineEdit_remoteIPAddress.setObjectName("lineEdit_remoteIPAddress")
        self.pushButton_addRemote = QtWidgets.QPushButton(self.groupBox_IPAddress)
        self.pushButton_addRemote.setGeometry(QtCore.QRect(190, 20, 75, 25))
        self.pushButton_addRemote.setObjectName("pushButton_addRemote")
        self.gridLayout_tool.addWidget(self.groupBox_IPAddress, 0, 0, 1, 1)
        self.gridLayout_Dialog.addLayout(self.gridLayout_tool, 2, 0, 1, 1)
        self.gridLayout_Dialog.setRowMinimumHeight(2, 60)
        self.gridLayout_Dialog.setRowMinimumHeight(3, 60)

        self.retranslateUi(NetworkScanningDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NetworkScanningDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NetworkScanningDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NetworkScanningDialog)

    def retranslateUi(self, NetworkScanningDialog):
        NetworkScanningDialog.setWindowTitle(QtWidgets.QApplication.translate("NetworkScanningDialog", "Network Scanning", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Available controllers on the network:", None, -1))
        self.pushButton_refresh.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Refresh", None, -1))
        self.checkBox_showVirtual.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Show Virtual Controllers", None, -1))
        self.groupBox_filer.setTitle(QtWidgets.QApplication.translate("NetworkScanningDialog", "Filter", None, -1))
        self.groupBox_IPAddress.setTitle(QtWidgets.QApplication.translate("NetworkScanningDialog", "Remote Controller", None, -1))
        self.pushButton_addRemote.setToolTip(QtWidgets.QApplication.translate("NetworkScanningDialog", "Add a remote controller", None, -1))
        self.pushButton_addRemote.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Add", None, -1))

