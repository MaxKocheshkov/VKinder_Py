# import unittest
# import requests
# import vk_data
# import user_data
#
#
# class VkTests(unittest.TestCase):
#
#     def test_user_response(self):
#         resp = requests.get('http://api.vk.com/method/users.get')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_search_response(self):
#         resp = requests.get('https://api.vk.com/method/users.search')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_token(self):
#         self.assertTrue(vk_data.TOKEN)

    # def test_translate(self):
    #     test_input = 'This is test message'
    #     self.assertIsNotNone(vk_data.(test_input))
    #
    # def test_negativ_status(self):
    #     resp = requests.get('http://translate.yandex.ru')
    #     self.assertEqual(resp.status_code, 402, msg='API-ключ заблокирован')
    #
    # def test_negativ_translate(self):
    #     test_input = None
    #     self.assertIsNotNone(translator.translate_it(test_input), msg='Отсутствует текст для перевода')