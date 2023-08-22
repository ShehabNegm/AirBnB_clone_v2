#!/usr/bin/python3
# models/engine/db_storage.py
"""represent SQL storage using SQLAlchemy"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Session


class DBStorage:
    """SQL db engine"""

    __engine = None
    __session = None

    def __init__(self):
        """engine initialization"""
        usr = getenv("HBNB_MYSQL_USER")
        psswrd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env =getenv("HBNB_ENV")


        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format
            (usr,
             psswrd,
             host,
             db),
            pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=engine)
        session = Session()

    def all(self, cls=None):
        """return all the obj depending on cls"""

        dict_r = {}
        if cls is None:
            for cl in Base.__subclasses__():
                for obj in self.__session.query(cl).all():
                    key = obj.__class__.__name__ + "." + obj.id
                    dict_r[key] = obj
        else:
            for obj in self.__session.query(eval(cls)).all():
                key = obj.__class__.__name__ + "." + obj.id
                dict_r[key] = obj

        return dict_r
            
