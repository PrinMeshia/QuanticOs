import os
import os.path
from PySide2.QtCore import Qt

class RessurceTypeError(Exception):
    pass


class Ressources:
    applicationName = "QuanticOS"
    assetsPath = os.path.join(os.getcwd(),"assets")
    imagesPath = "images"
    backgroundColor = Qt.black
    fontColor = Qt.white
    positions = {
        "top-left": Qt.AlignTop | Qt.AlignLeft,
        "top" : Qt.AlignTop |  Qt.AlignCenter,
        "top-right" : Qt.AlignTop | Qt.AlignRight,
        "left": Qt.AlignCenter | Qt.AlignLeft,
        "center" : Qt.AlignCenter | Qt.AlignCenter,
        "right" : Qt.AlignCenter | Qt.AlignRight,
        "bottom-left": Qt.AlignBottom | Qt.AlignLeft,
        "bottom" : Qt.AlignBottom |  Qt.AlignCenter,
        "bottom-right" : Qt.AlignBottom | Qt.AlignRight
    }
    images = {
        "logo" : "logo.png",
        "icon" : "favicon.png"
    }
    
    @classmethod
    def getImagePath(self,image):
        return os.path.join(self.assetsPath,self.imagesPath,image)
    
    @classmethod
    def getAlignment(self,position):
        return int(self.positions[position])
    
    @classmethod
    def getImage(self,image):
        return self.getImagePath(self.images[image])