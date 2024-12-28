from tkinter import *
from tkinter import ttk
from App.Controller import Controller
from Config.Config import STORES,STORES_CLASS,STORES_URI,TEXT,HELP

def app():
    #notebook = ttk.Notebook()
    #notebook.pack(expand=True, fill=BOTH)
    
    frame1 = ttk.Frame()
    text_1 = Text(frame1,width=49,height=7)
    text_1.insert(1.0,TEXT)
    text_1.config(state=DISABLED)
    text_1.grid(column=0,columnspan=4,row=0,rowspan=3)
    
    frame2 = ttk.Frame()
    text_2 = Text(frame2,width=49,height=5)
    text_2.insert(1.0,"Выберите магазины:\n1.AliExpress\n2.Satu\n3.Ozon\n4.WildBerries")
    text_2.config(state=DISABLED)
    text_2.grid(column=0,columnspan=4,row=0,rowspan=2)
    
    combo = ttk.Combobox(frame2)  
    combo['values'] = (1, 2, 3, 4)  
    combo.current(1)  # установите вариант по умолчанию     
    combo.grid(column=0, row=2,padx=0,sticky=W,pady=5,)
    
    frame3 = ttk.Frame(height=300)
    Label(frame3,text="Вводите имя товар:",width=31).grid(column=0,row=0,padx=10,pady=3,sticky=W)
    e1 = Entry(frame3,width=30)
    e1.grid(column=0,row=1,columnspan=4,sticky=W,padx=15)
    Label(frame3,text="",height=4).grid(column=0,row=2,sticky=W)
    
    def table1():
        frame1.forget()
        frame2.pack(fill=BOTH, expand=True)
        
    def table_back_2():
        frame2.forget()
        frame1.pack(fill=BOTH,expand=True) 
        
    def table_forth_2():
        frame2.forget()
        frame3.pack(fill=BOTH,expand=True)  
        
    def table_back_3():
        frame3.forget()
        frame1.pack(fill=BOTH,expand=True) 
        
    def func():
        main_object = Controller(STORES,STORES_CLASS,STORES_URI)
        list_used_store = list(map(main_object.return_store,combo.get()))
        article_product = e1.get()
        print(list_used_store,article_product)
        data = main_object.main_func(list_used_store=list_used_store,article_product=article_product)
        print(data)
        tables = main_object.save_data('product',data)
        
        root = Tk()
        root.title("Таблица")
        root.geometry("600x200") 
        columns = ("name", "price", "local")
 
        tree = ttk.Treeview(root,columns=columns, show="headings")
        tree.pack(fill=BOTH, expand=1)
 
        tree.heading("name", text="name")
        tree.heading("price", text="price")
        tree.heading("local", text="local")
        
        for key,valuess in data.items():
            for values in valuess:
                for value in values:
                    tree.insert("",END,values = (value["name"],value["price"],value["local"]))
        
        root.mainloop()
        
    def func_1():
        win = Tk()
        win.title("Руководство")
        win.geometry("400x400")
        text_help = Text(win)
        text_help.insert(1.0,HELP)
        text_help.config(state=DISABLED)
        text_help.pack(fill=BOTH, expand=1)
        win.mainloop()
    
    Button(frame1,text = "Вперед",command=table1).grid(row=3,column=3,padx=10,pady=10,sticky=E)
    Button(frame1,text = "Руководство",command=func_1).grid(row=3,column=0,padx=10,pady=10,sticky=W)
    
    
    Button(frame2,text = "Назад",command=table_back_2).grid(column=0,row=3,padx=10,pady=10,sticky=W)
    Button(frame2,text = "Вперед",command=table_forth_2).grid(row=3,column=3,padx=10,pady=10,sticky=E)
    
    
    Button(frame3,text = "Назад",command=table_back_3).grid(column=0,row=3,padx=10,pady=10,sticky=W+S)
    Button(frame3,text = "Рассчитать",command=func).grid(row=3,column=3,padx=10,pady=10,sticky=E+S)
    
    
    frame1.pack(fill=BOTH, expand=True)

if __name__ == "__main__":
    window = Tk()
    window.geometry("400x200")
    window.title("Добро пожаловать в Webscraper")
    
    app()
    
    window.mainloop()