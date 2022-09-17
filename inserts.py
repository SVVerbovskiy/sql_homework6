import json
from db_connect import DB
from models import Publisher, Book, Sale, Stock, Shop

session = DB.Session


def insert_data_into_tables():
    with open('fixtures/test_data.json', 'r') as f:
        data = json.load(f)

    publishers = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'publisher')
    books = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'book')
    shops = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'shop')
    stocks = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'stock')
    sales = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'sale')

    for publisher in publishers:
        add_record = Publisher(id_publisher=publisher['id'],
                               publisher_name=publisher['fields']['name'])
        session.add(add_record)
        session.commit()

    for book in books:
        add_record = Book(id_book=book['id'],
                          book_title=book['fields']['title'],
                          id_publisher=book['fields']['id_publisher'])
        session.add(add_record)
        session.commit()

    for shop in shops:
        add_record = Shop(id_shop=shop['id'],
                          shop_name=shop['fields']['name'])
        session.add(add_record)
        session.commit()

    for stock in stocks:
        add_record = Stock(id_stock=stock['id'],
                           stock_count=stock['fields']['count'],
                           id_book=stock['fields']['id_book'],
                           id_shop=stock['fields']['id_shop'])
        session.add(add_record)
        session.commit()

    for sale in sales:
        add_record = Sale(id_sale=sale['id'],
                          sale_price=sale['fields']['price'],
                          sale_date=sale['fields']['date_sale'],
                          sale_count=sale['fields']['count'],
                          id_stock=sale['fields']['id_stock'])
        session.add(add_record)
        session.commit()
