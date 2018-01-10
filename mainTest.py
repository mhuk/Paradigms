from unittest import TestCase

global wrong_value
wrong_value = "Not correct value."

class TestMenu(TestCase):

    def test_menu(self):
        self.assertRaises(ValueError,wrong_value, )


