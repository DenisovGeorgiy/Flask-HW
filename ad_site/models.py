from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

# from sqlalchemy.orm import session

# менеджер сессий (что-то вроде курсоров):
from sqlalchemy.orm import sessionmaker

# колонки и типы данных,
# а func - для проставления текущей Даты и Времени
from sqlalchemy import Column, Integer, String, DateTime, func



engine = create_engine(
    'postgresql://postgres:gosha23452453@127.0.0.1:5431/flask_hw'
)


Session = sessionmaker(engine)

Base = declarative_base(bind=engine)


class User(Base):

    __tablename__ = 'ad_users'


    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
        )
    username = Column(
        String,
        nullable=False,
        unique=True,
        index=True
        )
    password = Column(
        String,
        nullable=False
        )
    email = Column(
        String,
        nullable=False,
        index=True
        )
    creation_time = Column(
        DateTime,
        server_default=func.now()
        )


class Ad(Base):
    __tablename__ = 'ads'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
        )
    header = Column(
        String,
        nullable=False,
        index=True
        )
    description = Column(
        String
        )
    creation_time = Column(
        DateTime,
        server_default=func.now()
        )
    user_id = Column(
        Integer,
        nullable=False
    )



Base.metadata.create_all()
