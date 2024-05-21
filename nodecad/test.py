import sys
import ryven
import pathlib

from qtpy.QtCore import Qt, QTimer, QCoreApplication
from qtpy.QtGui import QGuiApplication, QIcon
from qtpy.QtWidgets import QApplication, QMainWindow, QDockWidget

from pyqtribbon import RibbonBar

from OCC.Display.backend import load_backend
load_backend("pyside2")

from OCC.Display.qtDisplay import qtViewer3d
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

class MainWindow(QMainWindow):

    def __init__(self,app):

        super().__init__()
        self.setWindowTitle("NodeCAD")
        self.app = app

        self.ribbonmenu()
        self.canvas()
        self.ryven_dock(app)
        self.center_screen()

        QTimer.singleShot(100, self.showMaximized)

    def ribbonmenu(self):
        ribbonbar = RibbonBar()
        self.setMenuBar(ribbonbar)

        # Categories
        category1 = ribbonbar.addCategory("Test")
        panel1 = category1.addPanel("Box")

        disp = panel1.addLargeButton("Display Box", QIcon("python.png"))
        disp.clicked.connect(self.displayBOX)

        eras = panel1.addLargeButton("Erase Box", QIcon("python.png"))
        eras.clicked.connect(self.eraseBOX)

    def canvas(self):
        self.canvas = qtViewer3d(self)
        self.canvas.InitDriver()
        self.app.display = self.canvas._display
        self.setCentralWidget(self.canvas)

    def ryven_dock(self,app):
        ryven_main = ryven.run_ryven(
            qt_app=app, 
            gui_parent=self.canvas, 
            nodes=[pathlib.Path('PythonOCC')],
            show_dialog=False)

        self.ryven_widget = QDockWidget(self)
        self.ryven_widget.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.ryven_widget.setWidget(ryven_main)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.ryven_widget)


    def center_screen(self) -> None:
        """Centers the window on the screen."""
        geometry = self.frameGeometry()
        center = QGuiApplication.primaryScreen().availableGeometry().center()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def displayBOX(self):
        a_box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
        self.ais_box = self.display.DisplayShape(a_box)[0]
        self.display.FitAll()

    def eraseBOX(self):
        self.display.Context.Erase(self.ais_box, True)

class NodeCAD(QApplication):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display = None
        self.main_window = MainWindow(app=self)
        self.main_window.show()

if __name__ == '__main__':
    app = NodeCAD(sys.argv)
    sys.exit(app.exec_())