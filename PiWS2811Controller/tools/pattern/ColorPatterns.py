from importlib import util
import os


class PatternRegistry(type):
    patterns = []
    
    def __init__(cls, name, bases, attrs):
        if name != "ColorPattern":
            cls.patterns.append(cls)
            print("loaded plugins: " + str(cls.patterns))
            

class ColorPattern(object, metaclass=PatternRegistry):   
    def pattern(self, pixels, pixelCount, theme): raise NotImplementedError
    
    

def loadPatterns(path):
    for fname in os.listdir(path):
        if not fname.startswith("__") and not fname.startswith(".") and fname.endswith(".py"):
            load(os.path.join(path, fname))
    return PatternRegistry.patterns

def load(path):
    name = os.path.split(path)[-1]
    #print("loaded: " + name)
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
