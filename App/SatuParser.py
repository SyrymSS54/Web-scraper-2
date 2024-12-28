from bs4 import BeautifulSoup as bs
import requests

class SatuParser():
    def __init__(self,template,uri):
        self.template = template
        self.uri = uri
        self.data = []
        self.parser()

    def connection(self):
        return requests.get(self.uri)
    
    def parser(self):
        structure = self.template
        soup = bs(self.connection().text,'lxml')
        quotes = soup.find(class_ = structure["prime"])
        quotes = soup.find_all(class_ = structure["card"])
        for quote in quotes:
            name = quote.find(class_ = structure["name"]).text
            price = quote.find(class_ = structure["price"]).text
            local = quote.find(class_ = structure["local"]).text
            self.data.append({"name":name,"price":price,"local":local})

