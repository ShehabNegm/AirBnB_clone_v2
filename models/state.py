#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """get list of the cities along with state ID"""

            c = models.storage.all(models.classes['City']).values()
            c_list = []
            for i in c:
                if i.state_id == self.id:
                    c_list.append(i)
            return c_list
