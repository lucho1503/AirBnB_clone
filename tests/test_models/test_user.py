#!/usr/bin/python3
"""
test User - this test perform the User class test
"""
import unittest
from models.user import User


class Test_Base_Model(unittest.TestCase):
    """ class Test_Base_model """

    def test_hasattribute(self):
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

    def test_type(self):
        t = User()
        self.assertEqual(type(t.email), str)
        self.assertEqual(type(t.password), str)
        self.assertEqual(type(t.first_name), str)
        self.assertEqual(type(t.last_name), str)

    def test_instance(self):
        i = User()
        assert isinstance(i, User)
