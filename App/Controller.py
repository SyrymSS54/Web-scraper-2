from .Divarication import Divarication
from .Model import Model
import random

class Controller():
    def __init__(self,stores,s_class,s_uri):
        self.stores = stores #Config/Config.py const STORES
        self.s_class = s_class #Config/Config.py const STORES_CLASS
        self.s_uri = s_uri #Config/Config.py const STORES_URI
        

    def return_store(self,var):
        try:
            return self.stores[int(var)-1]
        except IndexError:
            return 

    def main_func(self,list_used_store,article_product):
        
        store = self.receiving_requests(list_used_store,article_product)
        
        return Divarication(store,self.s_class).main_data
        
    def save_data(self,article,main_data):
        model = Model()
        con = model.create_connection()
        arr = []
        for key,valuess in main_data.items():
            name = article + key
            arr.append(name)
            model.execute_query(con,model.create_products_table_template(name))
            for values in valuess:
                m = model.create_products_insert_template(name,model.create_products_values_template(values))
                model.execute_query(con,m)
                
        return arr


    def receiving_requests(self,list_used,article):
        pages = range(1,3)
        store = {}
        for used_store in list_used:
            store[used_store] = []
            try:
                uri = self.s_uri[used_store]
            except KeyError:
                pass
            for page in pages:
                store[used_store].append(uri.format(text = article,page=page))
        return store