# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NetworkScanningWindow.ui',
# licensing of 'NetworkScanningWindow.ui' applies.
#
# Created: Thu Jan 10 20:30:33 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NetworkScanningDialog(object):
    def setupUi(self, NetworkScanningDialog):
        NetworkScanningDialog.setObjectName("NetworkScanningDialog")
        NetworkScanningDialog.resize(800, 600)
        self.gridLayout_3 = QtWidgets.QGridLayout(NetworkScanningDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(NetworkScanningDialog)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_refresh = QtWidgets.QPushButton(NetworkScanningDialog)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout_2.addWidget(self.pushButton_refresh, 0, 0, 1, 1)
        self.checkBox_showVirtual = QtWidgets.QCheckBox(NetworkScanningDialog)
        self.checkBox_showVirtual.setObjectName("checkBox_showVirtual")
        self.gridLayout_2.addWidget(self.checkBox_showVirtual, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(NetworkScanningDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.tableWidget_controllerInfo = QtWidgets.QTableWidget(NetworkScanningDialog)
        self.tableWidget_controllerInfo.setColumnCount(8)
        self.tableWidget_controllerInfo.setObjectName("tableWidget_controllerInfo")
        self.tableWidget_controllerInfo.setColumnCount(8)
        self.tableWidget_controllerInfo.setRowCount(0)
        self.tableWidget_controllerInfo.horizontalHeader().setMinimumSectionSize(31)
        self.tableWidget_controllerInfo.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_controllerInfo.verticalHeader().setMinimumSectionSize(23)
        self.gridLayout_3.addWidget(self.tableWidget_controllerInfo, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(NetworkScanningDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_filter = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_filter.setGeometry(QtCore.QRect(30, 20, 150, 25))
        self.comboBox_filter.setCurrentText("")
        self.comboBox_filter.setObjectName("comboBox_filter")
        self.lineEdit_filter = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_filter.setGeometry(QtCore.QRect(200, 20, 150, 25))
        self.lineEdit_filter.setText("")
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(NetworkScanningDialog)
        self.groupBox.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_remoteIPAddress = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_remoteIPAddress.setGeometry(QtCore.QRect(20, 20, 150, 25))
        self.lineEdit_remoteIPAddress.setObjectName("lineEdit_remoteIPAddress")
        self.pushButton_addRemote = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_addRemote.setGeometry(QtCore.QRect(190, 20, 75, 25))
        self.pushButton_addRemote.setObjectName("pushButton_addRemote")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_3.setRowMinimumHeight(2, 60)
        self.gridLayout_3.setRowMinimumHeight(3, 60)

        self.retranslateUi(NetworkScanningDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NetworkScanningDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NetworkScanningDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NetworkScanningDialog)

    def retranslateUi(self, NetworkScanningDialog):
        NetworkScanningDialog.setWindowTitle(QtWidgets.QApplication.translate("NetworkScanningDialog", "Network Scanning", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Available controllers on the network:", None, -1))
        self.pushButton_refresh.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Refresh", None, -1))
        self.checkBox_showVirtual.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Show Virtual Controllers", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("NetworkScanningDialog", "Filter", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("NetworkScanningDialog", "Remote Controller", None, -1))
        self.pushButton_addRemote.setText(QtWidgets.QApplication.translate("NetworkScanningDialog", "Add", None, -1))

