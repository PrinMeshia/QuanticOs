from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
import time

if __name__ == "__main__":
    from ressources import Ressources
else:
    from .ressources import Ressources

class Window(QtWidgets.QApplication):
    fullscreen = False
    numPackage = 1
    def __init__(self, fullscreen,default,numPackage):
        # QtWidgets.QApplication.__init__(self)
        super().__init__([])
        Window.fullscreen = fullscreen
        Window.numPackage = numPackage
        self.splashScreen(default)
        self.createWindow()
        
    @classmethod
    def createWindow(self):
        self.setOverrideCursor(Qt.BlankCursor)
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle(Ressources.applicationName)
        self.window.setAutoFillBackground(True)
        p = self.window.palette()
        p.setColor(self.window.backgroundRole(),Ressources.backgroundColor)
        self.window.setPalette(p)
        self.window.setWindowIcon(QtGui.QIcon(Ressources.getImage("icon")))
        self.window.resize(800,600)
        if Window.fullscreen == True:
            self.window.showFullScreen()
        QtWidgets.QShortcut(QtGui.QKeySequence.FullScreen,self.window,self.toggleScreen)
        self.layout = QtWidgets.QHBoxLayout()
        
    @classmethod
    def toggleScreen(self):
        Window.fullscreen = not Window.fullscreen
        if Window.fullscreen == True : 
            self.window.showFullScreen()
        else :
            self.window.showNormal()

    @classmethod
    def splashScreen(self,default):
        splashPix = QtGui.QPixmap(Ressources.getImage("logo"))
        self.splash = QtWidgets.QSplashScreen(splashPix, Qt.WindowStaysOnTopHint)
      
        self.splash.setAutoFillBackground(True)
        p = self.splash.palette()
        p.setColor(self.splash.backgroundRole(),Ressources.backgroundColor)
        self.splash.setPalette(p)            
        self.splash.setEnabled ( False ) 
        self.setProgressBar(splashPix)
        if default == True:
            self.splash.showMessage("Default configuration", Ressources.getAlignment("bottom"), Ressources.fontColor)
        self.splash.show()
        
    @classmethod    
    def setProgressBar(self,splashPix):
        self.progressBar = QtWidgets.QProgressBar(self.splash) 
        self.progressBar.setValue(0)
        self.progressBar.setStyleSheet(
            "QProgressBar::chunk { background-color: #05B8CC; }"+
            "QProgressBar { color: #000000; text-align:center;font-weight:bold}" 
        )
        self.progressBar.setMaximum(Window.numPackage) 
        self.progressBar.total_bytes = Window.numPackage
        self.progressBar.setGeometry(0, splashPix.height()-50, splashPix.width(),20) 
         
    @classmethod
    def show(self):
        self.splash.finish(self.window)
        self.window.show()
        self.exec_()

if __name__ == "__main__":
    window = Window(True,True,1) 
    time.sleep(6)
    window.show()
    
