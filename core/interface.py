if __name__ == "__main__":
    from window import Window
else:
    from .window import Window

class Interface(Window):
    def __init__(self, name,fullscreen = True):
        super().__init__(name,fullscreen)

    def create_interface(self, configs = []):
        for config in configs:
            pass
    

if __name__ == "__main__":
    Interface = Interface("MirrorOS") 
    Interface.show()