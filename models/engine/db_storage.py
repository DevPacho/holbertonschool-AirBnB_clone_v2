#!/usr/bin/python3
"""Module that defines the new engine 'DBStorage' for MySQL"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Engine for connect to MySQL"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of the database"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Get all objects of a class or all the classes"""

        objects = {}

        if cls:
            query = self.__session.query(cls).all()

            for object in query:
                objects[f"{object.__class__}.{object.id}"] = object

        else:
            classes = [State, Place, User, City, Review, Amenity]
            for input_class in classes:
                query = self.__session.query(input_class).all()

                for object in query:
                    objects[f"{object.__class__}.{object.id}"] = object
        return objects

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
        my_session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()

    def close(self):
        """Call 'remove()' method on the private session attribute"""
        self.__session.close()
