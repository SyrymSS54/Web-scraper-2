import sqlite3 
import os 

class Model():
    def __init__(self):
        #self.path = "/home/syrym/Documents/Web scraper 2/App/webscraper.db"
        self.path = os.path.abspath("App/webscraper.db")
        print(self.path)
        
    def create_products_table_template(self,article):
        return f""" CREATE TABLE IF NOT EXISTS {article} (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,price TEXT NOT NULL,local TEXT NOT NULL)"""
    
    def create_products_values_template(self,tables):
        tabl = ""
        len_tables = len(tables)
        for i in range(len_tables):
            table = tables[i]
            tabl += f"""('{table['name']}', '{table['price']}', '{table['local']}')"""
            if i == (len_tables-1):
                tabl += ";"
            else:
                tabl += ","
        return tabl
    
    def create_products_insert_template(self,article,table):
        return f"""INSERT INTO {article} (name,price,local) VALUES {table}"""
        
    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.path)
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            
        return connection
    
    def execute_query(self,connection,query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query execute successfully")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

if __name__ == "__main__":
    model = Model()
    con = model.create_connection()
    model.execute_query(con,model.create_products_table_template("syr"))
    m = model.create_products_insert_template("syr",model.create_products_values_template([{'name':'oil','price':'100','local':'Russia'}]))
    model.execute_query(con,m)