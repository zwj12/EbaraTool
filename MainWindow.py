import sys, logging
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Ui.Ui_MainWindow import Ui_MainWindow
from NetworkScanningDialog import NetworkScanningDialog
from zeroconf import ServiceBrowser, Zeroconf, ZeroconfServiceTypes
from web_service_connection import WebServiceConnection
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
        self.ui.pushButton_RequestWriteAccess.clicked.connect(self.request_write_access)
        self.ui.pushButton_ReleaseWriteAccess.clicked.connect(self.release_write_access)
        self.ui.pushButton_Update.clicked.connect(self.update_data)
        self.pipe_groove_model = PipeGrooveModel()

    def add_controller(self):
        network_scanning_dialog = NetworkScanningDialog()
        if network_scanning_dialog.exec_() == QDialog.Accepted:
            self.status_ipaddress.setText('IP Address：{0}'.format(WebServiceConnection.get_host()))
            self.status_connection.setText('Connection: Connected')
            self.pipe_groove_model.get_data_from_web_service()
            print(self.pipe_groove_model.to_string())
            self.ui.lineEdit_Index.setText(str(self.pipe_groove_model.num_index))
            self.ui.lineEdit_BranchGrooveAngle.setText(str(self.pipe_groove_model.num_revise_scan_branch_type))
            self.ui.lineEdit_BranchGrooveRoot.setText(str(self.pipe_groove_model.num_branch_groove_root))
            self.ui.lineEdit_GrooveGap.setText(str(self.pipe_groove_model.num_groove_gap))
            self.ui.lineEdit_SeamCenterX.setText(str(self.pipe_groove_model.num_seam_centerX))
            self.ui.lineEdit_SeamNormalAngle.setText(str(self.pipe_groove_model.num_seam_normal_angle))
            self.ui.lineEdit_WeldLegWidth.setText(str(self.pipe_groove_model.num_weld_leg_width))
        else:
            logging.basicConfig(filename='example1.log', level=logging.DEBUG, style='{'
                                ,format='{asctime}:{levelname}:{message}')
            logging.debug('This message should go to the log file')
            logging.info('So should this')
            logging.warning('And this, too')
            logging.warning('%s before you %s', 'Look', 'leap!',
                            exc_info=True, stack_info=True,  extra={'user': 'Tom', 'ip': '47.98.53.222'})
            logging.log()
            # logging.warning("{0} before you ", "Look")

    def update_data(self):
        self.pipe_groove_model.num_index = float(self.ui.lineEdit_Index.text())
        self.pipe_groove_model.num_revise_scan_branch_type = float(self.ui.lineEdit_BranchGrooveAngle.text())
        self.pipe_groove_model.num_branch_groove_root = float(self.ui.lineEdit_BranchGrooveRoot.text())
        self.pipe_groove_model.num_groove_gap = float(self.ui.lineEdit_GrooveGap.text())
        self.pipe_groove_model.num_seam_centerX = float(self.ui.lineEdit_SeamCenterX.text())
        self.pipe_groove_model.num_seam_normal_angle = float(self.ui.lineEdit_SeamNormalAngle.text())
        self.pipe_groove_model.num_weld_leg_width = float(self.ui.lineEdit_WeldLegWidth.text())
        self.pipe_groove_model.set_data_to_web_service()

    def request_write_access(self):
        WebServiceConnection.request_manual_mode_privileges()
        # WebServiceConnection.request_master_ship()

    def release_write_access(self):
        WebServiceConnection.cancel_manual_mode_privileges()
        # WebServiceConnection.release_master_ship()

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
