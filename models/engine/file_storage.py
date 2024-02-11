#!/usr/bin/python3
"""Dedines a filestorage class"""

import json


class FileStorage:
    """Class used to serialize and deserialize JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, mode='a', encoding="UTF-8") as f:
            json.dump(serialized, f)
            f.write("\n")

    def get_classes(self):
        """Returns a dictionary of valid classes and their references."""
        return {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
                'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def load(self):
        """Deserializes the JSON file to __objects(Only if the JSON file
        (__file_path)exists; otherwise, does nothing. If the file doesn't exist
        no exception is raised)"""
        try:
            with open(self.__file_path, mode='r', encoding="UTF-8") as f:
                for line in f:
                    data = json.loads(line)
                    classes = self.get_classes()
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj_class = classes.get(class_name)
                        if obj_class:
                            obj = obj_class(**value)
                            self.__objects[key] = obj
        except FileNotFoundError:
            pass

