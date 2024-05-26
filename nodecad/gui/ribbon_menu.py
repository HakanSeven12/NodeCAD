from qtpy.QtGui import QIcon
from pyqtribbon import RibbonBar

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox


class RibbonMenu(RibbonBar):

    def __init__(self, parent):
        """Creates a ribbon menu with buttons."""
        super().__init__(parent) 

        # Add a category and panel to the ribbon menu
        category1 = self.addCategory("Test")
        panel1 = category1.addPanel("Box")

        # Add buttons to the panel and connect them to actions
        disp = panel1.addLargeButton("Display Box", QIcon("python.png"))
        disp.clicked.connect(self.displayBOX)

        eras = panel1.addLargeButton("Erase Box", QIcon("python.png"))
        eras.clicked.connect(self.eraseBOX)

    def displayBOX(self):
        """Displays a 3D box in the viewer."""
        a_box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
        self.ais_box = self.display.DisplayShape(a_box)[0]
        self.display.FitAll()

    def eraseBOX(self):
        """Erases the displayed 3D box from the viewer."""
        self.display.Context.Erase(self.ais_box, True)
