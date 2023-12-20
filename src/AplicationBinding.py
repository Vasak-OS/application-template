import os
from PyQt6.QtCore import pyqtSlot, QObject

class ApplicationBinding(QObject):
  def __init__(self, window, app):
    super().__init__()
    self.window = window
    self.app = app

  @pyqtSlot(result=str)
  def getHome(self):
      home_path = os.path.expanduser("~")

      if not os.path.isabs(home_path):
        home_path = os.path.join("/", home_path)

      return home_path
  
  @pyqtSlot()
  def startMove(self):
    self.window.windowHandle().startSystemMove()

  @pyqtSlot()
  def exit(self):
    self.app.exit()

  @pyqtSlot()
  def minimize(self):
    self.window.showMinimized()
  
  @pyqtSlot()
  def toggleMaximize(self):
    if self.window.isMaximized():
      self.window.showNormal()
    else:
      self.window.showMaximized()