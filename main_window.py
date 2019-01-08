import sys
from PySide2 import QtCore, QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ebara Tool')
        self.grid = QtWidgets.QGridLayout()
        names = ['1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16',
                 '17', '18', '19', '20']
        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3),
               (4, 0), (4, 1), (4, 2), (4, 3)]
        for i in names:
            button = QtWidgets.QPushButton(i)
            self.grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1
        self.setLayout(self.grid)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
