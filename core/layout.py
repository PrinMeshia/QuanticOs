import time
from PySide2 import QtWidgets
from .window import Window
from .ressources import Ressources
from .dynamicLoad import getInstance


class Layout(Window):
    def __init__(self, data, default=False):
        super().__init__(data["global"]["fullscreen"],
                         default, len(data["packages"]))
        self.data = data
        w, h= 3,3
        self.matrix = [[0 for x in range(w)] for y in range(h)] 
        self.createWidget(data["packages"])
        self.createEmptySlot()        

    def createWidget(self, packages=[]):
        for package in packages:
            config = {**self.data["global"], **package}
            pos = package["position"]
            span = 1
            if "colspan" in package:
                span = package["colspan"]
                for index in range(package["colspan"]):
                    self.matrix[pos[0]][pos[1]+index] = "span"
            self.matrix[pos[0]][pos[1]] = [getInstance(package["name"], self.window, config),span]
        self.layout.update()
    
    def createEmptySlot(self):
        i=1
        print(self.matrix)
        for row,line in enumerate(self.matrix):
            self.layout.setRowStretch(row,1)
            for col, instance in enumerate(line):
                if row == 0:
                    self.layout.setColumnStretch(col,1)
                if instance == 0:
                    widget = QtWidgets.QWidget(self.window)
                    self.layout.addWidget(widget,row,col) 
                elif instance != "span":
                    print(instance)
                    self.layout.addWidget(instance[0],row,col,1,int(instance[1]))
                    self.progressBar.setValue(i) 
                    self.processEvents()
                    i += 1
                    time.sleep(1)   
        time.sleep(1)            
if __name__ == "__main__":
    window = Layout(False, True)
    time.sleep(6)
    window.show()
