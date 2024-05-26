import ryven
import pathlib

from qtpy.QtCore import Qt, QTimer
from qtpy.QtGui import QGuiApplication
from qtpy.QtWidgets import QMainWindow, QDockWidget, QTreeView


from gui.ribbon_menu import RibbonMenu
from gui.canvas import Viewer3D


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("NodeCAD")

        # Initialize the main components of the window
        self.viewer = Viewer3D(self)
        app.display = self.viewer._display
        self.setCentralWidget(self.viewer)
        self.setMenuBar(RibbonMenu(self))
        self.ryven_dock(app)
        self.center_screen()

        # Maximize the window after a short delay
        QTimer.singleShot(100, self.showMaximized)

    def ryven_dock(self, app):
        """Sets up the Ryven dock widget."""
        ryven_main = ryven.run_ryven(
            qt_app=app, 
            gui_parent=self, 
            nodes=[pathlib.Path('PythonOCC'), pathlib.Path('std')],
            show_dialog=True
        )

        self.ryven_widget = QDockWidget(self)
        #self.ryven_widget.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.ryven_widget.setWidget(ryven_main)
        screen_heigth = QGuiApplication.primaryScreen().availableGeometry().width()
        self.ryven_widget.setMaximumWidth(screen_heigth*(2/5))
        self.addDockWidget(Qt.LeftDockWidgetArea, self.ryven_widget)

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
