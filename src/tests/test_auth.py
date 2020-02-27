import unittest
from src.omnitradeClient.auth import Auth

ACCESS_KEY = '123456'
SECRET_KEY = '123456'
class TestAuthMethods(unittest.TestCase):
    def test_signed_challenge(self):
        auth = Auth(ACCESS_KEY, SECRET_KEY)

        subject = auth.signed_challenge('challenge')

        self.assertEqual(list(subject.keys()), ['auth'])
        self.assertEqual(list(subject['auth'].keys()), ['access_key', 'answer'])

    def test_signed_params(self):
        auth = Auth(ACCESS_KEY, SECRET_KEY)

        subject = auth.signed_params('GET', 'api/v2/order_markets', volume = 0, total = 0 )

        self.assertEqual(sorted(subject.keys()), sorted(['volume', 'access_key', 'tonce', 'total', 'signature']))
