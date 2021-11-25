import requests
import json
from src.check_string import check_string


class list_food:
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

    def list_meal_categories_which_begins_with_letter(self, letter):
        if check_string(letter):
            data = \
                json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/categories.php').text)['categories']
            result = []
            for i in data:
                if i['strCategory'][0] == letter:
                    result.append(i['strCategory'])
            return result

    def list_all_categories_which_begins_with_letter(self, letter):
        if check_string(letter):
            data = \
                json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/list.php?c=list').text)['meals']
            result = []
            for i in data:
                if i['strCategory'][0] == letter:
                    result.append(i['strCategory'])
            return result

    def list_all_area_which_begins_with_letter(self, letter):
        if check_string(letter):
            data = \
                json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/list.php?a=list').text)['meals']
            result = []
            for i in data:
                if i['strArea'][0] == letter:
                    result.append(i['strArea'])
            return result

    def list_all_ingredients_which_begins_with_letter(self, letter):
        if check_string(letter):
            data = \
                json.loads(requests.get('http://www.themealdb.com/api/json/v1/1/list.php?i=list').text)['meals']
            result = []
            for i in data:
                if i['strIngredient'][0] == letter:
                    result.append(i['strIngredient'])
            return result
