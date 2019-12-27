import time
if __name__ == "__main__":
    from window import Window
    from dynamicLoad import getInstance
else:
    from .window import Window
    from .dynamicLoad import getInstance

class Interface(Window):
    def __init__(self, data, default = False):
        super().__init__(data["global"]["fullscreen"],default,len(data["packages"]))
        self.data = data
        self.create_interface(data["packages"])
        
    def create_interface(self, packages = []):
        package_list = {}  
        i = 1
        for package in packages:
            
            # config = {**self.data["global"] , **package} 
            # package_list[package["name"]] = getInstance(package["name"], tk,self, config).start()
            self.progressBar.setValue(i)
            self.processEvents()
            time.sleep(1)
            i += 1
            
if __name__ == "__main__":
    window = Interface(False,True) 
    time.sleep(6)
    window.show()