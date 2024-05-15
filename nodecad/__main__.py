import sys

from PySide6 import QtWidgets

from mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow("ribbonbar.png")
    window.showMaximized()
    window.show()

    sys.exit(app.exec_())