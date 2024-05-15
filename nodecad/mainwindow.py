from PySide6.QtWidgets import (
    QMainWindow
)

from PySide6.QtGui import (
    QIcon
)

from pyqtribbon import RibbonBar

from OCC.Display.backend import load_backend

load_backend("pyside6")
import OCC.Display.qtDisplay as qtDisplay 
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

class MainWindow(QMainWindow):

    def __init__(self, fileName: str = "shot.jpg", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_canvas()
        self.set_ribbonmenu()
        
    def set_canvas(self):
        self.canvas = qtDisplay.qtViewer3d(self)
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

