from .window import Window
from .dynamicLoad import get_instance
import tkinter as tk

class Interface(Window):
    def __init__(self, name,data, default = False):
        super().__init__(name,data["global"]["fullscreen"],default)
        self.data = data
        self.create_interface(data["packages"])
        

    def create_interface(self, packages = []):
        package_list = {}  
        for package in packages:
            config = {**self.data["global"] , **package} 
            package_list[package["name"]] = get_instance(package["name"], tk,self, config).start()
            
    