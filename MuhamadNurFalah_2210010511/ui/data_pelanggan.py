from PyQt6 import QtWidgets, uic
import sys

class app5f(QtWidgets.QMainWindow):
    def __init__(self):
        super(app5f, self).__init__()
        uic.loadUi('data_pelanggan.ui', self)

if __name__ == '__main__':
    aplikasiku = QtWidgets.QApplication(sys.argv)
    jendela = app5f()
    jendela.show()

    sys.exit(aplikasiku.exec())