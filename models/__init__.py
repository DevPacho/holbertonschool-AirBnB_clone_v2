#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
# from os import getenv

""" if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
