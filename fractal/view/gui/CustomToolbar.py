from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar


class CustomToolbar(NavigationToolbar):
    def __init__(self, canvas, parent):
        super().__init__(canvas, parent)


    def custom_action(self):
        pass
