#!/usr/bin/python3
"""
This is the base model for all classes
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """Here goes the base attributes"""

    def __init__(self, *args, **kwargs):
        """Initializing public attributes

        args:
            args: non keyword arguments
            kwargs: keyword arguments
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """Updates the updated_at every time object is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

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
