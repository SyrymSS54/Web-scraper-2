from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import shutil
import time
class AliParser():
    def __init__(self,template,uri):
        self.template = template
        self.uri = uri
        self.data = []
        self.parser()
        
    def get_webdriver_options(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-features=NetworkService")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-features=VizDisplayCompositor")
        return options
    
    def get_chromedriver_path(self):
        return shutil.which('chromedriver')
    
    
    def get_webdriver_service(self):
        service = Service(
            executable_path=self.get_chromedriver_path(),
        )
        
        return service

    def connection(self):
        browser = webdriver.Chrome(options = self.get_webdriver_options(), service = self.get_webdriver_service())
        browser.get(self.uri)
        time.sleep(5)
        return browser.page_source
    
    def parser(self):
        structure = self.template
        print(self.connection())
        soup = bs(self.connection(),'lxml')
        quotes = soup.find(class_ = structure["prime"])
        quotes = soup.find_all(class_ = structure["card"])
        for quote in quotes:
            name = quote.find(class_ = structure["name"]).text
            price = quote.find(class_ = structure["price"]).text
            local = quote.find(class_ = structure["local"]).text
            self.data.append({"name":name,"price":price,"local":local})