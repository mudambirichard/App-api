import os
from app import app
import unittest
class FlaskTestCase(unittest.TestCase):

    def test_requests(self):
        tester = app.test_client(self)
        response = tester.requests('/api/v1.0/users/requests', methods=['GET'])
        self.assertFalse( response.data )

    def test_requests(self):
        tester = app.test_client(self)
        response = tester.requests('/api/v1.0/users/requests', methods=['POST'])
        self.assertFalse( response.data )


if __name__ == '__main__':
    unittest.main()
