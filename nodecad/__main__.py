import sys

from qtpy.QtWidgets import QApplication
from main_window import MainWindow

class NodeCAD(QApplication):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display = None
        self.main_window = MainWindow(app=self)
        self.main_window.show()

if __name__ == '__main__':
    app = NodeCAD(sys.argv)
    sys.exit(app.exec_())