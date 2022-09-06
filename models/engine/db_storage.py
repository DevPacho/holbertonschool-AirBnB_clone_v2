#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class DBStorage:
    __engine = None
    __session = None
    classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(getenv('HBNB_MYSQL_USER'),
                                                                           getenv('HBNB_MYSQL_PWD'),
                                                                           getenv('HBNB_MYSQL_HOST'),
                                                                           getenv('HBNB_MYSQL_DB')),
                                                                           pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """List current database session"""
        pass

    def new(self, obj):
        """Adds the object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the db session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables in the database"""

        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()
