import unittest
from app.models import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class UserModelTestCase(unittest.TestCase):
    def test_token_confirmation(self):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
        token = s.dumps({'confirm': 23})
        self.assertTrue(s.loads(token) == {'confirm': 23})