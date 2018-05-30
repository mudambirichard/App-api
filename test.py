from app import app
import unittest
import requests
import json

BASE_URL = 'http://127.0.0.15000/api/v1/users/requests'
BAD_ITEM_URL = '{}/5'.format(BASE_URL)
GOOD_ITEM_URL ='{}/3'.format(BASE_URL)
class FlaskTestCase(unittest.TestCase):


    def test_user_request(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.15000/api/v1.0/users/requests')
        self.assertEqual( response.status_code, 200 )

    def test_user_request(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.15000/api/v1.0/users/requests/<int:user_id>')
        self.assertEqual(response.status_code, 404 )


if __name__ == '__main__':
    unittest.main()
