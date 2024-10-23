import sqlalchemy as sq

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = 'course'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length = 40), unique = True)

    #homeworks = relationship('Homework', back_populates = 'cours')

    def __str__(self):
        return f'{self.id}: {self.name}'

class Homework(Base):
    __tablename__ = 'homework'

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable = True)
    description = sq.Column(sq.Text, nullable = True)
    course_id= sq.Column(sq.Integer, sq.ForeignKey('course.id'), nullable = True)

    course = relationship('Course', backref = 'homework')

def creat_tables(engine):
   # Base.metadata.drop_all(engine) #удалить все таблицы 
    Base.metadata.create_all(engine) #создать все таблицы 

