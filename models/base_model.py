#!/usr/bin/python3
"""Import datetime"""
from datetime import datetime
"""Import uuid"""
import uuid

"""This is the base model for all classes"""
class BaseModel:
    """Here goes the base attributes"""
    def __init__(self):
        """Initializing public attributes

        args:
           id: id of the instance
           created_at: time when the instance is created
           updated_at: time the instance is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Updates the updated_at every time object
           is changed with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """retuns a dictionary containing all keys/values of __dict__"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """Return the following string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
