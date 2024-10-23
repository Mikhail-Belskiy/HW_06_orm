import sqlalchemy 
from sqlalchemy.orm import sessionmaker

from mosels import creat_tables, Course, Homework

DSN = "postgresql://postgres:Mb20041995@localhost:5432/netilogy"
engine = sqlalchemy.create_engine(DSN)


creat_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

course_1 = Course(name = 'Python')

session.add(course_1)
session.commit


print(course_1)

hw1 = Homework(number=1, description="первое задание", course=course_1)
hw2 = Homework(number=2, description="второе задание (сложное)", course=course_1)

#session.add(js)
#print(js.id)
session.add_all([hw1, hw2])
session.commit()  # фиксируем изменения
#print(js.id)

session.close()


