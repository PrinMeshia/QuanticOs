from PySide2 import QtWidgets,QtCore
from PySide2.QtCore import QLocale
from core.ressources import Ressources
import feedparser

class Newsfeed(QtWidgets.QWidget):  
    def __init__(self,parent,config):
        super(Newsfeed,self).__init__(parent)
        all_head_lines = []
        print(config["rssUrl"])
        for url in config["rssUrl"]:
            all_head_lines.append(self.getHeadLines(url))
        
        for hl in all_head_lines:
            print(hl)
        
    def parseRSS(self,url_flux):
        return feedparser.parse(url_flux)
    
    def getHeadLines(self,url_flux)    :
        headlines = []
        feed = self.parseRSS(url_flux)
        print(feed)
        for newsitem in feed["items"]:
            
            headlines.append(newsitem['title'])
        return headlines