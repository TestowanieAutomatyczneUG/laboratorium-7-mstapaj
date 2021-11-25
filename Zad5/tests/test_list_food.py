import unittest
from src.list_food import list_food


class test_list_food(unittest.TestCase):

    def setUp(self):
        self.temp = list_food()

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

    def test_list_meal_categories_which_begins_with_letter(self):
        self.assertEqual(
            ['Dessert'],
            self.temp.list_meal_categories_which_begins_with_letter('D'))

    def test_list_meal_categories_which_begins_with_letter_2(self):
        self.assertEqual(['Seafood', 'Side', 'Starter'],
                         self.temp.list_meal_categories_which_begins_with_letter('S'))

    def test_list_meal_categories_which_begins_with_letter_array(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, [])

    def test_list_meal_categories_which_begins_with_letter_object(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, {})

    def test_list_meal_categories_which_begins_with_letter_none(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, None)

    def test_list_meal_categories_which_begins_with_letter_true(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, True)

    def test_list_meal_categories_which_begins_with_letter_False(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, False)

    def test_list_meal_categories_which_begins_with_letter_int(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, 23)

    def test_list_meal_categories_which_begins_with_letter_float(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, 2.1233)

    def test_list_meal_categories_which_begins_with_letter_negative_int(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, -21)

    def test_list_meal_categories_which_begins_with_letter_negative_float(self):
        self.assertRaises(TypeError, self.temp.list_meal_categories_which_begins_with_letter, -2.451)

    def test_list_all_categories_which_begins_with_letter(self):
        self.assertEqual(
            ['Pasta', 'Pork'],
            self.temp.list_all_categories_which_begins_with_letter('P'))

    def test_list_all_categories_which_begins_with_letter_2(self):
        self.assertEqual(['Goat'],
                         self.temp.list_all_categories_which_begins_with_letter('G'))

    def test_list_all_categories_which_begins_with_letter_array(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, [])

    def test_list_all_categories_which_begins_with_letter_object(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, {})

    def test_list_all_categories_which_begins_with_letter_none(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, None)

    def test_list_all_categories_which_begins_with_letter_true(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, True)

    def test_list_all_categories_which_begins_with_letter_False(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, False)

    def test_list_all_categories_which_begins_with_letter_int(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, 23)

    def test_list_all_categories_which_begins_with_letter_float(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, 2.1233)

    def test_list_all_categories_which_begins_with_letter_negative_int(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, -21)

    def test_list_all_categories_which_begins_with_letter_negative_float(self):
        self.assertRaises(TypeError, self.temp.list_all_categories_which_begins_with_letter, -2.451)

    def test_list_all_area_which_begins_with_letter(self):
        self.assertEqual(
            ['Polish', 'Portuguese'],
            self.temp.list_all_area_which_begins_with_letter('P'))

    def test_list_all_area_which_begins_with_letter_2(self):
        self.assertEqual(['Greek'],
                         self.temp.list_all_area_which_begins_with_letter('G'))

    def test_list_all_area_which_begins_with_letter_array(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, [])

    def test_list_all_area_which_begins_with_letter_object(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, {})

    def test_list_all_area_which_begins_with_letter_none(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, None)

    def test_list_all_area_which_begins_with_letter_true(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, True)

    def test_list_all_area_which_begins_with_letter_False(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, False)

    def test_list_all_area_which_begins_with_letter_int(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, 23)

    def test_list_all_area_which_begins_with_letter_float(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, 2.1233)

    def test_list_all_area_which_begins_with_letter_negative_int(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, -21)

    def test_list_all_area_which_begins_with_letter_negative_float(self):
        self.assertRaises(TypeError, self.temp.list_all_area_which_begins_with_letter, -2.451)

    def test_list_all_ingredients_which_begins_with_letter(self):
        self.assertEqual(
            ['Pork',
             'Paprika',
             'Parma Ham',
             'Parmesan',
             'Parmesan Cheese',
             'Parmigiano-reggiano',
             'Parsley',
             'Peanut Butter',
             'Peanut Oil',
             'Peanuts',
             'Peas',
             'Pecorino',
             'Penne Rigate',
             'Pepper',
             'Pine Nuts',
             'Pitted Black Olives',
             'Plain Chocolate',
             'Plain Flour',
             'Plum Tomatoes',
             'Potato Starch',
             'Potatoes',
             'Prawns',
             'Puff Pastry',
             'Pretzels',
             'Pilchards',
             'Pappardelle Pasta',
             'Paccheri Pasta',
             'Passata',
             'Pinto Beans',
             'Pecan Nuts',
             'Pumpkin',
             'Peanut Cookies',
             'Peanut Brittle',
             'Peaches',
             'Paneer',
             'Pink Food Colouring',
             'Prosciutto',
             'Pears',
             'Paella Rice',
             'Potatoe Buns',
             'Pork Chops',
             'Persian Cucumber',
             'Pita Bread',
             'Pickle Juice',
             'Powdered Sugar',
             'Polish Sausage'],
            self.temp.list_all_ingredients_which_begins_with_letter('P'))

    def test_list_all_ingredients_which_begins_with_letter_2(self):
        self.assertEqual(['Garam Masala',
                          'Garlic',
                          'Garlic Clove',
                          'Garlic Powder',
                          'Garlic Sauce',
                          'Ghee',
                          'Ginger',
                          'Ginger Cordial',
                          'Ginger Garlic Paste',
                          'Ginger Paste',
                          'Golden Syrup',
                          'Gouda Cheese',
                          'Granulated Sugar',
                          'Grape Tomatoes',
                          'Greek Yogurt',
                          'Green Beans',
                          'Green Chilli',
                          'Green Olives',
                          'Green Red Lentils',
                          'Green Salsa',
                          'Ground Almonds',
                          'Ground Cumin',
                          'Ground Ginger',
                          'Gruyère',
                          'Goose Fat',
                          'Gelatine Leafs',
                          'Green Pepper',
                          'Glace Cherry',
                          'Goats Cheese',
                          'Ground Beef',
                          'Gochujang',
                          'Goat Meat',
                          'Grand Marnier',
                          'Ground Pork',
                          'Gherkin Relish'],
                         self.temp.list_all_ingredients_which_begins_with_letter('G'))

    def test_list_all_ingredients_which_begins_with_letter_array(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, [])

    def test_list_all_ingredients_which_begins_with_letter_object(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, {})

    def test_list_all_ingredients_which_begins_with_letter_none(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, None)

    def test_list_all_ingredients_which_begins_with_letter_true(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, True)

    def test_list_all_ingredients_which_begins_with_letter_False(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, False)

    def test_list_all_ingredients_which_begins_with_letter_int(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, 23)

    def test_list_all_ingredients_which_begins_with_letter_float(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, 2.1233)

    def test_list_all_ingredients_which_begins_with_letter_negative_int(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, -21)

    def test_list_all_ingredients_which_begins_with_letter_negative_float(self):
        self.assertRaises(TypeError, self.temp.list_all_ingredients_which_begins_with_letter, -2.451)
