import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from NetworkScanningWindow import Ui_NetworkScanningDialog
from zeroconf import ServiceBrowser, Zeroconf
from zeroconf import ZeroconfServiceTypes


class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.ui = Ui_NetworkScanningDialog()
        self.ui.setupUi(self)
        # self.ui.tableWidget_controllerInfo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_controllerInfo.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.ui.tableWidget_controllerInfo.setColumnWidth(5, 200)
        self.ui.tableWidget_controllerInfo.setColumnWidth(7, 200)
        self.ui.tableWidget_controllerInfo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_controllerInfo.setHorizontalHeaderLabels(
            ['IP Address', 'SystemId', 'ID', 'Availability', 'Virtual'
                , 'System Name', 'RobotWare Version', 'Controller Name'])
        # self.ui.tableWidget_controllerInfo.setRowCount(4)
        self.current_row = 0
        # self.connect(self.ui.tableWidget_controllerInfo, SIGNAL(
        # "itemClicked (QTableWidgetItem)"), self.get_current_row)
        self.ui.tableWidget_controllerInfo.cellClicked.connect(self.get_current_row)
        self.zeroconf = Zeroconf()
        self.listener = MyListener(self)
        self.browser = ServiceBrowser(self.zeroconf, "_http._tcp.local.", self.listener)

    def get_current_row(self, row, column):
        self.current_row = row


class MyListener:
    def __init__(self, dialog):
        self.networkScanningDialog = dialog

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info.name.startswith("RobotWebServices_"):
            row_index = self.networkScanningDialog.ui.tableWidget_controllerInfo.rowCount()
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setRowCount(row_index + 1)
            table_item = QTableWidgetItem('{0}.{1}.{2}.{3}'.format(info.address[0],
                                                                   info.address[1], info.address[2], info.address[3]))
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 0, table_item)
            index_end = info.name.find("._http._tcp")
            table_item = QTableWidgetItem(info.name[17:index_end])
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 5, table_item)
            table_item = QTableWidgetItem(info.server)
            self.networkScanningDialog.ui.tableWidget_controllerInfo.setItem(row_index, 7, table_item)


class W1(QWidget):
    def __init__(self, parent=None):
        super(W1, self).__init__(parent)
        self.btn = QPushButton('Click1')
        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)
        self.btn.clicked.connect(self.fireupWindows2)

    def fireupWindows2(self):
        w2 = MainDialog()
        if w2.exec_() == QDialog.Accepted:
            print(w2.current_row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = W1()
    window.show()
    sys.exit(app.exec_())
