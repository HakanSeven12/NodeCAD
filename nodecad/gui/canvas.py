import os

# Load the backend for the OCC display
from OCC.Display.backend import load_backend
qt_api = os.getenv('QT_API')
load_backend(qt_api)

from OCC.Display.qtDisplay import qtViewer3d
from OCC.Core.AIS import AIS_ViewCube



class Viewer3D(qtViewer3d):
    def __init__(self, *kargs):

        super().__init__(*kargs)

        self.InitDriver()
        self.set_scene(self._display)

    def set_scene(self,display):
        """Sets up the 3D viewer canvas."""
        display.display_triedron()

        # Create and display the ViewCube in the 3D viewer
        view_cube = AIS_ViewCube()
        view_cube.SetDrawAxes(False)  # Customize the view cube appearance
        content = display.GetContext()
        content.Display(view_cube, True)

    def EraseAll(self):
        # Get all displayed objects
        ais_context = self._display.GetContext()
        displayed_objects = ais_context.DisplayedObjects()

        # Loop through and erase all objects except the view cube
        for obj in displayed_objects:
            if not isinstance(obj, AIS_ViewCube):
                ais_context.Erase(obj, False)
        self._display.Context.UpdateCurrentViewer()
