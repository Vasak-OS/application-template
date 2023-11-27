import os
from PyQt6.QtCore import pyqtSlot, QObject

class ApplicationBinding(QObject):
  def __init__(self, window):
    super().__init__()
    self.window = window

  @pyqtSlot(result=str)
  def getHome(self):
      home_path = os.path.expanduser("~")

      if not os.path.isabs(home_path):
        home_path = os.path.join("/", home_path)

      return home_path