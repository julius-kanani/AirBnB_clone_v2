#!/usr/bin/env python3
""" The db_storage module that provides database access. """


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "Place": Place, "City": City, "State": State, "Review": Review }

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
                f'mysql+mysqldb://{user}:{password}@{host}/{database}',
                pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dcit = {}

        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs=[]
            for _class in classes.values():
                objs.extend(self.__session.query(_class).all())

        for obj in objs:
            key = f'{obj.__class__.__name__}.{obj.id}'
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()
