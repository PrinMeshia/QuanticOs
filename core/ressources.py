import os
import os.path
from PySide2.QtCore import Qt

applicationName = "QuanticOS"
assetsPath = os.path.join(os.getcwd(), "assets")
imagesPath = "images"
iconsPath = "icons"
backgroundColor = Qt.black
fontColor = Qt.white
alignments = {
    "top_left": Qt.AlignTop | Qt.AlignLeft,
    "top": Qt.AlignTop | Qt.AlignCenter,
    "top_right": Qt.AlignTop | Qt.AlignRight,
    "left": Qt.AlignCenter | Qt.AlignLeft,
    "center": Qt.AlignCenter | Qt.AlignCenter,
    "right": Qt.AlignCenter | Qt.AlignRight,
    "bottom_left": Qt.AlignBottom | Qt.AlignLeft,
    "bottom": Qt.AlignBottom | Qt.AlignCenter,
    "bottom_right": Qt.AlignBottom | Qt.AlignRight
}
positions = {
    "top_left": (0, 0),
    "top": (0, 1),
    "top-right": (0, 2),
    "left": (1, 0),
    "center": (1, 1),
    "right": (1, 2),
    "bottom-left": (2, 0),
    "bottom":  (2, 1),
    "bottom-right": (2, 2)
}
images = {
    "logo": "logo.png",
    "icon": "favicon.png",
    "loader": "loader.gif"
}
icon_lookup = {
    'clear-day': "Sun.png",  # clear sky day
    'wind': "Wind.png",  # wind
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


def getImagePath(image):
    return os.path.join(assetsPath, imagesPath, image)


def getAlignment(alignment):
    return alignments[alignment]


def getPosition(alignment):
    return positions[alignment]


def getImage(image):
    return getImagePath(images[image])


def getIconPath(folder, image):
    return os.path.join(assetsPath, folder, iconsPath, image)


def getIcons(folder, image):
    return getIconPath(folder, images[image])
