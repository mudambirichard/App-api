import os
from app import app
import unittest
class FlaskTestCase(unittest.TestCase):

    def test_requests(self):
        tester = app.test_client(self)
        response = tester.requsets('/api/v1.0/users/requsets', methods=['GET'])
        self.assertFalse( response.data )




if __name__ == '__main__':
    unittest.main()
