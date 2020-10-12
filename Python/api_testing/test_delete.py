import requests
import json
import unittest

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        
        url = r'https://reqres.in/api/users/2'
        response = requests.delete(url) # will show the numeric response (200, 300, 400, 500)
        self.status = response.status_code # wull return the status code of the request

    def test_status_code(self):
        self.assertEqual(self.status, 204)


if __name__ == '__main__':
    unittest.main()