import os
from PyQt6.QtCore import pyqtSlot, QObject, Qt

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
  
  # Don't remove this method, it's used for VSK Window
  @pyqtSlot()
  def startMove(self):
    self.window.windowHandle().startSystemMove()

  # Don't remove this method, it's used for VSK Window
  @pyqtSlot(str)
  def startResize(self, direction: str):
    
    if direction == "top":
      direction = Qt.Edge.TopEdge
    elif direction == "right":
      direction = Qt.Edge.RightEdge
    elif direction == "bottom":
      direction = Qt.Edge.BottomEdge
    elif direction == "left":
      direction = Qt.Edge.LeftEdge
    elif direction == "topright":
      direction = Qt.Edge.TopEdge | Qt.Edge.RightEdge
    elif direction == "bottomright":
      direction = Qt.Edge.BottomEdge | Qt.Edge.RightEdge
    elif direction == "bottomleft":
      direction = Qt.Edge.BottomEdge | Qt.Edge.LeftEdge
    elif direction == "topleft":
      direction = Qt.Edge.TopEdge | Qt.Edge.LeftEdge
    else:
      direction = Qt.Edge.TopEdge | Qt.Edge.LeftEdge
    
    self.window.windowHandle().startSystemResize(direction)

  # Don't remove this method, it's used for VSK Window
  @pyqtSlot()
  def exit(self):
    self.app.exit()

  # Don't remove this method, it's used for VSK Window
  @pyqtSlot()
  def minimize(self):
    self.window.showMinimized()
  
  # Don't remove this method, it's used for VSK Window
  @pyqtSlot()
  def toggleMaximize(self):
    if self.window.isMaximized():
      self.window.showNormal()
    else:
      self.window.showMaximized()
  
  @pyqtSlot()
  def loadUIConfig(self):
    self.window.load_ui_config()