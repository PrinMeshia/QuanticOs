import os
import os.path
from PySide2.QtCore import Qt

class RessurceTypeError(Exception):
    pass


class Ressources:
    applicationName = "QuanticOS"
    assetsPath = os.path.join(os.getcwd(),"assets")
    imagesPath = "images"
    iconsPath = "icons"
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
        "icon" : "favicon.png",
        "loader" : "loader.gif"
    }
    icon_lookup = {
        'clear-day': "Sun.png",  # clear sky day
        'wind': "Wind.png",   #wind
        'cloudy': "Cloud.png",  # cloudy day
        'partly-day': "assets/PartlySunny.png",  # partly cloudy day
        'rain': "Rain.png",  # rain day
        'snow': "Snow.png",  # snow day
        'snow-thin': "Snow.png",  # sleet day
        'fog': "Haze.png",  # fog day
        'clear-night': "Moon.png",  # clear sky night
        'partly-cloudy-night': "PartlyMoon.png",  # scattered clouds night
        'thunderstorm': "Storm.png",  # thunderstorm
        'tornado': "Tornado.png",    # tornado
        'hail': "Hail.png"  # hail
    }
    
    @classmethod
    def getImagePath(self,image):
        return os.path.join(self.assetsPath,self.imagesPath,image)
    
    @classmethod
    def getAlignment(self,position):
        return self.positions[position]
    
    @classmethod
    def getImage(self,image):
        return self.getImagePath(self.images[image])
    
    @classmethod
    def getIconPath(self,folder,image):
        return os.path.join(self.assetsPath,folder,self.iconsPath,image)
    
    @classmethod
    def getIcons(self,folder,image):
        return self.getIconPath(folder,self.images[image])