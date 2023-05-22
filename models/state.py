#!/usr/bin/python3
"""State Module for HBNB project"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")

    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id
            equals to the current State.id"""
            instance_list = []
            for key, obj in models.storage.all().items():
                if obj.__class__.__name__ == 'City':
                    if obj.state_id == self.id:
                        instance_list.append(obj)
            return instance_list

    def get_cities(self):
        """
        Return the list of City objects linked to the current State.
        """
        if self.__file_storage is not None:
            city_objs = []
            for city in self.__file_storage.all(City).values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
        else:
            return []
