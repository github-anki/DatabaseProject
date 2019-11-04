from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date

meta = MetaData()

engine = create_engine('postgres://docker:docker@localhost/docker', echo=True)

meta.create_all(engine)

students = Table(
    'user', meta,
    Column('user_id', Integer, primary_key=True),
    Column('university_id', Integer),
    Column('name', String),
    Column('email', String),
    Column('surname', String),
    Column('registration_date', Date)
)

conn = engine.connect()
ins = students.insert().values(university_id=1, name='Ravi', surname='Surname', email='a@a.com', registration_date=date.today())
result = conn.execute(ins)
