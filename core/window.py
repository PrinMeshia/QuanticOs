
if __name__ == "__main__":
    from splash import Splash
else:
    from .splash import Splash
import tkinter as tk
import time
import os.path     
"""Generate window for mirrorOs
"""
class Window(tk.Tk):
    def __init__(self, name,fullscreen = True):
        self.name = name
        self.fullscreen = fullscreen
        self.default_w = 800
        self.default_h = 600
        tk.Tk.__init__(self)
        self.pos_x = int((self.winfo_screenwidth() / 2) - (self.default_w / 2))  
        self.pos_y = int((self.winfo_screenheight() / 2) - (self.default_h / 2))
        self.withdraw()
        self.splash = Splash(self)
        self.geometry("{}x{}+{}+{}".format(self.default_w, self.default_h, self.pos_x, self.pos_y))
        self.attributes("-fullscreen", self.fullscreen)
        self.title(name)
        self.configure(background="black", cursor="none")
        if(self.fullscreen == True):
            self.bind("<Escape>",self.toggle_screen)
        
    def toggle_screen(self,event):
        self.fullscreen = not self.fullscreen
        self.attributes("-fullscreen", self.fullscreen)
        
    def show(self):
        self.deiconify()
        self.splash.destroy()
        self.mainloop()
    
if __name__ == "__main__":
    window = Window("MirrorOS",False) 
    time.sleep(6)
    window.show()