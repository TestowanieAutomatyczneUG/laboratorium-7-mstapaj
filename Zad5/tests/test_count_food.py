import unittest
from src.count_food import count_food


class test_count_food(unittest.TestCase):

    def setUp(self):
        self.temp = count_food()

    def test_count_list_meals_by_first_letter(self):
        self.assertEqual(4, self.temp.count_list_meals_by_first_letter('a'))

    def test_count_list_meals_by_first_letter_2(self):
        self.assertEqual(7, self.temp.count_list_meals_by_first_letter('h'))

    def test_count_list_meals_by_first_letter_string(self):
        self.assertRaises(ValueError, self.temp.count_list_meals_by_first_letter, 'abc')

    def test_count_list_meals_by_first_letter_long_string(self):
        self.assertRaises(ValueError, self.temp.count_list_meals_by_first_letter, 'abcasssssssczxcasdfasdSASD')

    def test_count_list_meals_by_first_letter_number_string(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, '2')

    def test_count_list_meals_by_first_letter_empty_string(self):
        self.assertRaises(ValueError, self.temp.count_list_meals_by_first_letter, '')

    def test_count_list_meals_by_first_letter_array(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, [])

    def test_count_list_meals_by_first_letter_object(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, {})

    def test_count_list_meals_by_first_letter_none(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, None)

    def test_count_list_meals_by_first_letter_true(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, True)

    def test_count_list_meals_by_first_letter_False(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, False)

    def test_count_list_meals_by_first_letter_int(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, 23)

    def test_count_list_meals_by_first_letter_float(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, 2.1233)

    def test_count_list_meals_by_first_letter_negative_int(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, -21)

    def test_count_list_meals_by_first_letter_negative_float(self):
        self.assertRaises(TypeError, self.temp.count_list_meals_by_first_letter, -2.451)

    def test_count_meals_filtered_by_main_ingredient(self):
        self.assertEqual(9, self.temp.count_meals_filtered_by_main_ingredient('chicken_breast'))

    def test_count_meals_filtered_by_main_ingredient_2(self):
        self.assertEqual(3, self.temp.count_meals_filtered_by_main_ingredient('Lamb'))

    def test_count_meals_filtered_by_main_ingredient_wrong_name(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, 'random')

    def test_count_meals_filtered_by_main_ingredient_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, 'sand')

    def test_count_meals_filtered_by_main_ingredient_array(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, [])

    def test_count_meals_filtered_by_main_ingredient_object(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, {})

    def test_count_meals_filtered_by_main_ingredient_none(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, None)

    def test_count_meals_filtered_by_main_ingredient_true(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, True)

    def test_count_meals_filtered_by_main_ingredient_False(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, False)

    def test_count_meals_filtered_by_main_ingredient_int(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, 23)

    def test_count_meals_filtered_by_main_ingredient_float(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, 2.1233)

    def test_count_meals_filtered_by_main_ingredient_negative_int(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, -21)

    def test_count_meals_filtered_by_main_ingredient_negative_float(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_main_ingredient, -2.451)

    def test_count_meals_filtered_by_category(self):
        self.assertEqual(27, self.temp.count_meals_filtered_by_category('Seafood'))

    def test_count_meals_filtered_by_category_2(self):
        self.assertEqual(64, self.temp.count_meals_filtered_by_category('Dessert'))

    def test_count_meals_filtered_by_category_wrong_name(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, 'random')

    def test_count_meals_filtered_by_category_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, 'water')

    def test_count_meals_filtered_by_category_array(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, [])

    def test_count_meals_filtered_by_category_object(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, {})

    def test_count_meals_filtered_by_category_none(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, None)

    def test_count_meals_filtered_by_category_true(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, True)

    def test_count_meals_filtered_by_category_False(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, False)

    def test_count_meals_filtered_by_category_int(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, 23)

    def test_count_meals_filtered_by_category_float(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, 2.1233)

    def test_count_meals_filtered_by_category_negative_int(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, -21)

    def test_count_meals_filtered_by_category_negative_float(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_category, -2.451)

    def test_count_meals_filtered_by_area(self):
        self.assertEqual(13, self.temp.count_meals_filtered_by_area('Canadian'))

    def test_count_meals_filtered_by_area_2(self):
        self.assertEqual(8, self.temp.count_meals_filtered_by_area('Polish'))

    def test_count_meals_filtered_by_area_wrong_name(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, 'USA')

    def test_count_meals_filtered_by_area_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, 'random')

    def test_count_meals_filtered_by_area_array(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, [])

    def test_count_meals_filtered_by_area_object(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, {})

    def test_count_meals_filtered_by_area_none(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, None)

    def test_count_meals_filtered_by_area_true(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, True)

    def test_count_meals_filtered_by_area_False(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, False)

    def test_count_meals_filtered_by_area_int(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, 23)

    def test_count_meals_filtered_by_area_float(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, 2.1233)

    def test_count_meals_filtered_by_area_negative_int(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, -21)

    def test_count_meals_filtered_by_area_negative_float(self):
        self.assertRaises(TypeError, self.temp.count_meals_filtered_by_area, -2.451)
