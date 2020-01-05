from PySide2 import QtWidgets,QtCore
from PySide2.QtCore import QLocale
import core.ressources as Ressources
from datetime import datetime
from dateutil import parser
import random
import feedparser


class Newsfeed(QtWidgets.QWidget):  
    def __init__(self,parent,config):
        super(Newsfeed,self).__init__(parent)
        self.locale = config["locale"]
        QLocale.setDefault(self.locale)
        self.config = config
        self.all_head_lines = []
        self.timerFeed = QtCore.QTimer(self)
        self.timerNews = QtCore.QTimer(self)
        self.date_pub = QtWidgets.QLabel()
        self.title_pub = QtWidgets.QLabel()
        self.date_pub.setObjectName("datePub")
        self.title_pub.setObjectName("titlePub")
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.date_pub)
        self.layout.addWidget(self.title_pub)
        self.layout.setAlignment(Ressources.getAlignment("bottom_left"))
        self.setStyleSheet("""
                           #datePub,#titlePub {
                               color:white; 
                               padding: 6px;
                            } 
                            #titlePub {
                               font: bold 35px;
                            } 
                            #datePub {
                               font: 25px;
                            } 
                            """)



        self.connect(self.timerFeed,QtCore.SIGNAL('timeout()'),self.getNewsFedd)
        self.timerFeed.start(6*60*60*1000)
        self.getNewsFedd()      
        

    def getNewsFedd(self): 
        self.all_head_lines.clear()
        self.timerNews.stop()
        for url in self.config["rssUrl"]:
            feed_list = self.getHeadLines(url)
            self.all_head_lines = [*self.all_head_lines, *feed_list]
        self.connect(self.timerNews,QtCore.SIGNAL('timeout()'),self.showNews)
        self.timerNews.start(30*1000)
        self.showNews()

    def showNews(self):
        random_items = random.choices(population=self.all_head_lines, k=1)[0]
        date = parser.parse(random_items["date"])
        str_date = QLocale().toString(date) 
        self.date_pub.setText(str_date.capitalize())
        self.title_pub.setText(random_items["title"])
        print(random_items)

    def parseRSS(self,url_flux):
        return feedparser.parse(url_flux)
    
    def getHeadLines(self,url_flux)    :
        headlines = []
        feed = self.parseRSS(url_flux)
        for newsitem in feed["items"]:
            news = {}
            news["date"] = newsitem["published"]
            news["title"] = newsitem["title"]
            headlines.append(news)
        return headlines