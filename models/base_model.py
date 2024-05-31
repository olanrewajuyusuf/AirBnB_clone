#!/usr/bin/python3
from datetime import datetime
import uuid

"""This is the base model for all classes"""
class BaseModel:
    """Here goes the base attributes"""

    def __init__(self):
        """Initializing public attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Updates the updated_at every time object is changed"""
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
