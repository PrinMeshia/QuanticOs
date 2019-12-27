from core.interface import Interface
import sys
import os
import os.path
import time
import json
from pathlib import Path
def curtime():
    return time.strftime("%H:%M:%S %Y-%m-%d")

def launch_os(data, default = False):
    print(curtime() +' : Start OS')
    test = Interface(data,default)
    test.show()
    

config_file_path = os.path.join(os.getcwd(),"config","config.json")
config_default_file_path = os.path.join(os.getcwd(),"config","config-default.json")

if os.path.isfile(config_file_path):
    config_file = config_file_path
    default_conf = False
else:
    config_file = config_default_file_path
    default_conf = True

try:
    with open(config_file,encoding="UTF-8",mode="r") as json_file:
        data = json.load(json_file)
        launch_os(data,default_conf)
        # Do something with the file
except FileNotFoundError:
    print("File not accessible")







