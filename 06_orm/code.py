import json
from traceback import print_tb
import sqlalchemy 
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:Mb20041995@localhost:5432/shop_book"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('/home/mikl/Рабочий стол/homework/sql_PY_Alch/06_orm/tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

publisher_input = input("Введите имя или ID издателя: ")

is_id = publisher_input.isdigit()
if is_id:
    publisher = session.query(Publisher).filter_by(id=int(publisher_input)).first()
else:
    publisher = session.query(Publisher).filter_by(name=publisher_input).first()

if publisher:
    purchase_records = (
        session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .join(Stock, Stock.id == Sale.id_stock)
        .join(Book, Stock.id_book == Book.id)
        .join(Shop, Stock.id_shop == Shop.id)
        .filter(Book.id_publisher == publisher.id)
        .all()
    )

    if purchase_records:
        print("Название книги | Название магазина | Стоимость покупки | Дата покупки")
        for record in purchase_records:
            print(f"{record[0]} | {record[1]} | {record[2]} | {record[3]}")
    else:
        print("Нет фактов покупки книг этого издателя.")
else:
    print("Издатель не найден.")

