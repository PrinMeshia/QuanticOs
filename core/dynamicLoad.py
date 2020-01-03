import importlib
def loadModule(module_name):
    module = None
    try:
        import sys
        del sys.modules[module_name]
    except BaseException as err:
        pass
    try:
        import importlib
        module = importlib.import_module("modules."+module_name+".module")
    except BaseException as err:
        serr = str(err)
        print("Error to load the module '" + module_name + "': " + serr)
   
    return module
      
def getInstance(module_name,parent, config):
    module = loadModule(module_name)
    try:
        instance = eval("module." + module_name.capitalize() + "(parent,config)")
        return instance
    except AttributeError as err:
        serr = str(err)
        print("Error to load the module '" + module_name + "': " + serr)
    
    
    