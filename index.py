from App.Controller import Controller
from Config.Config import STORES,STORES_CLASS,STORES_URI
from tkinter import *

if __name__ == "__main__":
    while True:
        try:
            main_request = input("Активирувать программу?(да/нет)")
            if main_request == "да":
                main_object = Controller(STORES,STORES_CLASS,STORES_URI)
                
                print("Выберите магазины:")
                for i in range(1,len(STORES)+1):
                    print(i,STORES[i-1])
                list_used_store = list(map(main_object.return_store,input("").split()))
                article_product = str(input("Какой товар искать?"))

                data = main_object.main_func(list_used_store=list_used_store,article_product=article_product)
                tables = main_object.save_data('headphone',data)
            else:
                break
        except KeyboardInterrupt:
            break