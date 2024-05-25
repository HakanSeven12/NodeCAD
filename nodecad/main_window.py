import ryven
import pathlib

from qtpy.QtCore import Qt, QTimer
from qtpy.QtGui import QGuiApplication, QIcon
from qtpy.QtWidgets import QMainWindow, QDockWidget, QTreeView

from pyqtribbon import RibbonBar

# Load the backend for the OCC display
from OCC.Display.backend import load_backend
load_backend("pyside2")

from OCC.Display.qtDisplay import qtViewer3d
from OCC.Core.AIS import AIS_ViewCube
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("NodeCAD")
        self.app = app

        # Initialize the main components of the window
        self.canvas()
        self.objects_dock()
        self.ryven_dock(app)
        self.center_screen()

        # Maximize the window after a short delay
        QTimer.singleShot(100, self.showMaximized)

    def ribbonmenu(self):
        """Creates a ribbon menu with buttons."""
        ribbonbar = RibbonBar()
        self.setMenuBar(ribbonbar)

        # Add a category and panel to the ribbon menu
        category1 = ribbonbar.addCategory("Test")
        panel1 = category1.addPanel("Box")

        # Add buttons to the panel and connect them to actions
        disp = panel1.addLargeButton("Display Box", QIcon("python.png"))
        disp.clicked.connect(self.displayBOX)

        eras = panel1.addLargeButton("Erase Box", QIcon("python.png"))
        eras.clicked.connect(self.eraseBOX)

    def canvas(self):
        """Sets up the 3D viewer canvas."""
        self.canvas = qtViewer3d(self)
        self.canvas.InitDriver()
        self.app.display = self.canvas._display
        
        # Create and display the ViewCube in the 3D viewer
        view_cube = AIS_ViewCube()
        view_cube.SetDrawAxes(False)  # Customize the view cube appearance
        content = self.canvas._display.GetContext()
        content.Display(view_cube, True)
        
        self.setCentralWidget(self.canvas)

    def ryven_dock(self, app):
        """Sets up the Ryven dock widget."""
        ryven_main = ryven.run_ryven(
            qt_app=app, 
            gui_parent=self.canvas, 
            nodes=[pathlib.Path('PythonOCC'), pathlib.Path('std')],
            show_dialog=False
        )

        self.ryven_widget = QDockWidget(self)
        self.ryven_widget.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.ryven_widget.setWidget(ryven_main)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.ryven_widget)

    def objects_dock(self):
        """Sets up the dock widget for displaying objects."""
        self.dock_widget = QDockWidget(self)
        self.dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.tree_view = QTreeView(self)
        self.dock_widget.setWidget(self.tree_view)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget)

    def center_screen(self) -> None:
        """Centers the window on the screen."""
        geometry = self.frameGeometry()
        center = QGuiApplication.primaryScreen().availableGeometry().center()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def displayBOX(self):
        """Displays a 3D box in the viewer."""
        a_box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
        self.ais_box = self.display.DisplayShape(a_box)[0]
        self.display.FitAll()

    def eraseBOX(self):
        """Erases the displayed 3D box from the viewer."""
        self.display.Context.Erase(self.ais_box, True)
