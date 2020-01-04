from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt, QSize
import time
import core.ressources as rs

class Window(QtWidgets.QApplication):
    fullscreen = False
    numPackage = 1
    def __init__(cls, fullscreen,default,numPackage):
        # QtWidgets.QApplication.__init__(cls)
        super().__init__([])
        Window.fullscreen = fullscreen
        Window.numPackage = numPackage
        cls.splashScreen(default)
        cls.createWindow()
        
    @classmethod
    def createWindow(cls):
        cls.setOverrideCursor(Qt.BlankCursor)
        cls.window = QtWidgets.QWidget()
        cls.window.setWindowTitle(rs.applicationName)
        cls.window.setAutoFillBackground(True)
        p = cls.window.palette()
        p.setColor(cls.window.backgroundRole(),rs.backgroundColor)
        cls.window.setPalette(p)
        cls.window.setWindowIcon(QtGui.QIcon(rs.getImage("icon")))
        cls.window.resize(800,600)
        if Window.fullscreen == True:
            cls.window.showFullScreen()
        QtWidgets.QShortcut(QtGui.QKeySequence.FullScreen,cls.window,cls.toggleScreen)
        QtWidgets.QShortcut(QtGui.QKeySequence.Cancel,cls.window,cls.closeAllWindows)
        # cls.mainWidget()
        cls.layout = QtWidgets.QGridLayout()
        cls.window.setLayout(cls.layout)
                
    @classmethod
    def mainWidget(cls):
        rect = cls.window.geometry()
        movie = QtGui.QMovie(rs.getImage("loader"))
        label = QtWidgets.QLabel()
        label.setMovie(movie)
        movie.start()
        label.setAlignment(rs.getAlignment("center"))
        movie.setScaledSize(QSize(200,200))
        cls.window.setCentralWidget(label)
         
    @classmethod
    def toggleScreen(cls):
        Window.fullscreen = not Window.fullscreen
        if Window.fullscreen == True : 
            cls.window.showFullScreen()
        else :
            cls.window.showNormal()

    @classmethod
    def splashScreen(cls,default):
        splashPix = QtGui.QPixmap(rs.getImage("logo"))
        cls.splash = QtWidgets.QSplashScreen(splashPix, Qt.WindowStaysOnTopHint)
        cls.splash.setAutoFillBackground(True)
        p = cls.splash.palette()
        p.setColor(cls.splash.backgroundRole(),rs.backgroundColor)
        cls.splash.setPalette(p)            
        cls.splash.setEnabled ( False ) 
        cls.setProgressBar(splashPix)
        if default == True:
            cls.splash.showMessage("Default configuration", int(rs.getAlignment("bottom")), rs.fontColor)
        cls.splash.show()
        
    @classmethod    
    def setProgressBar(cls,splashPix):
        cls.progressBar = QtWidgets.QProgressBar(cls.splash) 
        cls.progressBar.setObjectName("splashLoader")
        cls.progressBar.setValue(0)
        cls.progressBar.setStyleSheet("""
            #splashLoader::chunk { background-color: #05B8CC; }
            #splashLoader { color: #000000; text-align:center;font-weight:bold}
        """)
        cls.progressBar.setMaximum(Window.numPackage) 
        cls.progressBar.total_bytes = Window.numPackage
        cls.progressBar.setGeometry(0, splashPix.height()-50, splashPix.width(),20) 
         
    @classmethod
    def show(cls):
        cls.splash.finish(cls.window)
        cls.window.show()
        cls.exec_()

if __name__ == "__main__":
    window = Window(True,True,1) 
    time.sleep(1)
    window.show()
    
