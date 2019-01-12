import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from NetworkScanningDialog import NetworkScanningDialog
from zeroconf import ServiceBrowser, Zeroconf
from zeroconf import ZeroconfServiceTypes


class W1(QWidget):
    def __init__(self, parent=None):
        super(W1, self).__init__(parent)
        self.btn = QPushButton('Click1')
        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)
        self.btn.clicked.connect(self.fireupWindows2)

    def fireupWindows2(self):
        w2 = NetworkScanningDialog()
        if w2.exec_() == QDialog.Accepted:
            print(w2.current_row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = W1()
    window.show()
    sys.exit(app.exec_())
