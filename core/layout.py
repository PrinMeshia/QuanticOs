import time
from .window import Window
from .ressources import Ressources
from .dynamicLoad import getInstance


class Layout(Window):
    def __init__(self, data, default=False):
        super().__init__(data["global"]["fullscreen"],
                         default, len(data["packages"]))
        self.data = data
        self.createWidget(data["packages"])

    def createWidget(self, packages=[]):
        package_list = {}
        i = 1
        for package in packages:
            config = {**self.data["global"], **package}
            package_list[package["name"]] = getInstance(
                package["name"], config)
            # self.window.addDockWidget(package_list[package["name"]],)
            self.layout.addWidget(package_list[package["name"]])
            self.progressBar.setValue(i)
            self.processEvents()
            time.sleep(1)
            i += 1
        
        self.window.setLayout(self.layout)


if __name__ == "__main__":
    window = Layout(False, True)
    time.sleep(6)
    window.show()
