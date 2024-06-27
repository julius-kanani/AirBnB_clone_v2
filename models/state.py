#!/usr/bin/python3
""" State Module for HBNB project """

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
         __tablename__ = "states"
         name = Column(String(128), nullable=False)
         cities = relationship(
                 'City',
                 back_populates='state',
                 cascade='all, delete, delete-orphan'
         )

    else:
        name = ""

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
