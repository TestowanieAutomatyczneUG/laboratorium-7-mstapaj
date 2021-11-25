import unittest
from src.filter_food import filter_food


class test_filter_food(unittest.TestCase):

    def setUp(self):
        self.temp = filter_food()

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
