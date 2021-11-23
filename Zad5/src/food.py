import requests
import json


def check_string(word):
    if isinstance(word, str):
        return True
    else:
        raise TypeError("Podane słowo nie jest stringiem")


class food:

    def search_meal_by_name(self, name):
        if check_string(name):
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?s={name}').text)['meals'][0]
            result = {
                'id': data['idMeal'],
                'meal': data['strMeal'],
                'category': data['strCategory'],
                'area': data['strArea'],
                'instructions': data['strInstructions']
            }
            return result

    def list_meals_by_first_letter(self, letter):
        if check_string(letter):
            if len(letter) == 1:
                result = []
                data = \
                    json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?f={letter}').text)[
                        'meals']
                for i in data:
                    result.append({'id': i['idMeal'], 'meal': i['strMeal']})
                return result
            else:
                raise ValueError('Podane dane nie są pojedyńczą literą')

    def search_meal_by_id(self, id):
        if isinstance(id, int) and str(id) != 'True' and str(id) != 'False':
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}').text)['meals'][0]
            result = {
                'id': data['idMeal'],
                'meal': data['strMeal'],
                'category': data['strCategory'],
                'area': data['strArea'],
                'instructions': data['strInstructions']
            }
            return result
        else:
            raise TypeError("Id nie jest typu int")

    def list_meal_categories(self):
        data = \
            json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/categories.php').text)['categories']
        result = []
        for i in data:
            result.append({'id': i['idCategory'], 'category': i['strCategory']})
        return result

    def list_all_categories(self):
        data = \
            json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/list.php?c=list').text)['meals']
        result = []
        for i in data:
            result.append(i['strCategory'])
        return result

    def list_all_area(self):
        data = \
            json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/list.php?a=list').text)['meals']
        result = []
        for i in data:
            result.append(i['strArea'])
        return result

    def list_all_ingredients(self):
        data = \
            json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/list.php?i=list').text)['meals']
        result = []
        for i in data:
            result.append(i['strIngredient'])
        return result

    def filter_by_main_ingredient(self, word):
        if check_string(word):
            result = []
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/filter.php?i={word}').text)[
                    'meals']
            for i in data:
                result.append({'id': i['idMeal'], 'meal': i['strMeal']})
            return result

    def filter_by_category(self, word):
        if check_string(word):
            result = []
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/filter.php?c={word}').text)[
                    'meals']
            for i in data:
                result.append({'id': i['idMeal'], 'meal': i['strMeal']})
            return result

    def filter_by_area(self, word):
        if check_string(word):
            result = []
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/filter.php?a={word}').text)[
                    'meals']
            for i in data:
                result.append({'id': i['idMeal'], 'meal': i['strMeal']})
            return result

