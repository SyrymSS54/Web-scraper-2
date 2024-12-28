from .AliParser import AliParser
from .SatuParser import SatuParser
from .OzonParser import OzonParser
from .WildParser import WildParser

class Divarication():
    def __init__(self,store,s_class):
        self.store = store
        self.s_class = s_class
        self.main_data = {}
        self.main_func()
    
    def main_func(self):
        for key,values in self.store.items():
            self.main_data[key] = []
            class__ = self.s_class[key]
            for value in values:
                if key == "AliExpress":
                    self.main_data[key].append(AliParser(class__,value).data)
                elif key == "Satu":
                    self.main_data[key].append(SatuParser(class__,value).data)
                elif key == "Ozon":
                    self.main_data[key].append(OzonParser(class__,value).data)
                elif key == "WildBerries":
                    self.main_data[key].append(WildParser(class__,value).data)
                    