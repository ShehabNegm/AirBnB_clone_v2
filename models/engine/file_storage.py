#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage based on cls"""

        if cls is None:
            return self.__objects

        else:
            temp_dict = {}
            for k in self.__objects.keys():
                if cls.__name__ in k:
                    temp_dict[k] = self.__objects[k]
        return temp_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        filename = FileStorage.__file_path
        if not os.path.isfile(filename):
            pass

        else:
            with open(filename, 'r') as f:
                r_dict = json.load(f)
                for v in r_dict.values():
                    class_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(class_name)(**v)) 

    def delete(self, obj=None):
        """delete obj from dict"""

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            for k in FileStorage.__objects.keys():
                if key == k:
                    del FileStorage.__objects[k]
                    break
