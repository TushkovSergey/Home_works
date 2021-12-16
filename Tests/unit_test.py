from unittest.mock import patch

import unittest
import secretary
import yandex

class TestSecretary(unittest.TestCase):
    def setUp(self): print("method setUp")
    def tearDown(self): print("method tearDown")

    @patch('secretary.get_input', return_value='2207 876234')
    def test_selfs(self, input):
        self.assertEqual(secretary.shelfs(), 'Документ находится на полке 1')

    @patch('secretary.get_input', return_value='10006')
    def test_delete(self, input):
        self.assertNotIn('10006', secretary.delete_doc())

    def test_add(self):
        type = "passport"
        number = "123"
        name = "Sokolov"
        shelf = '3'
        self.assertIn(({"type": type, "number": number, "name": name}), secretary.add(type, number, name, shelf))

class TestYandex(unittest.TestCase):
    def setUp(self): print("method setUp")

    def tearDown(self): print("method tearDown")

    def test_yandex(self):
        path = 'My_folder1'
        token = ''
        self.assertEqual(yandex.create_folder(path, token), 201)
        self.assertEqual(yandex.create_folder(path, token), 409)
        self.assertEqual(yandex.create_folder(path, '1'), 401)