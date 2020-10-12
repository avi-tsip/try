import requests
import json
import unittest

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        
        url = r'https://reqres.in/api/users?page=2'
        response = requests.get(url) # will show the numeric response (200, 300, 400, 500)
        status = response.status_code # wull return the status code of the request
        content = response.content # will return the body in json format
        header = response.headers # will return the header in json fromat
        self.json_respons = json.loads(response.text)

    def test_total_pages(self):
        print(self.json_respons)
        pages = self.json_respons['page']
        self.assertEqual(pages, 2)


if __name__ == '__main__':
    unittest.main()