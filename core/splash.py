import tkinter as tk
from tkinter import PhotoImage,Canvas
import time
import os.path

class Splash(tk.Toplevel):
    logo = 'logo.png'
    default_ratio = 4
    def __init__(self, parent, default):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.title(parent.name)
        self.resizable(False, False)            
        geometry = self.get_geometry()
        self.geometry("{}x{}+{}+{}".format(geometry[0], geometry[1], parent.pos_x, parent.pos_y))
        self.attributes("-fullscreen", parent.fullscreen)
        image = self.set_image(geometry)
        
        self.set_canva(image,geometry,default)
        self.configure(background="black", cursor="none")
        self.wm_overrideredirect(True)
        self.update()
         
    def get_geometry(self):
        geo_width = self.parent.winfo_screenwidth() if self.parent.fullscreen else self.parent.default_w  
        geo_height = self.parent.winfo_screenheight() if self.parent.fullscreen else self.parent.default_h
        geometry = (geo_width,geo_height)  
        return geometry
    
    def set_image(self,geometry):
        image_path = os.path.join(os.getcwd(),'assets','image',self.logo)
        image = PhotoImage(file=image_path)
        ratio = image.width()/geometry[1]
        if(ratio > self.default_ratio):
            self.default_ratio = ratio
        image = image.subsample(self.default_ratio)
        return image
    
    def set_canva(self,image,geometry,default):
        canvas = Canvas(self,width=geometry[0], height=geometry[1],bg="black",highlightthickness=0)
        canvas.create_image(geometry[0]/2, geometry[1]/2, image=image, anchor="center")
        if default == True:
            canvas.create_text(geometry[0]/2, geometry[1]-20,fill="white",font="calibri 20 bold",
                        text="Default configuration",anchor="s")
        canvas.pack()
        
    def quit(self):
        self.fade_away()
        
    def fade_away(self):
        alpha = self.attributes("-alpha")
        if alpha > 0:
            alpha -= .1
            self.attributes("-alpha", alpha)
            self.after(100, self.fade_away)
        else:
            self.destroy()