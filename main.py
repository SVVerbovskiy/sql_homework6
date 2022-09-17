from db_connect import DB
from models import Publisher, Book, Shop, Stock, create_tables
from inserts import insert_data_into_tables

session = DB.Session


def serching_publisher_name():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите имя издателя: ')
    query_result = query_join.filter(Publisher.publisher_name == query_publisher_name)
    for result in query_result.all():
        print(
            f'Издатель "{query_publisher_name}" найден в магазине "{result.shop_name}" с идентификатором "{result.id_shop}"')


def serching_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_id = input('Введите идентификатор издателя: ')
    query_result = query_join.filter((Publisher.id_publisher == query_publisher_id))
    for result in query_result.all():
        print(
            f'Издатель c id: {query_publisher_id} найден в магазине "{result.shop_name}" с идентификатором "{result.id_shop}"')


if __name__ == '__main__':
    create_tables()
    # insert_data_into_tables()
    serching_publisher_name()
    serching_publisher_id()

session.close()
