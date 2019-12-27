from PySide2 import QtWidgets,QtCore

class Clock(QtWidgets.QLCDNumber):
    def __init__(self,config):
        super(Clock,self).__init__()
        self.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        timer = QtCore.QTimer(self)
        self.connect(timer,QtCore.SIGNAL('timeout()'),self.showTime)
        timer.start(1000)
        self.showTime()
        style_str = "QWidget {font-size: 20px}"
        self.setStyleSheet(style_str)
        
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)    
       
        
    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:5]+' '+text[6:]
        self.display(text)
    #     self.lbl = tk.Label(root, font = ('calibri', 40, 'bold'), 
    #         background = 'purple', 
    #         foreground = 'white') 
    #     self.lbl.pack(anchor = 'center') 
    #     self.time_format = "%H:%M:%S" if config["time_format"] == 24 else "%I:%M:%S %p"
    # def start(self): 
    #     string = strftime(time_format) 
    #     self.lbl.config(text = string) 
    #     self.lbl.after(1000, self.start) 