import unittest
import requests

class VkTests(unittest.TestCase):

    def test_user_response(self):
        resp = requests.get('http://api.vk.com/method/users.get')
        self.assertEqual(resp.status_code, 200)

    def test_search_response(self):
        resp = requests.get('https://api.vk.com/method/users.search')
        self.assertEqual(resp.status_code, 200)

    def test_negativ_status(self):
        resp = requests.get('http://api.vk.com/method/users.get')
        self.assertEqual(resp.status_code, 3609, msg='Token extension required')


