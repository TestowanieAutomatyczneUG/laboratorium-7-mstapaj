import unittest
from src.search_food import search_food


class test_search_food(unittest.TestCase):

    def setUp(self):
        self.temp = search_food()

    def test_search_meal_by_name(self):
        self.assertEqual(
            [{'id': '52771', 'meal': 'Spicy Arrabiata Penne', 'category': 'Vegetarian', 'area': 'Italian'}],
            self.temp.search_meal_by_name('Arrabiata'))

    def test_search_meal_by_name_2(self):
        self.assertEqual([{'area': 'Croatian',
                           'category': 'Side',
                           'id': '53060',
                           'meal': 'Burek'}],
                         self.temp.search_meal_by_name('Burek'))

    def test_search_meal_by_name_many(self):
        self.assertEqual([{'area': 'Croatian',
                           'category': 'Side',
                           'id': '53060',
                           'meal': 'Burek'},
                          {'area': 'Greek',
                           'category': 'Lamb',
                           'id': '53010',
                           'meal': 'Lamb Tzatziki Burgers'}],
                         self.temp.search_meal_by_name('Bur'))

    def test_search_meal_by_name_wrong_name(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, 'random')

    def test_search_meal_by_name_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, 'abc')

    def test_search_meal_by_name_array(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, [])

    def test_search_meal_by_name_object(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, {})

    def test_search_meal_by_name_none(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, None)

    def test_search_meal_by_name_true(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, True)

    def test_search_meal_by_name_False(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, False)

    def test_search_meal_by_name_int(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, 23)

    def test_search_meal_by_name_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, 2.1233)

    def test_search_meal_by_name_negative_int(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, -21)

    def test_search_meal_by_name_negative_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name, -2.451)

    def test_search_meal_by_name_with_all_details(self):
        self.assertEqual([{'id': '52771', 'meal': 'Spicy Arrabiata Penne', 'category': 'Vegetarian', 'area': 'Italian',
                           'instructions': 'Bring a large pot of water to a boil. Add kosher salt to the boiling '
                                           'water, then add the pasta. Cook according to the package instructions, '
                                           'about 9 minutes.\r\nIn a large skillet over medium-high heat, '
                                           'add the olive oil and heat until the oil starts to shimmer. Add the '
                                           'garlic and cook, stirring, until fragrant, 1 to 2 minutes. Add the '
                                           'chopped tomatoes, red chile flakes, Italian seasoning and salt and pepper '
                                           'to taste. Bring to a boil and cook for 5 minutes. Remove from the heat '
                                           'and add the chopped basil.\r\nDrain the pasta and add it to the sauce. '
                                           'Garnish with Parmigiano-Reggiano flakes and more basil and serve warm.',
                           'photoLink': 'https://www.themealdb.com/images/media/meals/ustsqw1468250014.jpg',
                           'youtubeLink': 'https://www.youtube.com/watch?v=1IszT_guI08',
                           'ingredients': ['penne rigate 1 pound', 'olive oil 1/4 cup', 'garlic 3 cloves',
                                           'chopped tomatoes 1 tin ', 'red chile flakes 1/2 teaspoon',
                                           'italian seasoning 1/2 teaspoon', 'basil 6 leaves',
                                           'Parmigiano-Reggiano spinkling'], 'sourceLink': None,
                           'imageSourceLink': None, 'creativeCommonsConfirmed': None, 'dateModified': None}]
                         ,
                         self.temp.search_meal_by_name_with_all_details('Arrabiata'))

    def test_search_meal_by_name_with_all_details_2(self):
        self.assertEqual([{'area': 'Croatian',
                           'category': 'Side',
                           'creativeCommonsConfirmed': None,
                           'dateModified': None,
                           'id': '53060',
                           'imageSourceLink': None,
                           'ingredients': ['Filo Pastry 1 Packet',
                                           'Minced Beef 150g',
                                           'Onion 150g',
                                           'Oil 40g',
                                           'Salt Dash',
                                           'Pepper Dash'],
                           'instructions': 'Fry the finely chopped onions and minced meat in oil. Add '
                                           'the salt and pepper. Grease a round baking tray and put a '
                                           'layer of pastry in it. Cover with a thin layer of filling '
                                           'and cover this with another layer of filo pastry which must '
                                           'be well coated in oil. Put another layer of filling and '
                                           'cover with pastry. When you have five or six layers, cover '
                                           'with filo pastry, bake at 200ºC/392ºF for half an hour and '
                                           'cut in quarters and serve.',
                           'meal': 'Burek',
                           'photoLink': 'https://www.themealdb.com/images/media/meals/tkxquw1628771028.jpg',
                           'sourceLink': 'https://www.visit-croatia.co.uk/croatian-cuisine/croatian-recipes/',
                           'youtubeLink': 'https://www.youtube.com/watch?v=YsJXZwE5pdY'}],
                         self.temp.search_meal_by_name_with_all_details('Burek'))

    def test_search_meal_by_name_with_all_details_many(self):
        self.assertEqual([{'area': 'Croatian',
                           'category': 'Side',
                           'creativeCommonsConfirmed': None,
                           'dateModified': None,
                           'id': '53060',
                           'imageSourceLink': None,
                           'ingredients': ['Filo Pastry 1 Packet',
                                           'Minced Beef 150g',
                                           'Onion 150g',
                                           'Oil 40g',
                                           'Salt Dash',
                                           'Pepper Dash'],
                           'instructions': 'Fry the finely chopped onions and minced meat in oil. Add '
                                           'the salt and pepper. Grease a round baking tray and put a '
                                           'layer of pastry in it. Cover with a thin layer of filling '
                                           'and cover this with another layer of filo pastry which must '
                                           'be well coated in oil. Put another layer of filling and '
                                           'cover with pastry. When you have five or six layers, cover '
                                           'with filo pastry, bake at 200ºC/392ºF for half an hour and '
                                           'cut in quarters and serve.',
                           'meal': 'Burek',
                           'photoLink': 'https://www.themealdb.com/images/media/meals/tkxquw1628771028.jpg',
                           'sourceLink': 'https://www.visit-croatia.co.uk/croatian-cuisine/croatian-recipes/',
                           'youtubeLink': 'https://www.youtube.com/watch?v=YsJXZwE5pdY'},
                          {'area': 'Greek',
                           'category': 'Lamb',
                           'creativeCommonsConfirmed': None,
                           'dateModified': None,
                           'id': '53010',
                           'imageSourceLink': None,
                           'ingredients': ['Bulgur Wheat 25g',
                                           'Lamb Mince 500g',
                                           'Cumin 1 tsp ',
                                           'Coriander 1 tsp ',
                                           'Paprika 1 tsp ',
                                           'Garlic 1 clove finely chopped',
                                           'Olive Oil For frying',
                                           'Bun 4',
                                           'Cucumber Grated',
                                           'Greek Yogurt 200g',
                                           'Mint 2 tbs'],
                           'instructions': 'Tip the bulghar into a pan, cover with water and boil for '
                                           '10 mins. Drain really well in a sieve, pressing out any '
                                           'excess water.\r\n'
                                           '\r\n'
                                           'To make the tzatziki, squeeze and discard the juice from '
                                           'the cucumber, then mix into the yogurt with the chopped '
                                           'mint and a little salt.\r\n'
                                           '\r\n'
                                           'Work the bulghar into the lamb with the spices, garlic (if '
                                           'using) and seasoning, then shape into 4 burgers. Brush with '
                                           'a little oil and fry or barbecue for about 5 mins each side '
                                           'until cooked all the way through. Serve in the buns '
                                           '(toasted if you like) with the tzatziki, tomatoes, onion '
                                           'and a few mint leaves.',
                           'meal': 'Lamb Tzatziki Burgers',
                           'photoLink': 'https://www.themealdb.com/images/media/meals/k420tj1585565244.jpg',
                           'sourceLink': 'https://www.bbcgoodfood.com/recipes/lamb-burgers-tzatziki',
                           'youtubeLink': 'https://www.youtube.com/watch?v=s7_TF4ZHjPc'}],
                         self.temp.search_meal_by_name_with_all_details('Bur'))

    def test_search_meal_by_name_with_all_details_wrong_name(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, 'random')

    def test_search_meal_by_name_with_all_details_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, 'abc')

    def test_search_meal_by_name_with_all_details_array(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, [])

    def test_search_meal_by_name_with_all_details_object(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, {})

    def test_search_meal_by_name_with_all_details_none(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, None)

    def test_search_meal_by_name_with_all_details_true(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, True)

    def test_search_meal_by_name_with_all_details_False(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, False)

    def test_search_meal_by_name_with_all_details_int(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, 23)

    def test_search_meal_by_name_with_all_details_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, 2.1233)

    def test_search_meal_by_name_with_all_details_negative_int(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, -21)

    def test_search_meal_by_name_with_all_details_negative_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_name_with_all_details, -2.451)

    def test_search_meal_by_id(self):
        self.assertEqual(
            {'id': '52772', 'meal': 'Teriyaki Chicken Casserole', 'category': 'Chicken', 'area': 'Japanese'},
            self.temp.search_meal_by_id(52772))

    def test_search_meal_by_id_2(self):
        self.assertEqual(
            {'area': 'Croatian',
             'category': 'Beef',
             'id': '53057',
             'meal': 'Traditional Croatian Goulash'},
            self.temp.search_meal_by_id(53057))

    def test_test_search_meal_by_id_wrong_id(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, 52778)

    def test_search_meal_by_id_array(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, [])

    def test_search_meal_by_id_object(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, {})

    def test_search_meal_by_id_none(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, None)

    def test_search_meal_by_id_true(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, True)

    def test_search_meal_by_id_False(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, False)

    def test_search_meal_by_id_string(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, 'abc')

    def test_search_meal_by_id_string_number(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, '23784')

    def test_search_meal_by_id_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, 2.1233)

    def test_search_meal_by_id_negative_int(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, -21)

    def test_search_meal_by_id_negative_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id, -2.451)

    def test_search_meal_by_id_with_all_details(self):
        self.assertEqual(
            {'id': '52772', 'meal': 'Teriyaki Chicken Casserole', 'category': 'Chicken', 'area': 'Japanese',
             'instructions': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine '
                             'soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. '
                             'Bring to a boil over medium heat. Remove lid and cook for one minute once '
                             'boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a '
                             'separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir '
                             'to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the '
                             'chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. '
                             'Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and '
                             'shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables '
                             'according to package directions.\r\nAdd the cooked vegetables and rice to the casserole '
                             'dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over '
                             'the top when serving. Gently toss everything together in the casserole dish until '
                             'combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes '
                             'before serving. Drizzle each serving with remaining sauce. Enjoy!',
             'photoLink': 'https://www.themealdb.com/images/media/meals/wvpsxx1468256321.jpg',
             'youtubeLink': 'https://www.youtube.com/watch?v=4aZr5hZXP_s',
             'ingredients': ['soy sauce 3/4 cup', 'water 1/2 cup', 'brown sugar 1/4 cup', 'ground ginger 1/2 teaspoon',
                             'minced garlic 1/2 teaspoon', 'cornstarch 4 Tablespoons', 'chicken breasts 2',
                             'stir-fry vegetables 1 (12 oz.)', 'brown rice 3 cups'], 'sourceLink': None,
             'imageSourceLink': None, 'creativeCommonsConfirmed': None, 'dateModified': None}
            ,
            self.temp.search_meal_by_id_with_all_details(52772))

    def test_search_meal_by_id_with_all_details_2(self):
        self.assertEqual({'id': '53057', 'meal': 'Traditional Croatian Goulash', 'category': 'Beef', 'area': 'Croatian',
                          'instructions': 'Clean the meat from the veins if there are some and cut it into smaller '
                                          'pieces, 3 × 3 cm. Marinate the meat in the mustard and spices and let it '
                                          'sit in the refrigerator for one hour\r\nHeat one tablespoon of pork fat or '
                                          'vegetable oil in a pot and fry the meat on all sides until it gets '
                                          'browned. Once the meat is cooked, transfer it to a plate and add another '
                                          'tablespoon of fat to the pot\r\nCut the onions very fine, peel the carrots '
                                          'and shred it using a grater. Cook the onions and carrots over low heat for '
                                          '15 minutes. You can salt the vegetables a little to make them soften '
                                          'faster\r\nOnce the vegetables have browned and become slightly mushy, '
                                          'add the meat and bay leaves and garlic. Pour over with wine and simmer for '
                                          '10-15 minutes to allow the alcohol to evaporate. Now is the right time to '
                                          'add 2/3 the amount of liquid\r\nCover the pot and cook over low heat for '
                                          'an hour, stirring occasionally. After the first hour, pour over the rest '
                                          'of the water or stock and cook for another 30-45 minutes\r\nAllow the stew '
                                          'to cool slightly and serve it with a sprinkle of chopped parsley and few '
                                          'slices of fresh hot pepper if you like to spice it up a bit\r\nSlice '
                                          '\u200b\u200bsome fresh bread, season the salad and simply enjoying these '
                                          'wonderful flavors',
                          'photoLink': 'https://www.themealdb.com/images/media/meals/n1hcou1628770088.jpg',
                          'youtubeLink': 'https://www.youtube.com/watch?v=ipEz5u2T7KM',
                          'ingredients': ['Beef 500g', 'Onions 2 chopped', 'Carrots 2 chopped', 'Garlic 2 cloves',
                                          'Bay Leaf 2', 'Red Wine 200ml', 'Water 2 Litres', 'Mustard 3 tbs',
                                          'Salt 1tbsp', 'Pepper 1/2 tsp', 'Paprika 1/2 tsp', 'Vegetable Oil 2 tbs'],
                          'sourceLink': 'https://www.chasingthedonkey.com/croatian-recipes-traditional-croatian'
                                        '-goulash/',
                          'imageSourceLink': None, 'creativeCommonsConfirmed': None, 'dateModified': None}
                         ,
                         self.temp.search_meal_by_id_with_all_details(53057))

    def test_test_search_meal_by_id_with_all_details_wrong_id(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, 52778)

    def test_search_meal_by_id_with_all_details_array(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, [])

    def test_search_meal_by_id_with_all_details_object(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, {})

    def test_search_meal_by_id_with_all_details_none(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, None)

    def test_search_meal_by_id_with_all_details_true(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, True)

    def test_search_meal_by_id_with_all_details_False(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, False)

    def test_search_meal_by_id_with_all_details_string(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, 'abc')

    def test_search_meal_by_id_with_all_details_string_number(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, '23784')

    def test_search_meal_by_id_with_all_details_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, 2.1233)

    def test_search_meal_by_id_with_all_details_negative_int(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, -21)

    def test_search_meal_by_id_with_all_details_negative_float(self):
        self.assertRaises(TypeError, self.temp.search_meal_by_id_with_all_details, -2.451)
