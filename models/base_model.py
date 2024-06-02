#!/usr/bin/python3
from datetime import datetime
import uuid

"""This is the base model for all classes"""
class BaseModel:
    """Here goes the base attributes"""

    def __init__(self, *args, **kwargs):
        """Initializing public attributes

        args:
            args: non keyword arguments
            kwargs: keyword arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.__post_init__()

    def __post_init__(self):
        """call new method"""
        from models import storage
        storage.new(self)

    def save(self):
        """Updates the updated_at every time object is changed"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

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
