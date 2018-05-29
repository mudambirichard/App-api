from app import app
import unittest

def test_requests(self):
    tester = app.test_client(self)
    response = tester.requests('/api/v1.0/requests')
    self.assertFalse( response.data )

if __name__ == '__main__':
    unittest.main()
