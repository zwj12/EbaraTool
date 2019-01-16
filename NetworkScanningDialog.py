import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Ui.Ui_NetworkScanningDialog import Ui_NetworkScanningDialog
from zeroconf import ServiceBrowser, Zeroconf, ZeroconfServiceTypes
from web_service_connection import WebServiceConnection


class NetworkScanningDialog(QDialog):
    def __init__(self):
        super(NetworkScanningDialog, self).__init__()
        self.ui = Ui_NetworkScanningDialog()
        self.ui.setupUi(self)
        # self.ui.tableWidget_controllerInfo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_controllerInfo.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.ui.tableWidget_controllerInfo.setColumnWidth(0, 100)
        self.ui.tableWidget_controllerInfo.setColumnWidth(1, 40)
        self.ui.tableWidget_controllerInfo.setColumnWidth(2, 300)
        self.ui.tableWidget_controllerInfo.setColumnWidth(5, 50)
        self.ui.tableWidget_controllerInfo.setColumnWidth(6, 200)
        self.ui.tableWidget_controllerInfo.setColumnWidth(8, 200)
        self.ui.tableWidget_controllerInfo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_controllerInfo.setHorizontalHeaderLabels(
            ['IP Address', 'Port', 'SystemId', 'ID', 'Availability', 'Virtual'
                , 'System Name', 'RobotWare Version', 'Controller Name'])
        self.ui.tableWidget_controllerInfo.setRowCount(0)
        self.ui.tableWidget_controllerInfo.cellClicked.connect(self.get_current_row)
        self.ui.tableWidget_controllerInfo.cellDoubleClicked.connect(
            self.table_controllerInfo_cellDoubleClicked)
        self.zeroconf = Zeroconf()
        self.listener = MyListener(self)
        self.browser = ServiceBrowser(self.zeroconf, "_http._tcp.local.", self.listener)
        self.current_row = 0

    def get_current_row(self, row, column):
        self.current_row = row

    def table_controllerInfo_cellDoubleClicked(self, row, column):
        self.current_row = row
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to connect this controller?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.accept()


class MyListener:
    def __init__(self, dialog):
        self.networkScanningDialog = dialog

    def remove_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info.name.startswith("RobotWebServices_"):
            ip_address = '{0}.{1}.{2}.{3}'.format(info.address[0], info.address[1], info.address[2], info.address[3])
            index_end = info.name.find("._http._tcp")
            system_name = info.name[17:index_end]
            items = self.networkScanningDialog.ui.tableWidget_controllerInfo.findItems(ip_address, Qt.MatchExactly)
            if len(items) > 0:
                for item in items:
                    # self.networkScanningDialog.ui.tableWidget_controllerInfo.removeRow(item.row())
                    item_system_name = \
                        self.networkScanningDialog.ui.tableWidget_controllerInfo.item(item.row(), 6).text()
                    if item_system_name == system_name:
                        self.networkScanningDialog.ui.tableWidget_controllerInfo.removeRow(item.row())

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info.name.startswith("RobotWebServices_"):
            row_index = self.networkScanningDialog.ui.tableWidget_controllerInfo.rowCount()
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setRowCount(row_index + 1)
            ip_address = '{0}.{1}.{2}.{3}'.format(info.address[0], info.address[1], info.address[2], info.address[3])
            table_item = QTableWidgetItem(ip_address)
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 0, table_item)
            table_item = QTableWidgetItem('{0}'.format(info.port))
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 1, table_item)
            # index_end = info.name.find("._http._tcp")
            # table_item = QTableWidgetItem(info.name[17:index_end])
            # self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 6, table_item)
            # table_item = QTableWidgetItem(info.server)
            # self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 8, table_item)
            username = "Default User"
            password = "robotics"
            web_service_connection = WebServiceConnection(ip_address, info.port, username, password)
            check_box = QTableWidgetItem()
            if WebServiceConnection.get_ctrl_type() == True:
                check_box.setCheckState(Qt.Checked)
            else:
                check_box.setCheckState(Qt.Unchecked)
                check_box.setFlags(check_box.flags() & (~Qt.ItemIsEnabled))
                table_item = QTableWidgetItem(WebServiceConnection.get_ctrl_id())
                self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 3, table_item)
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 5, check_box)
            table_item = QTableWidgetItem(WebServiceConnection.get_system_guid())
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 2, table_item)
            table_item = QTableWidgetItem(WebServiceConnection.get_rw_version())
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 7, table_item)
            table_item = QTableWidgetItem(WebServiceConnection.get_system_name())
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 6, table_item)
            table_item = QTableWidgetItem(WebServiceConnection.get_ctrl_name())
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 8, table_item)

