from PySide2 import QtWidgets,QtGui
from PySide2.QtCore import Qt, QSize
from core.ressources import Ressources

class Speech(QtWidgets.QWidget):  
    def __init__(self,parent,config):
        super(Speech,self).__init__()
        self.layout = QtWidgets.QGridLayout(self)
        rect = parent.geometry()
        movie = QtGui.QMovie(Ressources.getImage("loader"))
        label = QtWidgets.QLabel()
        label.setMovie(movie)
        movie.start()
        label.setAlignment(Ressources.getAlignment("center"))
        movie.setScaledSize(QSize(200,200))
        self.layout.addWidget(label,0,0)
        
        
        
    