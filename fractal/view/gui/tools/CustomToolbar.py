from matplotlib.backend_managers import ToolManager
from matplotlib.backend_tools import ToolCursorPosition
from matplotlib.figure import Figure

from view.gui.tools.CustomSave import CustomSave


class CustomToolbar(ToolManager):
    def __init__(self, fig: Figure):
        super().__init__(fig)

        self.add_tool("Cursor Position", ToolCursorPosition)
        self.add_tool("Save Figure", CustomSave)
