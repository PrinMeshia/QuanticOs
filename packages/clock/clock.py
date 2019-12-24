from time import strftime

class Clock:
    def __init__(self,tk,root,config ):
        self.lbl = tk.Label(root, font = ('calibri', 40, 'bold'), 
            background = 'purple', 
            foreground = 'white') 
        self.lbl.pack(anchor = 'center') 
        self.tk = tk
        self.config = config
        
    def start(self): 
        time_format = "%H:%M:%S" if self.config["time_format"] == 24 else "%I:%M:%S %p"
        string = strftime(time_format) 
        self.lbl.config(text = string) 
        self.lbl.after(1000, self.start) 