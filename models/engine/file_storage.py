#!/usr/bin/python3

"""
    Define FileStorage class
"""

import json
import models


class FileStorage:
    """Represent a FileStorage

        ATTRIBUTES:
        -----------
        __file_path (str): name of the JSOn file to save the data in.
        __objects (dict): store all objects by <class name>.id

        METHODS:
        --------
        all(self): return dict __objects
        new(self, obj): add new object in __objects with
        key <obj class name>.id
        save(self): serialize __objects to the JSON file
        with path __file_path
        reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all the objects saved in the file"""
        print("In ALL ({})!!!!!".format(len(self.__objects)))
        return self.__objects

    def new(self, obj):
        """Add a new object into objects dictionary"""
        obj_id = obj.__class__.__name__ + '.' + obj.id
        self.__objects[obj_id] = obj

    def save(self):
        """Save object representation of JSON to a file"""

        with open(self.__file_path, mode='w', encoding='UTF-8') as jsonFile:
            to_json = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(to_json, jsonFile)

    def reload(self):
        """Function that creates an Object from a JSON file"""

        from_json = {}
        try:
            with open("//wsl.localhost/Ubuntu-22.04/home/nour-m-ibrahim/ALX\AirBnB_clone/file.json", mode='r', encoding="UTF-8") as jsonFile:
                from_json = json.loads(jsonFile)
                for key, value in from_json.items():
                    attr_class_name = value.pop("__class__")
                    self.new(eval(attr_class_name)(**value))
        except:
            print("Didn't Read Any File XXXXXXXXXX----")
            pass
