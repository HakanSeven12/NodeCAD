import sys

from PySide6 import QtWidgets

from mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())