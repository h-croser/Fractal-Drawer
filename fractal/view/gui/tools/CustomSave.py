from matplotlib.backend_tools import SaveFigureBase


class CustomSave(SaveFigureBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = "./icons/save.png"
