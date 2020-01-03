from PySide2 import QtWidgets,QtCore
from PySide2.QtCore import QLocale
from core.ressources import Ressources
class Clock(QtWidgets.QWidget):  
    def __init__(self,parent,config):
        super(Clock,self).__init__(parent)
        self.locale = config["locale"]
        
        QLocale.setDefault(self.locale)
        self.curTime = QtWidgets.QLabel()
        self.curTime.setObjectName("curTime")
        curDate = QtWidgets.QLabel(QLocale().toString(QtCore.QDate.currentDate()).capitalize())
        curDate.setObjectName("curdate")
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(curDate)
        self.layout.addWidget(self.curTime)
        self.layout.setAlignment(Ressources.getAlignment(config["alignment"]))
        self.setStyleSheet("""
                           #curdate,#curTime {
                               color:white; 
                               font: bold 35px;
                               padding: 6px;
                            } 
                            """)
        self.curTime.setAlignment(Ressources.getAlignment("center"))
        timer = QtCore.QTimer(self)
        self.connect(timer,QtCore.SIGNAL('timeout()'),self.showTime)
        timer.start(1000)
        self.showTime()      
        
    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = QLocale().toString(time,"hh:mm:ss") 
        self.curTime.setText(text)