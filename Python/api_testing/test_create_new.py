import requests
import json
import unittest

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        
        body = {'name': 'avi', 'job': 'qa'}
        url = r'https://reqres.in/api/users'
        response = requests.post(url, body) # will show the numeric response (200, 300, 400, 500)
        self.status = response.status_code # will return the status code of the request
        content = response.content # will return the body in json format
        header = response.headers # will return the header in json fromat
        get_length = response.headers.get('Content-Length')
        self.json_respons = json.loads(response.text) # parse the response into json

    def test_total_pages(self):
        self.assertEqual(self.status, 201)

if __name__ == '__main__':
    unittest.main()