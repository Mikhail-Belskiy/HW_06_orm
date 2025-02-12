import sqlalchemy as sq

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher (Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=30), unique = True)

    def __str__(self):
        return f'{self.id}: {self.name}'
    
class Book (Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key = True)
    title = sq.Column(sq.String(length=45), unique = True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable = True)

    publisher = relationship ('Publisher', backref='book')

    def __str__(self):
        return f'{self.id}: {self.title}'


class Shop (Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=30), unique = True)

    def __str__(self):
        return f'{self.id}: {self.name}'
    
class Stock (Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key = True)
    count = sq.Column(sq.String(length=45))
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable = True)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable = True)


    book = relationship ('Book', backref='stock')
    shop = relationship ('Shop', backref='stock')

    def __str__(self):
        return f'{self.id}: {self.count}'
    
class Sale (Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key = True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable = True)
    count = sq.Column(sq.String(length=45))

    stock = relationship ('Stock', backref='sale')

    def __str__(self):
        return f'{self.id}: {self.count}, {self.price}'
    
def create_tables(engine):
    Base.metadata.drop_all(engine) 
    Base.metadata.create_all(engine) 