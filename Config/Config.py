STORES = ['AliExpress','Satu','Ozon','WildBerries']

STORES_URI = {
    "AliExpress":"https://aliexpress.ru/wholesale?SearchText={text}&g=y&page={page}",
    "Satu":"https://satu.kz/search?search_term={text}&page={page}",
    "Ozon":"https://ozon.kz/search/?from_global=true&text={text}&page={page}",
    "WildBerries":"https://www.wildberries.by/catalog?search={text}&tail-location=SNS&page={page}"
}

STORES_CLASS = {
    "AliExpress":{
        "prime":"product-snippet_ProductSnippet__grid__w6hatm product-snippet_ProductSnippet__vertical__w6hatm SnowSearchProductFeed_List__grid__vmkcs",
        "card":"product-snippet_ProductSnippet__content__w6hatm",
        "name":"product-snippet_ProductSnippet__name__w6hatm",
        "price":"snow-price_SnowPrice__mainM__1cmks6",
        "local":"product-snippet_ProductSnippet__caption__w6hatm"
    },
    "Satu":{
        "prime":"MafxA Nt5uf tPYLO QdzA1 BmN-- UQxaL",
        "card":"M3v0L DUxBc sMgZR _5R9j6 wEofQ qzGRQ IM66u J5vFR hxTp1",
        "name":"_3Trjq htldP _7NHpZ h97_n",
        "price":"bkjEo",
        "local":"_3Trjq aXB7S"
    },
    "Ozon":{
        "prime":"xi7",
        "card":"v4i vi5",
        "name":"tile-hover-target si5 i6s",
        "price":"c3118-a1 tsHeadline500Medium c3118-b9",
        "local":None
    },
    "WildBerries":{
        "prime":"card-grid",
        "card":"card-cell",
        "name":"b-card__name",
        "price":"price__lower",
        "local":"b-card__brand"}}

TEXT = "Привет,это приложение Webscraper.\nWebscraper-ы подключается к веб-сайтом и парсить.\nА этот приложение подключается к магазинам и получает цены товаров.\nТакие как 1.AliExrpress,2.Satu,3.Ozon,4.WildBerries"

HELP = "Привет, это руководство программы Webscraper!\nЯ тут чтобы тебе помоч\nЧтобы начать работы программы\n1.Запусти файл viewer.py\n2.В первом привественном окне нажми 'Вперед'\n3.На окне выбора магазина выбери магазин и 'Вперед'\n4.В четвертом окне введи имя товара которые ты хочеш найти и нажми 'Рассчитать'\n5.Выйдет окно с результатом\n\nСостояние выполнение процесса и приложения можно увидить в терминале\n\nДля запуска проекта вам понадабиться python,tkinter и sqlite3\n\nНавигация по приложению идет через кнопки 'Назад' и 'Вперед'"