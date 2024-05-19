#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """This method will return the list of objects of one type of class"""
        if cls is None:
            return self.__objects
        else:
            nameofclass = cls.__name__
            newdic = {}
            for onekey in self.__objects.keys():
                if (onekey.split('.')[0] == nameofclass):
                    newdic[onekey] = self.__objects[onekey]
            return newdic

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
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """This method will delete the obj from __objects"""
        if obj is None:
            return

        which_obj = obj.to_dict()['__class__'] + '.' + obj.id
        if which_obj in self.__objects.keys():
            del self.__objects[which_obj]

    def close(self):
        """This function will be used to deserialize the JSON file to objects"""
        self.reload()
