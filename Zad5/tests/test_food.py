import unittest
from src.food import food


class test_food(unittest.TestCase):

    def setUp(self):
        self.temp = food()

    def test_search_meal_by_name(self):
        self.assertEqual({'id': '52771', 'meal': 'Spicy Arrabiata Penne', 'category': 'Vegetarian', 'area': 'Italian',
                          'instructions': 'Bring a large pot of water to a boil. Add kosher salt to the boiling '
                                          'water, then add the pasta. Cook according to the package instructions, '
                                          'about 9 minutes.\r\nIn a large skillet over medium-high heat, '
                                          'add the olive oil and heat until the oil starts to shimmer. Add the garlic '
                                          'and cook, stirring, until fragrant, 1 to 2 minutes. Add the chopped '
                                          'tomatoes, red chile flakes, Italian seasoning and salt and pepper to '
                                          'taste. Bring to a boil and cook for 5 minutes. Remove from the heat and '
                                          'add the chopped basil.\r\nDrain the pasta and add it to the sauce. Garnish '
                                          'with Parmigiano-Reggiano flakes and more basil and serve warm.'},
                         self.temp.search_meal_by_name('Arrabiata'))

    def test_search_meal_by_name_2(self):
        self.assertEqual({'area': 'Croatian',
                          'category': 'Side',
                          'id': '53060',
                          'instructions': 'Fry the finely chopped onions and minced meat in oil. Add '
                                          'the salt and pepper. Grease a round baking tray and put a '
                                          'layer of pastry in it. Cover with a thin layer of filling '
                                          'and cover this with another layer of filo pastry which must '
                                          'be well coated in oil. Put another layer of filling and '
                                          'cover with pastry. When you have five or six layers, cover '
                                          'with filo pastry, bake at 200ºC/392ºF for half an hour and '
                                          'cut in quarters and serve.',
                          'meal': 'Burek'},
                         self.temp.search_meal_by_name('Burek'))

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

    def test_list_meals_by_first_letter(self):
        self.assertEqual(
            [{'id': '52768', 'meal': 'Apple Frangipan Tart'}, {'id': '52893', 'meal': 'Apple & Blackberry Crumble'},
             {'id': '53049', 'meal': 'Apam balik'}, {'id': '53050', 'meal': 'Ayam Percik'}],
            self.temp.list_meals_by_first_letter('a'))

    def test_list_meals_by_first_letter_2(self):
        self.assertEqual(
            [{'id': '52773', 'meal': 'Honey Teriyaki Salmon'}, {'id': '52787', 'meal': 'Hot Chocolate Fudge'},
             {'id': '52954', 'meal': 'Hot and Sour Soup'}, {'id': '52967', 'meal': 'Home-made Mandazi'},
             {'id': '52993', 'meal': 'Honey Balsamic Chicken with Crispy Broccoli & Potatoes'},
             {'id': '53007', 'meal': 'Honey Yogurt Cheesecake'}, {'id': '53035', 'meal': 'Ham hock colcannon'}],
            self.temp.list_meals_by_first_letter('h'))

    def test_list_meals_by_first_letter_string(self):
        self.assertRaises(ValueError, self.temp.list_meals_by_first_letter, 'abc')

    def test_list_meals_by_first_letter_long_string(self):
        self.assertRaises(ValueError, self.temp.list_meals_by_first_letter, 'abcasssssssczxcasdfasdSASD')

    def test_list_meals_by_first_letter_number_string(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, '2')

    def test_list_meals_by_first_letter_empty_string(self):
        self.assertRaises(ValueError, self.temp.list_meals_by_first_letter, '')

    def test_list_meals_by_first_letter_array(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, [])

    def test_list_meals_by_first_letter_object(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, {})

    def test_list_meals_by_first_letter_none(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, None)

    def test_list_meals_by_first_letter_true(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, True)

    def test_list_meals_by_first_letter_False(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, False)

    def test_list_meals_by_first_letter_int(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, 23)

    def test_list_meals_by_first_letter_float(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, 2.1233)

    def test_list_meals_by_first_letter_negative_int(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, -21)

    def test_list_meals_by_first_letter_negative_float(self):
        self.assertRaises(TypeError, self.temp.list_meals_by_first_letter, -2.451)

    def test_search_meal_by_id(self):
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
                             'before serving. Drizzle each serving with remaining sauce. Enjoy!'},
            self.temp.search_meal_by_id(52772))

    def test_search_meal_by_id_2(self):
        self.assertEqual(
            {'area': 'Croatian',
             'category': 'Beef',
             'id': '53057',
             'instructions': 'Clean the meat from the veins if there are some and cut it '
                             'into smaller pieces, 3 × 3 cm. Marinate the meat in the '
                             'mustard and spices and let it sit in the refrigerator for '
                             'one hour\r\n'
                             'Heat one tablespoon of pork fat or vegetable oil in a pot '
                             'and fry the meat on all sides until it gets browned. Once '
                             'the meat is cooked, transfer it to a plate and add another '
                             'tablespoon of fat to the pot\r\n'
                             'Cut the onions very fine, peel the carrots and shred it '
                             'using a grater. Cook the onions and carrots over low heat '
                             'for 15 minutes. You can salt the vegetables a little to make '
                             'them soften faster\r\n'
                             'Once the vegetables have browned and become slightly mushy, '
                             'add the meat and bay leaves and garlic. Pour over with wine '
                             'and simmer for 10-15 minutes to allow the alcohol to '
                             'evaporate. Now is the right time to add 2/3 the amount of '
                             'liquid\r\n'
                             'Cover the pot and cook over low heat for an hour, stirring '
                             'occasionally. After the first hour, pour over the rest of '
                             'the water or stock and cook for another 30-45 minutes\r\n'
                             'Allow the stew to cool slightly and serve it with a sprinkle '
                             'of chopped parsley and few slices of fresh hot pepper if you '
                             'like to spice it up a bit\r\n'
                             'Slice \u200b\u200bsome fresh bread, season the salad and '
                             'simply enjoying these wonderful flavors',
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

    def test_list_meal_categories(self):
        self.assertEqual(
            [{'id': '1', 'category': 'Beef'}, {'id': '2', 'category': 'Chicken'}, {'id': '3', 'category': 'Dessert'},
             {'id': '4', 'category': 'Lamb'}, {'id': '5', 'category': 'Miscellaneous'},
             {'id': '6', 'category': 'Pasta'}, {'id': '7', 'category': 'Pork'}, {'id': '8', 'category': 'Seafood'},
             {'id': '9', 'category': 'Side'}, {'id': '10', 'category': 'Starter'}, {'id': '11', 'category': 'Vegan'},
             {'id': '12', 'category': 'Vegetarian'}, {'id': '13', 'category': 'Breakfast'},
             {'id': '14', 'category': 'Goat'}], self.temp.list_meal_categories())

    def test_list_all_categories(self):
        self.assertEqual(
            ['Beef', 'Breakfast', 'Chicken', 'Dessert', 'Goat', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood',
             'Side', 'Starter', 'Vegan', 'Vegetarian']
            , self.temp.list_all_categories())

    def test_list_all_area(self):
        self.assertEqual(
            ['American', 'British', 'Canadian', 'Chinese', 'Croatian', 'Dutch', 'Egyptian', 'French', 'Greek', 'Indian',
             'Irish', 'Italian', 'Jamaican', 'Japanese', 'Kenyan', 'Malaysian', 'Mexican', 'Moroccan', 'Polish',
             'Portuguese', 'Russian', 'Spanish', 'Thai', 'Tunisian', 'Turkish', 'Unknown', 'Vietnamese']
            , self.temp.list_all_area())

    def test_list_all_ingredients(self):
        self.assertEqual(
            ['Chicken', 'Salmon', 'Beef', 'Pork', 'Avocado', 'Apple Cider Vinegar', 'Asparagus', 'Aubergine',
             'Baby Plum Tomatoes', 'Bacon', 'Baking Powder', 'Balsamic Vinegar', 'Basil', 'Basil Leaves',
             'Basmati Rice', 'Bay Leaf', 'Bay Leaves', 'Beef Brisket', 'Beef Fillet', 'Beef Gravy', 'Beef Stock',
             'Bicarbonate Of Soda', 'Biryani Masala', 'Black Pepper', 'Black Treacle', 'Borlotti Beans', 'Bowtie Pasta',
             'Bramley Apples', 'Brandy', 'Bread', 'Breadcrumbs', 'Broccoli', 'Brown Lentils', 'Brown Rice',
             'Brown Sugar', 'Butter', 'Cacao', 'Cajun', 'Canned Tomatoes', 'Cannellini Beans', 'Cardamom', 'Carrots',
             'Cashew Nuts', 'Cashews', 'Caster Sugar', 'Cayenne Pepper', 'Celeriac', 'Celery', 'Celery Salt',
             'Challots', 'Charlotte Potatoes', 'Cheddar Cheese', 'Cheese', 'Cheese Curds', 'Cherry Tomatoes',
             'Chestnut Mushroom', 'Chicken Breast', 'Chicken Breasts', 'Chicken Legs', 'Chicken Stock',
             'Chicken Thighs', 'Chickpeas', 'Chili Powder', 'Chilled Butter', 'Chilli', 'Chilli Powder',
             'Chinese Broccoli', 'Chocolate Chips', 'Chopped Onion', 'Chopped Parsley', 'Chopped Tomatoes', 'Chorizo',
             'Christmas Pudding', 'Cilantro', 'Cinnamon', 'Cinnamon Stick', 'Cloves', 'Coco Sugar', 'Cocoa',
             'Coconut Cream', 'Coconut Milk', 'Colby Jack Cheese', 'Cold Water', 'Condensed Milk', 'Coriander',
             'Coriander Leaves', 'Coriander Seeds', 'Corn Tortillas', 'Cornstarch', 'Cream', 'Creme Fraiche',
             'Cubed Feta Cheese', 'Cucumber', 'Cumin', 'Cumin Seeds', 'Curry Powder', 'Dark Brown Sugar',
             'Dark Soft Brown Sugar', 'Dark Soy Sauce', 'Demerara Sugar', 'Diced Tomatoes', 'Digestive Biscuits',
             'Dill', 'Doner Meat', 'Double Cream', 'Dried Oregano', 'Dry White Wine', 'Egg Plants', 'Egg Rolls',
             'Egg White', 'Egg Yolks', 'Eggs', 'Enchilada Sauce', 'English Mustard', 'Extra Virgin Olive Oil',
             'Fajita Seasoning', 'Farfalle', 'Fennel Bulb', 'Fennel Seeds', 'Fenugreek', 'Feta', 'Fish Sauce',
             'Flaked Almonds', 'Flax Eggs', 'Flour', 'Flour Tortilla', 'Floury Potatoes', 'Free-range Egg, Beaten',
             'Free-range Eggs, Beaten', 'French Lentils', 'Fresh Basil', 'Fresh Thyme', 'Freshly Chopped Parsley',
             'Fries', 'Full Fat Yogurt', 'Garam Masala', 'Garlic', 'Garlic Clove', 'Garlic Powder', 'Garlic Sauce',
             'Ghee', 'Ginger', 'Ginger Cordial', 'Ginger Garlic Paste', 'Ginger Paste', 'Golden Syrup', 'Gouda Cheese',
             'Granulated Sugar', 'Grape Tomatoes', 'Greek Yogurt', 'Green Beans', 'Green Chilli', 'Green Olives',
             'Green Red Lentils', 'Green Salsa', 'Ground Almonds', 'Ground Cumin', 'Ground Ginger', 'Gruyère',
             'Hard Taco Shells', 'Harissa Spice', 'Heavy Cream', 'Honey', 'Horseradish', 'Hot Beef Stock', 'Hotsauce',
             'Ice Cream', 'Italian Fennel Sausages', 'Italian Seasoning', 'Jalapeno', 'Jasmine Rice',
             'Jerusalem Artichokes', 'Kale', 'Khus Khus', 'King Prawns', 'Kosher Salt', 'Lamb', 'Lamb Loin Chops',
             'Lamb Mince', 'Lasagne Sheets', 'Lean Minced Beef', 'Leek', 'Lemon', 'Lemon Juice', 'Lemon Zest', 'Lemons',
             'Lettuce', 'Lime', 'Little Gem Lettuce', 'Macaroni', 'Mackerel', 'Madras Paste', 'Marjoram',
             'Massaman Curry Paste', 'Medjool Dates', 'Meringue Nests', 'Milk', 'Minced Garlic',
             'Miniature Marshmallows', 'Mint', 'Monterey Jack Cheese', 'Mozzarella Balls', 'Muscovado Sugar',
             'Mushrooms', 'Mustard', 'Mustard Powder', 'Mustard Seeds', 'Nutmeg', 'Oil', 'Olive Oil', 'Onion Salt',
             'Onions', 'Orange', 'Orange Zest', 'Oregano', 'Oyster Sauce', 'Paprika', 'Parma Ham', 'Parmesan',
             'Parmesan Cheese', 'Parmigiano-reggiano', 'Parsley', 'Peanut Butter', 'Peanut Oil', 'Peanuts', 'Peas',
             'Pecorino', 'Penne Rigate', 'Pepper', 'Pine Nuts', 'Pitted Black Olives', 'Plain Chocolate', 'Plain Flour',
             'Plum Tomatoes', 'Potato Starch', 'Potatoes', 'Prawns', 'Puff Pastry', 'Raspberry Jam', 'Raw King Prawns',
             'Red Chile Flakes', 'Red Chilli', 'Red Chilli Powder', 'Red Onions', 'Red Pepper', 'Red Pepper Flakes',
             'Red Wine', 'Refried Beans', 'Rice', 'Rice Noodles', 'Rice Stick Noodles', 'Rice Vermicelli', 'Rigatoni',
             'Rocket', 'Rolled Oats', 'Saffron', 'Sage', 'Sake', 'Salsa', 'Salt', 'Salted Butter', 'Sausages',
             'Sea Salt', 'Self-raising Flour', 'Semi-skimmed Milk', 'Sesame Seed', 'Shallots',
             'Shredded Mexican Cheese', 'Shredded Monterey Jack Cheese', 'Small Potatoes', 'Smoked Paprika',
             'Smoky Paprika', 'Sour Cream', 'Soy Sauce', 'Soya Milk', 'Spaghetti', 'Spinach', 'Spring Onions', 'Squash',
             'Stir-fry Vegetables', 'Strawberries', 'Sugar', 'Sultanas', 'Sunflower Oil', 'Tamarind Ball',
             'Tamarind Paste', 'Thai Fish Sauce', 'Thai Green Curry Paste', 'Thai Red Curry Paste', 'Thyme',
             'Tomato Ketchup', 'Tomato Puree', 'Tomatoes', 'Toor Dal', 'Tuna', 'Turmeric', 'Turmeric Powder', 'Turnips',
             'Vanilla', 'Vanilla Extract', 'Veal', 'Vegan Butter', 'Vegetable Oil', 'Vegetable Stock',
             'Vegetable Stock Cube', 'Vinaigrette Dressing', 'Vine Leaves', 'Vinegar', 'Water', 'White Chocolate Chips',
             'White Fish', 'White Fish Fillets', 'White Vinegar', 'White Wine', 'Whole Milk', 'Whole Wheat',
             'Wholegrain Bread', 'Worcestershire Sauce', 'Yogurt', 'Zucchini', 'Pretzels', 'Cream Cheese',
             'Icing Sugar', 'Toffee Popcorn', 'Caramel', 'Caramel Sauce', 'Tagliatelle', 'Fettuccine', 'Clotted Cream',
             'Corn Flour', 'Mussels', 'Fideo', 'Monkfish', 'Vermicelli Pasta', 'Baby Squid', 'Squid', 'Fish Stock',
             'Pilchards', 'Black Olives', 'Onion', 'Tomato', 'Duck', 'Duck Legs', 'Chicken Stock Cube',
             'Pappardelle Pasta', 'Paccheri Pasta', 'Linguine Pasta', 'Sugar Snap Peas', 'Crusty Bread',
             'Fromage Frais', 'Clams', 'Passata', 'Rapeseed Oil', 'Stilton Cheese', 'Lamb Leg', 'Lamb Shoulder',
             'Apricot', 'Butternut Squash', 'Couscous', 'Minced Beef', 'Turkey Mince', 'Barbeque Sauce', 'Sweetcorn',
             'Goose Fat', 'Duck Fat', 'Fennel', 'Red Wine Vinegar', 'Haricot Beans', 'Rosemary', 'Butter Beans',
             'Pinto Beans', 'Tomato Sauce', 'Mascarpone', 'Mozzarella', 'Ricotta', 'Dried Apricots', 'Capers', 'Banana',
             'Raspberries', 'Blueberries', 'Walnuts', 'Pecan Nuts', 'Maple Syrup', 'Light Brown Soft Sugar',
             'Dark Brown Soft Sugar', 'Dark Chocolate Chips', 'Milk Chocolate', 'Dark Chocolate', 'Pumpkin',
             'Shortcrust Pastry', 'Peanut Cookies', 'Gelatine Leafs', 'Peanut Brittle', 'Peaches', 'Yellow Pepper',
             'Green Pepper', 'Courgettes', 'Tinned Tomatos', 'Chestnuts', 'Wild Mushrooms', 'Truffle Oil', 'Paneer',
             'Naan Bread', 'Lentils', 'Roasted Vegetables', 'Kidney Beans', 'Mixed Grain', 'Tahini', 'Tortillas',
             'Udon Noodles', 'Cabbage', 'Shiitake Mushrooms', 'Mirin', 'Sesame Seed Oil', 'Baguette', 'Vine Tomatoes',
             'Suet', 'Swede', 'Ham', 'Oysters', 'Stout', 'Lard', 'Lamb Kidney', 'Beef Kidney', 'Haddock',
             'Smoked Haddock', 'Brussels Sprouts', 'Raisins', 'Currants', 'Custard', 'Mixed Peel', 'Redcurrants',
             'Blackberries', 'Hazlenuts', 'Braeburn Apples', 'Red Food Colouring', 'Pink Food Colouring',
             'Blue Food Colouring', 'Yellow Food Colouring', 'Apricot Jam', 'Marzipan', 'Almonds', 'Black Pudding',
             'Baked Beans', 'White Flour', 'Yeast', 'Fruit Mix', 'Dried Fruit', 'Cherry', 'Glace Cherry', 'Treacle',
             'Oatmeal', 'Oats', 'Egg', 'Beef Shin', 'Bouquet Garni', 'Single Cream', 'Red Wine Jelly', 'Apples',
             'Goats Cheese', 'Prosciutto', 'Unsalted Butter', 'Brie', 'Tarragon Leaves', 'Chives', 'Pears',
             'White Chocolate', 'Star Anise', 'Tiger Prawns', 'Custard Powder', 'Desiccated Coconut', 'Frozen Peas',
             'Minced Pork', 'Creamed Corn', 'Sun-Dried Tomatoes', 'Dijon Mustard', 'Tabasco Sauce', 'Canola Oil', 'Cod',
             'Salt Cod', 'Ackee', 'Jerk', 'Ground Beef', 'Baby Aubergine', 'Paella Rice', 'Scotch Bonnet', 'Oxtail',
             'Broad Beans', 'Red Snapper', 'Malt Vinegar', 'Rice Vinegar', 'Water Chestnut', 'Tofu', 'Doubanjiang',
             'Fermented Black Beans', 'Scallions', 'Sichuan Pepper', 'Wonton Skin', 'Starch', 'Rice wine',
             'Cooking wine', 'Duck Sauce', 'Gochujang', 'Bean Sprouts', 'Noodles', 'Wood Ear Mushrooms', 'Dark Rum',
             'Light Rum', 'Rum', 'English Muffins', 'Muffins', 'White Wine Vinegar', 'Smoked Salmon', 'Mars Bar',
             'Rice Krispies', 'Ancho Chillies', 'Almond Milk', 'Allspice', 'Almond Extract', 'Tripe', 'Goat Meat',
             'Black Beans', 'Anchovy Fillet', 'Ras el hanout', 'Filo Pastry', 'Orange Blossom Water', 'Candied Peel',
             'Grand Marnier', 'Sherry', 'Rose water', 'Mixed Spice', 'Mincemeat', 'Sweet Potatoes', 'Bread Rolls',
             'Bun', 'Potatoe Buns', 'Ground Pork', 'Pork Chops', 'Yukon Gold Potatoes', 'Yellow Onion',
             'Beef Stock Concentrate', 'Chicken Stock Concentrate', 'Persian Cucumber', 'Mayonnaise', 'Sriracha',
             'Rhubarb', 'Pita Bread', 'Bulgur Wheat', 'Quinoa', 'Dill Pickles', 'Sesame Seed Burger Buns', 'Buns',
             'Iceberg Lettuce', 'Gherkin Relish', 'Cheese Slices', 'Shortening', 'Warm Water', 'Boiling Water',
             'Pickle Juice', 'Powdered Sugar', 'Kielbasa', 'Polish Sausage', 'Sauerkraut', 'Caraway Seed', 'Herring',
             'Jam', 'Mulukhiyah', 'Sushi Rice', 'Figs', 'Cider', 'Beetroot', 'Sardines', 'Ciabatta', 'Buckwheat']
            , self.temp.list_all_ingredients())

    def test_filter_by_main_ingredient(self):
        self.assertEqual([{'id': '53016', 'meal': 'Chick-Fil-A Sandwich'}, {'id': '52850', 'meal': 'Chicken Couscous'},
                          {'id': '52818', 'meal': 'Chicken Fajita Mac and Cheese'},
                          {'id': '52875', 'meal': 'Chicken Ham and Leek Pie'},
                          {'id': '53011', 'meal': 'Chicken Quinoa Greek Salad'},
                          {'id': '52951', 'meal': "General Tso's Chicken"},
                          {'id': '52993', 'meal': 'Honey Balsamic Chicken with Crispy Broccoli & Potatoes'},
                          {'id': '52820', 'meal': 'Katsu Chicken curry'}, {'id': '52933', 'meal': 'Rappie Pie'}]
                         , self.temp.filter_by_main_ingredient('chicken_breast'))

    def test_filter_by_main_ingredient_2(self):
        self.assertEqual([{'id': '52974', 'meal': 'Keleya Zaara'},
                          {'id': '52884', 'meal': 'Lancashire hotpot'},
                          {'id': '53008', 'meal': 'Stuffed Lamb Tomatoes'}]
                         , self.temp.filter_by_main_ingredient('Lamb'))

    def test_filter_by_main_ingredient_wrong_name(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, 'random')

    def test_filter_by_main_ingredient_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, 'sand')

    def test_filter_by_main_ingredient_array(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, [])

    def test_filter_by_main_ingredient_object(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, {})

    def test_filter_by_main_ingredient_none(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, None)

    def test_filter_by_main_ingredient_true(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, True)

    def test_filter_by_main_ingredient_False(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, False)

    def test_filter_by_main_ingredient_int(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, 23)

    def test_filter_by_main_ingredient_float(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, 2.1233)

    def test_filter_by_main_ingredient_negative_int(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, -21)

    def test_filter_by_main_ingredient_negative_float(self):
        self.assertRaises(TypeError, self.temp.filter_by_main_ingredient, -2.451)

    def test_filter_by_category(self):
        self.assertEqual([{'id': '52959', 'meal': 'Baked salmon with fennel & tomatoes'},
                          {'id': '52819', 'meal': 'Cajun spiced fish tacos'}, {'id': '52944', 'meal': 'Escovitch Fish'},
                          {'id': '53043', 'meal': 'Fish fofos'}, {'id': '52802', 'meal': 'Fish pie'},
                          {'id': '52918', 'meal': 'Fish Stew with Rouille'},
                          {'id': '52764', 'meal': 'Garides Saganaki'},
                          {'id': '53041', 'meal': 'Grilled Portuguese sardines'},
                          {'id': '52773', 'meal': 'Honey Teriyaki Salmon'}, {'id': '52887', 'meal': 'Kedgeree'},
                          {'id': '52946', 'meal': 'Kung Po Prawns'},
                          {'id': '52821', 'meal': 'Laksa King Prawn Noodles'},
                          {'id': '52777', 'meal': 'Mediterranean Pasta Salad'},
                          {'id': '53048', 'meal': 'Mee goreng mamak'}, {'id': '53051', 'meal': 'Nasi lemak'},
                          {'id': '53045', 'meal': 'Portuguese fish stew (Caldeirada de peixe)'},
                          {'id': '52809', 'meal': 'Recheado Masala Fish'},
                          {'id': '52960', 'meal': 'Salmon Avocado Salad'},
                          {'id': '52823', 'meal': 'Salmon Prawn Risotto'},
                          {'id': '52936', 'meal': 'Saltfish and Ackee'}, {'id': '52836', 'meal': 'Seafood fideuà'},
                          {'id': '52953', 'meal': 'Shrimp Chow Fun'},
                          {'id': '53023', 'meal': 'Sledz w Oleju (Polish Herrings)'},
                          {'id': '53040', 'meal': 'Spring onion and prawn empanadas'},
                          {'id': '52882', 'meal': 'Three Fish Pie'}, {'id': '52975', 'meal': 'Tuna and Egg Briks'},
                          {'id': '52852', 'meal': 'Tuna Nicoise'}]
                         , self.temp.filter_by_category('Seafood'))

    def test_filter_by_category_2(self):
        self.assertEqual([{'id': '53049', 'meal': 'Apam balik'}, {'id': '52893', 'meal': 'Apple & Blackberry Crumble'},
                          {'id': '52768', 'meal': 'Apple Frangipan Tart'}, {'id': '52767', 'meal': 'Bakewell tart'},
                          {'id': '52855', 'meal': 'Banana Pancakes'}, {'id': '52894', 'meal': 'Battenberg Cake'},
                          {'id': '52928', 'meal': 'BeaverTails'}, {'id': '52891', 'meal': 'Blackberry Fool'},
                          {'id': '52792', 'meal': 'Bread and Butter Pudding'},
                          {'id': '52961', 'meal': 'Budino Di Ricotta'},
                          {'id': '52923', 'meal': 'Canadian Butter Tarts'}, {'id': '52897', 'meal': 'Carrot Cake'},
                          {'id': '52976', 'meal': 'Cashew Ghoriba Biscuits'}, {'id': '52898', 'meal': 'Chelsea Buns'},
                          {'id': '52910', 'meal': 'Chinon Apple Tarts'}, {'id': '52856', 'meal': 'Choc Chip Pecan Pie'},
                          {'id': '52853', 'meal': 'Chocolate Avocado Mousse'},
                          {'id': '52966', 'meal': 'Chocolate Caramel Crispy'},
                          {'id': '52776', 'meal': 'Chocolate Gateau'},
                          {'id': '52860', 'meal': 'Chocolate Raspberry Brownies'},
                          {'id': '52905', 'meal': 'Chocolate Souffle'}, {'id': '52990', 'meal': 'Christmas cake'},
                          {'id': '52788', 'meal': 'Christmas Pudding Flapjack'},
                          {'id': '52989', 'meal': 'Christmas Pudding Trifle'},
                          {'id': '52988', 'meal': 'Classic Christmas pudding'}, {'id': '52899', 'meal': 'Dundee cake'},
                          {'id': '52888', 'meal': 'Eccles Cakes'}, {'id': '52791', 'meal': 'Eton Mess'},
                          {'id': '53007', 'meal': 'Honey Yogurt Cheesecake'},
                          {'id': '52787', 'meal': 'Hot Chocolate Fudge'}, {'id': '52890', 'meal': 'Jam Roly-Poly'},
                          {'id': '52859', 'meal': 'Key Lime Pie'}, {'id': '53015', 'meal': 'Krispy Kreme Donut'},
                          {'id': '52900', 'meal': 'Madeira Cake'}, {'id': '52991', 'meal': 'Mince Pies'},
                          {'id': '52924', 'meal': 'Nanaimo Bars'}, {'id': '52858', 'meal': 'New York cheesecake'},
                          {'id': '52854', 'meal': 'Pancakes'}, {'id': '52902', 'meal': 'Parkin Cake'},
                          {'id': '52862', 'meal': 'Peach & Blueberry Grunt'},
                          {'id': '52861', 'meal': 'Peanut Butter Cheesecake'},
                          {'id': '52958', 'meal': 'Peanut Butter Cookies'}, {'id': '52916', 'meal': 'Pear Tarte Tatin'},
                          {'id': '53022', 'meal': 'Polskie Naleśniki (Polish Pancakes)'},
                          {'id': '53046', 'meal': 'Portuguese custard tarts'},
                          {'id': '52932', 'meal': 'Pouding chomeur'}, {'id': '52857', 'meal': 'Pumpkin Pie'},
                          {'id': '52901', 'meal': 'Rock Cakes'}, {'id': '52786', 'meal': 'Rocky Road Fudge'},
                          {'id': '53024', 'meal': 'Rogaliki (Polish Croissant Cookies)'},
                          {'id': '52833', 'meal': 'Salted Caramel Cheescake'},
                          {'id': '53054', 'meal': 'Seri muka kuih'}, {'id': '52886', 'meal': 'Spotted Dick'},
                          {'id': '52883', 'meal': 'Sticky Toffee Pudding'},
                          {'id': '52793', 'meal': 'Sticky Toffee Pudding Ultimate'},
                          {'id': '53005', 'meal': 'Strawberry Rhubarb Pie'}, {'id': '52931', 'meal': 'Sugar Pie'},
                          {'id': '52889', 'meal': 'Summer Pudding'}, {'id': '52909', 'meal': 'Tarte Tatin'},
                          {'id': '52929', 'meal': 'Timbits'}, {'id': '52892', 'meal': 'Treacle Tart'},
                          {'id': '52970', 'meal': 'Tunisian Orange Cake'},
                          {'id': '53062', 'meal': 'Walnut Roll Gužvara'},
                          {'id': '52917', 'meal': 'White chocolate creme brulee'}]
                         , self.temp.filter_by_category('Dessert'))

    def test_filter_by_category_wrong_name(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, 'random')

    def test_filter_by_category_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, 'water')

    def test_filter_by_category_array(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, [])

    def test_filter_by_category_object(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, {})

    def test_filter_by_category_none(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, None)

    def test_filter_by_category_true(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, True)

    def test_filter_by_category_False(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, False)

    def test_filter_by_category_int(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, 23)

    def test_filter_by_category_float(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, 2.1233)

    def test_filter_by_category_negative_int(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, -21)

    def test_filter_by_category_negative_float(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, -2.451)

    def test_filter_by_area(self):
        self.assertEqual([{'id': '52928', 'meal': 'BeaverTails'}, {'id': '52965', 'meal': 'Breakfast Potatoes'},
                          {'id': '52923', 'meal': 'Canadian Butter Tarts'},
                          {'id': '52927', 'meal': 'Montreal Smoked Meat'}, {'id': '52924', 'meal': 'Nanaimo Bars'},
                          {'id': '52930', 'meal': 'Pate Chinois'}, {'id': '52932', 'meal': 'Pouding chomeur'},
                          {'id': '52804', 'meal': 'Poutine'}, {'id': '52933', 'meal': 'Rappie Pie'},
                          {'id': '52925', 'meal': 'Split Pea Soup'}, {'id': '52931', 'meal': 'Sugar Pie'},
                          {'id': '52929', 'meal': 'Timbits'}, {'id': '52926', 'meal': 'Tourtiere'}],
                         self.temp.filter_by_area('Canadian'))

    def test_filter_by_area_2(self):
        self.assertEqual(
            [{'id': '53018', 'meal': 'Bigos (Hunters Stew)'}, {'id': '53021', 'meal': 'Gołąbki (cabbage roll)'},
             {'id': '53017', 'meal': 'Paszteciki (Polish Pasties)'},
             {'id': '53019', 'meal': 'Pierogi (Polish Dumplings)'},
             {'id': '53022', 'meal': 'Polskie Naleśniki (Polish Pancakes)'},
             {'id': '53024', 'meal': 'Rogaliki (Polish Croissant Cookies)'},
             {'id': '53020', 'meal': 'Rosół (Polish Chicken Soup)'},
             {'id': '53023', 'meal': 'Sledz w Oleju (Polish Herrings)'}],
            self.temp.filter_by_area('Polish'))

    def test_filter_by_area_wrong_name(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, 'USA')

    def test_filter_by_area_wrong_name_2(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, 'random')

    def test_filter_by_area_array(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, [])

    def test_filter_by_area_object(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, {})

    def test_filter_by_area_none(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, None)

    def test_filter_by_area_true(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, True)

    def test_filter_by_area_False(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, False)

    def test_filter_by_area_int(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, 23)

    def test_filter_by_area_float(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, 2.1233)

    def test_filter_by_area_negative_int(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, -21)

    def test_filter_by_area_negative_float(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, -2.451)
