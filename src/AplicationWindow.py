import os
from Vasak.VSKWindow import VSKWindow
from Vasak.system.VSKConfigManager import VSKConfigManager
from src.AplicationBinding import AplicationBinding
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, QFileSystemWatcher

class AplicationWindow(VSKWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.shareObject = AplicationBinding(self, app)
        self.configManager = VSKConfigManager()
        self.channel.registerObject("vsk", self.shareObject)
        self.load_html("ui/dist/index.html") # Cargar un HTML en el WebView
        QFileSystemWatcher([os.path.expanduser('~') ++ '/.config/vasak/vasak.conf']).fileChanged.connect(self.reload_ui_config)

    def set_position(self):
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowType.FramelessWindowHint 
        )

    def send_Javascript(self, message):
        self.webview.page().runJavaScript(message)

    def load_ui_config(self):
        self.configManager.reload()
        darkMode = self.configManager.get('STYLE', 'darkmode')
        radius = self.configManager.get('STYLE', 'radius')
        color = self.configManager.get('STYLE', 'color')

        self.send_Javascript(f'document.body.style.setProperty("--system-rounded", "{radius}px")')
        self.send_Javascript(f'document.body.style.setProperty("--system-accent-color", "{color}")')
        if darkMode == 'true':
            self.send_Javascript('document.body.classList.add("dark")')
        else:
            self.send_Javascript('document.body.classList.remove("dark")')
    
