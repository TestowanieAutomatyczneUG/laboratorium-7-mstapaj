import unittest
from src.ValidPassword import ValidPassword


class test_ValidPassword(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()

    def test_ValidPassword_correct(self):
        self.assertEqual(True, self.temp.check('abcDEF2@'))

    def test_ValidPassword_correct_2(self):
        self.assertEqual(True, self.temp.check('ABC2cdef$%'))

    def test_ValidPassword_very_long(self):
        self.assertEqual(True, self.temp.check(
            'abcccccccccccccccc@@@@@@cccccccsss!!!!!!!!sssssssssssssssaaaaaaaa3333333$$$$$$DEF2@'))

    def test_ValidPassword_too_short(self):
        self.assertEqual(False, self.temp.check('aDEF2@'))

    def test_ValidPassword_no_number(self):
        self.assertEqual(False, self.temp.check('abcdsDEF@'))

    def test_ValidPassword_no_symbol(self):
        self.assertEqual(False, self.temp.check('abcdDEF2a'))

    def test_ValidPassword_no_uppercase(self):
        self.assertEqual(False, self.temp.check('abcdefs2@'))

    def test_ValidPassword_empty_string(self):
        self.assertEqual(False, self.temp.check(''))

    def test_ValidPassword_only_lowercase(self):
        self.assertEqual(False, self.temp.check('aaaaaabbbb'))

    def test_ValidPassword_only_sybmols(self):
        self.assertEqual(False, self.temp.check('###$$$$&&***'))

    def test_ValidPassword_only_numbers(self):
        self.assertEqual(False, self.temp.check('222333115566'))

    def test_ValidPassword_array(self):
        self.assertRaises(TypeError, self.temp.check, [])

    def test_ValidPassword_object(self):
        self.assertRaises(TypeError, self.temp.check, {})

    def test_ValidPassword_none(self):
        self.assertRaises(TypeError, self.temp.check, None)

    def test_ValidPassword_true(self):
        self.assertRaises(TypeError, self.temp.check, True)

    def test_ValidPassword_False(self):
        self.assertRaises(TypeError, self.temp.check, False)

    def test_ValidPassword_int(self):
        self.assertRaises(TypeError, self.temp.check, 23)

    def test_ValidPassword_float(self):
        self.assertRaises(TypeError, self.temp.check, 2.1233)

    def test_ValidPassword_negative_int(self):
        self.assertRaises(TypeError, self.temp.check, -21)

    def test_ValidPassword_negative_float(self):
        self.assertRaises(TypeError, self.temp.check, -2.451)

    def tearDown(self):
        self.temp=None
