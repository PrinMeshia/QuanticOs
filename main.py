from core.interface import Interface
import sys
import os
import time
import json

def curtime():
    return time.strftime("%H:%M:%S %Y-%m-%d")

def launch_os():
    print(curtime() +' : Start MirrorOs')
    test = Interface("MirrorOs")
    time.sleep(6)
    test.show()
    
def launch_default():
    pass

config_file_path = os.path.join(os.getcwd(),"config","config.json")
config_default_file_path = os.path.join(os.getcwd(),"config","config.json.default")
try:
    with open(config_file_path,encoding="UTF-8",mode="r") as json_file:
        data = json.load(json_file)
        print(data)
        # Do something with the file
except FileNotFoundError:
    try:
        with open(config_default_file_path,encoding="UTF-8",mode="r") as json_file:
            data = json.load(json_file)
            print(data)
            # Do something with the file
    except FileNotFoundError:
        print("File not accessible")







