# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import shutil

if __name__ == "_main__":
    def get_webdriver_options():
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-features=NetworkService")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-features=VizDisplayCompositor")
        return options
    
    def get_chromedriver_path():
        print(shutil.which('chromedriver'))
        return shutil.which('chromedriver')

    def get_webdriver_service():
        service = Service(
            executable_path=get_chromedriver_path(),
        )
        
        return service
    browser = webdriver.Chrome(options=get_webdriver_options(), service=get_webdriver_service())
    browser.get('https://global.wildberries.ru/catalog?search=гирлянда&tail-location=SNS')
    time.sleep(5)
    print(browser.page_source)
    
arr ={'Satu': [[{'name': 'Гирлянды на батарейках, набор 4 шт', 'price': '1 900\xa0₸', 'local': 'Интернет-магазин Market VK'}, {'name': 'Гирлянда "Дождик" 3х0,7м', 'price': '3 500\xa0₸', 'local': 'Упакуй.kz'}, {'name': 'Гирлянда "Подвесные звезды" ,теплый свет, 3м', 'price': '6 500\xa0₸', 'local': 'Упакуй.kz'}, {'name': 'Гирлянды светодиодные, новогодние, уличные ВОДОПАДЫ 3*1 метр', 'price': 'от\xa03 500\xa0₸', 'local': 'TОО «SD Reliable Company»'}, {'name': 'Светодиодная нить - гирлянда на батарейках теплый свет, 2 м', 'price': '700\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Светодиодная нить - гирлянда на батарейках цветная, 2 м', 'price': '700\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Светодиодная нить - гирлянда на батарейках цветная, 3 м', 'price': '900\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Светодиодная нить - гирлянда на батарейках теплый свет, 3 м', 'price': '900\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Светодиодная нить - гирлянда на батарейках теплый свет, 1 м', 'price': '600\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Светодиодная нить - гирлянда на батарейках цветная, 1 м', 'price': '600\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Гирлянда "Звездочки"', 'price': '5 500\xa0₸', 'local': 'Упакуй.kz'}, {'name': 'Гирлянда " Водопад"', 'price': '7 500\xa0₸', 'local': 'Упакуй.kz'}, {'name': 'Ретро гирлянда цоколь Е27 в стиле лофт', 'price': '1 250\xa0₸', 'local': 'Kazmir Svet'}, {'name': 'Гирлянды светодиодные, новогодние, уличная LED гирлянда "ШТОРКИ ЗАНАВЕС" 2*2 метра', 'price': 'от\xa04 000\xa0₸', 'local': 'TОО «SD Reliable Company»'}, {'name': 'Ретро-гирлянда Белт Лайт влагозащищенная черная', 'price': 'от\xa01 000\xa0₸/м', 'local': 'TОО «SD Reliable Company»'}, {'name': 'Гирлянда "Тающая сосулька", гирлянда тубус', 'price': 'от\xa0980\xa0₸', 'local': 'TОО «SD Reliable Company»'}, {'name': 'Ретро гирлянда "Белт Лайт" влагозащищенная, черная', 'price': 'от\xa01 000\xa0₸/м', 'local': 'TОО «SD Reliable Company»'}, {'name': 'Ретро гирлянда "Белт Лайт" влагозащищенная, белая', 'price': 'от\xa01 000\xa0₸/м', 'local': 'TОО «SD Reliable Company»'}, {'name': 'Флажки, гирлянды', 'price': 'от\xa0200\xa0₸', 'local': 'Услуга'}, {'name': 'ГИРЛЯНДА ШАРИКИ ПРОЗРАЧНЫЕ', 'price': '4 120\xa0₸', 'local': 'Садовый центр BALNUR'}, {'name': 'Гирлянда LED 300 лампочек', 'price': '3 900\xa0₸', 'local': 'Wellshop'}, {'name': 'Гирлянда "Водопад", теплый свет, 3х3м', 'price': '6 000\xa0₸', 'local': 'Магазин-склад "МУРАШ-АТА"'}, {'name': 'Гирлянда с подвесными звездочками, теплый свет', 'price': '5 000\xa0₸', 'local': 'Магазин-склад "МУРАШ-АТА"'}, {'name': 'Гирлянда "Водопад", холодный свет, 3х3м', 'price': '6 000\xa0₸', 'local': 'Магазин-склад "МУРАШ-АТА"'}, {'name': 'Гирлянда на батарейках 3м тёплый', 'price': '850\xa0₸', 'local': 'Магазин-склад "МУРАШ-АТА"'}, {'name': 'Гирлянда-подвесная, круглая, 2 шт.', 'price': '460\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Гирлянда-венок "С новым годом", картонная, 35 см', 'price': '750\xa0₸', 'local': 'Интернет-магазин VPROK.kz'}, {'name': 'Праздничный набор для Дня рождения (6 тарелок, 6 стаканов, 6 колпачков+ Гирлянда в подарок!)', 'price': '3 590\xa0₸', 'local': 'Магазин приятных покупок LotOk.kz'}, {'name': 'Гирлянда уличная «Нить» цвет свечения белый', 'price': '5 990\xa0₸', 'local': 'Магазин приятных покупок LotOk.kz'}, {'name': 'Гирлянда фонарики', 'price': '2 590\xa0₸', 'local': 'Магазин приятных покупок LotOk.kz'}, {'name': 'Подвесная гирлянда «Скелеты»', 'price': '1 290\xa0₸', 'local': 'Магазин приятных покупок LotOk.kz'}, {'name': 'Набор для опытов «Новогодняя гирлянда с шариками Орбиз»', 'price': '2 490\xa0₸', 'local': 'Магазин приятных покупок LotOk.kz'}, {'name': 'Набор из шести гирлянд на Хэллоуин', 'price': '1 790\xa0₸', 'local': 'Магазин приятных покупок LotOk.kz'}, {'name': 'Гирлянда пластик белая 005601', 'price': '8 490\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'Гирлянда 130см золотая 726415', 'price': '13 900\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'Гирлянда пластик 130см белая 474027', 'price': '9 990\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'LED гирлянда 1000 ламп 22,5м мультиколор 495367', 'price': '29 990\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'LED гирлянда 2000 ламп 45м тёпло-белый свет 495360', 'price': '54 990\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'LED гирлянда 7,25м свечи 30шт 483298', 'price': '26 690\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'LED кластерная гирлянда 3000 ламп 27м тепло-белый свет 494743', 'price': '85 990\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'LED кластерная гирлянда черный провод 1440 ламп 9м тепло-белый свет 496740', 'price': '74 990\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'LED кластерная гирлянда черный провод 960 ламп 6м тепло-белый свет 496736', 'price': '47 950\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'ГИРЛЯНДА ХОЛОДНЫЙ СВЕТ 2000 ЛАМП, 8 ФУНКЦИЙ, ДЛЯ ЕЛКИ 260СМ, для наруж. и внутрен. использ.', 'price': '49 900\xa0₸', 'local': 'ВИСИПЕТ'}, {'name': 'Гирлянды светодиодные, новогодние, уличная LED гирлянда "ШТОРКИ ЗАНАВЕС" длина: 2-6 метров', 'price': 'от\xa09 500\xa0₸', 'local': 'TОО «SD Reliable Company»'}, {'name': 'Гирлянда светодиодная Палочки с пузырьками 20 палочек, цвет: мультиколор, 2 метра', 'price': '2 462\xa0₸', 'local': '220 VOLT'}, {'name': 'Гирлянда Шарики Ø15мм, 5м, темно-зеленый ПВХ, 30 диодов, цвет RGB', 'price': '4 812\xa0₸', 'local': '220 VOLT'}, {'name': 'Гирлянда Шарики Ø18 мм, 5 м, темно-зеленый ПВХ, 30 диодов, цвет RGB', 'price': '5 267\xa0₸', 'local': '220 VOLT'}, {'name': 'Гирлянда Шарики Ø18мм, 5м, темно-зеленый ПВХ, 30 диодов, цвет RGB', 'price': '5 267\xa0₸', 'local': '220 VOLT'}, {'name': 'Гирлянда Шарики Ø25 мм, 5м, темно-зеленый ПВХ, 25 диодов, цвет белый, без контроллера', 'price': '5 398\xa0₸', 'local': '220 VOLT'}, {'name': 'Гирлянда Шарики Ø25мм, 5м, темно-зеленый ПВХ, 25 диодов, цвет RGB', 'price': '5 853\xa0₸', 'local': '220 VOLT'}, {'name': 'Гирлянда Шарики Ø30мм, 5м, темно-зеленый ПВХ, 25 диодов, цвет RGB', 'price': '7 156\xa0₸', 'local': '220 VOLT'}, {'name': 'Елочная гирлянда с кольцом, 7 нитей по 1,5 метра, цвет диодов белый, не соединяется', 'price': '7 485\xa0₸', 'local': '220 VOLT'}, {'name': 'Елочная гирлянда с кольцом, 7 нитей по 1,5 метра, цвет диодов мультиколор, не соединяется', 'price': '7 485\xa0₸', 'local': '220 VOLT'}, {'name': 'Гирлянда Нить 10 м LED теплый цвет', 'price': '2 900\xa0₸', 'local': 'A and A'}, {'name': 'Гирлянда LED TWL-50 5 м теплый белый цвет', 'price': '12 500\xa0₸', 'local': 'Ellmart'}, {'name': 'Гирлянда Нить 8 м, теплый белый цвет', 'price': '6 000\xa0₸', 'local': 'Ellmart'}, {'name': 'Гирлянда Нить прозрачный шнур 8 м белый цвет', 'price': '3 000\xa0₸', 'local': 'Ellmart'}]]}

print(len(arr['Satu']))