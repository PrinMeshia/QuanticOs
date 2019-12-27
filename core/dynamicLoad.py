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
        module = importlib.import_module("packages."+module_name+"."+module_name)
        dir(module)
    except BaseException as err:
        serr = str(err)
        print("Error to load the module '" + module_name + "': " + serr)
    return module
      
def getInstance(module_name, config):
    module = loadModule(module_name)
    instance = eval("module." + module_name.capitalize() + "(config)")
    print(instance)
    return instance