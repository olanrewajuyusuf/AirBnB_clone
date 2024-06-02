"""Test file for base_model"""
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_id_is_unique(self):
        """Test if id is unique for each instance"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object"""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object"""
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test if save method updates updated_at"""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        sleep(0.1)
        bm.save()
        new_updated_at = bm.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_str_method(self):
        """Test the __str__ method for correct format"""
        bm = BaseModel()
        expected_str = f"[BaseModel] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected_str)

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict contains all necessary keys and correct types"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(bm_dict['id'], bm.id)
        self.assertEqual(bm_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(bm_dict['updated_at'], bm.updated_at.isoformat())
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)

    def test_to_dict_output(self):
        """Test the output of to_dict method"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertTrue(all(key in bm_dict for key in expected_keys))
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(bm_dict['id'], bm.id)
        self.assertEqual(bm_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(bm_dict['updated_at'], bm.updated_at.isoformat())

    def test_recreate_instance_from_dict(self):
        """Test if an instance can be recreated from a dictionary"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertEqual(bm1.id, bm2.id)
        self.assertEqual(bm1.created_at, bm2.created_at)
        self.assertEqual(bm1.updated_at, bm2.updated_at)
        self.assertNotIn('__class__', bm2.__dict__)

if __name__ == '__main__':
    unittest.main()
