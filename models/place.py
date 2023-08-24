#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import ForeignKey
from models.city import City
from models.user import User
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Table


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60),ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60),ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)

    else:
        @porperty
        def reviews(self):
            """get reviews"""
            rvw = models.storage.all(models.classes['Review']).values()
            r_list = []
            for i in rvw:
                if i.place_id == self.id:
                    r_list.append(i)
            return r_list

        @property
        def amenities(self):
            """get aminities"""
            amn = models.storage.all(models.classes['Amenity']).values()
            a_list = []
            for i in amn:
                if i.id in self.amenity_ids:
                    a_list.append(i)
            return a_list

        @amenities.setter
        def amenities(self, obj):
            """set amenities"""
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)


