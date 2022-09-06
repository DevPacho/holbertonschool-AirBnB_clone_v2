#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
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