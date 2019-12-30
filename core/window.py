from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt, QSize
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
        self.window = QtWidgets.QMainWindow()
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
        QtWidgets.QShortcut(QtGui.QKeySequence.Cancel,self.window,self.closeAllWindows)
        self.mainWidget()
        self.layout = QtWidgets.QGridLayout()
       
    @classmethod
    def mainWidget(self):
        rect = self.window.geometry()
        movie = QtGui.QMovie(Ressources.getImage("loader"))
        label = QtWidgets.QLabel()
        label.setMovie(movie)
        movie.start()
        label.setAlignment(Ressources.getAlignment("center"))
        movie.setScaledSize(QSize(200,200))
        self.window.setCentralWidget(label)
         
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
            self.splash.showMessage("Default configuration", int(Ressources.getAlignment("bottom")), Ressources.fontColor)
        self.splash.show()
        
    @classmethod    
    def setProgressBar(self,splashPix):
        self.progressBar = QtWidgets.QProgressBar(self.splash) 
        self.progressBar.setObjectName("splashLoader")
        self.progressBar.setValue(0)
        self.progressBar.setStyleSheet(
            "#splashLoader::chunk { background-color: #05B8CC; }"+
            "#splashLoader { color: #000000; text-align:center;font-weight:bold}" 
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
    time.sleep(1)
    window.show()
    
