from PySide6.QtWidgets import (
    QMainWindow
)

from PySide6.QtGui import (
    QIcon,
    QGuiApplication
)

from PySide6.QtCore import (
    QTimer
)

from pyqtribbon import RibbonBar

from OCC.Display.backend import load_backend

load_backend("pyside6")
from OCC.Display.qtDisplay import qtViewer3d 
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NodeCAD")
        self.init_ui()
        
    def init_ui(self):
        self.set_canvas()
        self.set_ribbonmenu()
        self.screen_center()
        QTimer.singleShot(100, self.showMaximized)

    def screen_center(self) -> None:
        """Centers the window on the screen."""
        geometry = self.frameGeometry()
        center = QGuiApplication.primaryScreen().availableGeometry().center()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def set_canvas(self):
        self.canvas = qtViewer3d(self)
        self.canvas.InitDriver()
        self.display = self.canvas._display
        self.setCentralWidget(self.canvas)

    def set_ribbonmenu(self):
        ribbonbar = RibbonBar()
        self.setMenuBar(ribbonbar)

        # Categories
        category1 = ribbonbar.addCategory("Test")
        panel1 = category1.addPanel("Box")
        
        disp = panel1.addLargeButton("Display Box", QIcon("python.png"))
        disp.clicked.connect(self.displayBOX)

        eras = panel1.addLargeButton("Erase Box", QIcon("python.png"))
        eras.clicked.connect(self.eraseBOX)

    def displayBOX(self):
        a_box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
        self.ais_box = self.display.DisplayShape(a_box)[0]
        self.display.FitAll()

    def eraseBOX(self):
        self.display.Context.Erase(self.ais_box, True)

