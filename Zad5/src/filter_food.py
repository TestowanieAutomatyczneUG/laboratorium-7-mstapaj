import requests
import json
from src.check_string import check_string


class filter_food:

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
