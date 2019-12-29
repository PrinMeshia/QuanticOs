from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
import time

from .ressources import Ressources

class Window(QtWidgets.QApplication):
    fullscreen = False
    numPackage = 1

    def __init__(self, fullscreen, default, numPackage):
        # QtWidgets.QApplication.__init__(cls)
        super().__init__([])
        Window.fullscreen = fullscreen
        Window.numPackage = numPackage
        self.splashScreen(default)
        self.createWindow()

    @classmethod
    def createWindow(cls):
        cls.setOverrideCursor(Qt.BlankCursor)
        cls.window = QtWidgets.QMainWindow()
        cls.window.setWindowTitle(Ressources.applicationName)
        cls.window.setAutoFillBackground(True)
        p = cls.window.palette()
        p.setColor(cls.window.backgroundRole(), Ressources.backgroundColor)
        cls.window.setPalette(p)
        cls.window.setWindowIcon(QtGui.QIcon(Ressources.getImage("icon")))
        cls.window.resize(800, 600)
        if Window.fullscreen == True:
            cls.window.showFullScreen()
        QtWidgets.QShortcut(QtGui.QKeySequence.FullScreen,
                            cls.window, cls.toggleScreen)
        cls.layout = QtWidgets.QHBoxLayout()

    @classmethod
    def toggleScreen(cls):
        Window.fullscreen = not Window.fullscreen
        if Window.fullscreen == True:
            cls.window.showFullScreen()
        else:
            cls.window.showNormal()

    @classmethod
    def splashScreen(cls, default):
        splashPix = QtGui.QPixmap(Ressources.getImage("logo"))
        cls.splash = QtWidgets.QSplashScreen(
            splashPix, Qt.WindowStaysOnTopHint)

        cls.splash.setAutoFillBackground(True)
        p = cls.splash.palette()
        p.setColor(cls.splash.backgroundRole(), Ressources.backgroundColor)
        cls.splash.setPalette(p)
        cls.splash.setEnabled(False)
        cls.setProgressBar(splashPix)
        if default == True:
            cls.splash.showMessage("Default configuration", Ressources.getAlignment(
                "bottom"), Ressources.fontColor)
        cls.splash.show()

    @classmethod
    def setProgressBar(cls, splashPix):
        cls.progressBar = QtWidgets.QProgressBar(cls.splash)
        cls.progressBar.setValue(0)
        cls.progressBar.setStyleSheet(
            "QProgressBar::chunk { background-color: #05B8CC; }" +
            "QProgressBar { color: #000000; text-align:center;font-weight:bold}"
        )
        cls.progressBar.setMaximum(Window.numPackage)
        cls.progressBar.total_bytes = Window.numPackage
        cls.progressBar.setGeometry(
            0, splashPix.height()-50, splashPix.width(), 20)

    @classmethod
    def show(cls):
        cls.splash.finish(cls.window)
        cls.window.show()
        cls.exec_()


if __name__ == "__main__":
    window = Window(False, True, 1)
    time.sleep(6)
    window.show()
