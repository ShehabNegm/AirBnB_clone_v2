#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        cities(self):
            """get list of the cities along with state ID"""

            cities = storage.all(City).values()
            c_list = []
            for i in cities:
                if i['state_id'] == self.id
                c_list.append(i)
            return c_list
