import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Ui.Ui_MainWindow import Ui_MainWindow
from NetworkScanningDialog import NetworkScanningDialog
from zeroconf import ServiceBrowser, Zeroconf, ZeroconfServiceTypes
from webserviceconnection import WebServiceConnection
from pipe_groove_model import PipeGrooveModel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready')
        self.status_ipaddress = QLabel('IP Address：')
        self.status_connection = QLabel('Connection: Not Connected')
        self.status_bar.addPermanentWidget(self.status_ipaddress, stretch=3)
        self.status_bar.addPermanentWidget(self.status_connection, stretch=1)
        self.ui.action_AddController.triggered.connect(self.add_controller)
        self.ui.action_View_statusbar.triggered.connect(self.toggle_menu)

    def add_controller(self):
        network_scanning_dialog = NetworkScanningDialog()
        if network_scanning_dialog.exec_() == QDialog.Accepted:
            self.status_ipaddress.setText('IP Address：{0}'.format(WebServiceConnection.get_host()))
            self.status_connection.setText('Connection: Connected')
            pipe_groove_model = PipeGrooveModel()
            pipe_groove_model.get_data_from_web_service()
            print(pipe_groove_model.to_string())

    def toggle_menu(self, state):
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
