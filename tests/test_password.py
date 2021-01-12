import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self): # Tests the ability to set a password
        u = User(password='randompassword')
        self.assertTrue(u.password_hash is not None)
    
    def test_no_password_getter(self):
        u = User(password='randompassword')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='randompassword')
        self.assertTrue(u.verify_password('randompassword'))
        self.assertFalse(u.verify_password('falsepassword'))

    def test_password_salts_are_random(self):
        u = User(password='randompassword')
        u2 = User(password='randompassword')
        self.assertTrue(u.password_hash != u2.password_hash)


