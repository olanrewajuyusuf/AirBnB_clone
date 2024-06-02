#!/usr/bin/python3
"""import file_storage.py"""
from models.engine.file_storage import FileStorage

"""create an instance of FileStorage"""
storage = FileStorage()
"""call reload() method"""
storage.reload()
