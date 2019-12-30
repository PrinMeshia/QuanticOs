from PySide2 import QtWidgets,QtCore
import json
import requests
import sys

class Weather(QtWidgets.QWidget):
    def __init__(self,parent,config):
        super(Weather,self).__init__(parent)
        self.baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
        self.setOWMUrl(config)
        if self.fullUrl != False:
            self.loadWeather()
        # print( self.fullUrl) 
        # response = request.GET()
    
    def setOWMUrl(self,config):
        if (not config["city_name"] or config["city_name"] == "") or (not config["city_code"] or config["city_code"] == ""):
            print('no appid or no city selected')
            self.fullUrl = False
        else:
            self.fullUrl = self.baseUrl+"appid="+config["api_key"]
            if config["city_name"] or config["city_name"] != "":
                self.fullUrl += "&q="+config["city_name"]
            if config["city_code"] or config["city_code"] != "":
                self.fullUrl += "&id="+config["city_code"]   
                
    def loadWeather(self):
        try:
            response = requests.get(self.fullUrl)
        except
            print()
       
        
        