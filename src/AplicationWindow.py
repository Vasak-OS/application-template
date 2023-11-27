from Vasak.VSKWindow import VSKWindow
from src.AplicationBinding import AplicationBinding

class AplicationWindow(VSKWindow):
    def __init__(self):
        super().__init__()
        self.shareObject = AplicationBinding(self)
        self.channel.registerObject("vsk", self.shareObject)
        self.load_html("ui/dist/index.html") # Cargar un HTML en el WebView
