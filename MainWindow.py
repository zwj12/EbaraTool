import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Ui.Ui_MainWindow import Ui_MainWindow
from NetworkScanningDialog import NetworkScanningDialog
from zeroconf import ServiceBrowser, Zeroconf, ZeroconfServiceTypes
from webserviceconnection import WebServiceConnection


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready')
        self.comNum = QLabel('串口号：')
        self.baudNum = QLabel('波特率:')
        self.status_bar.addPermanentWidget(self.comNum, stretch=3)
        self.status_bar.addPermanentWidget(self.baudNum, stretch=1)
        self.ui.action_AddController.triggered.connect(self.add_controller)
        self.ui.action_View_statusbar.triggered.connect(self.toggle_menu)

    def add_controller(self):
        network_scanning_dialog = NetworkScanningDialog()
        if network_scanning_dialog.exec_() == QDialog.Accepted:
            print(WebServiceConnection.get_system_name())

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
