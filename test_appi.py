import json
import unittest
import app as my_app
from flask import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = my_app.app.test_client()

    def test_page_list(self):
        my_app.page = []
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        
if __name__ == '__main__':
    unittest.main() 