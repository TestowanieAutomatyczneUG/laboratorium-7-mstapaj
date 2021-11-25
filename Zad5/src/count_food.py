import requests
import json
from src.check_string import check_string


class count_food:

    def count_list_meals_by_first_letter(self, letter):
        if check_string(letter):
            if len(letter) == 1:
                data = \
                    json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?f={letter}').text)[
                        'meals']
                return len(data)
            else:
                raise ValueError('Podane dane nie są pojedyńczą literą')

    def count_meals_filtered_by_main_ingredient(self, word):
        if check_string(word):
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/filter.php?i={word}').text)[
                    'meals']
            return len(data)

    def count_meals_filtered_by_category(self, word):
        if check_string(word):
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/filter.php?c={word}').text)[
                    'meals']
            return len(data)

    def count_meals_filtered_by_area(self, word):
        if check_string(word):
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/filter.php?a={word}').text)[
                    'meals']
            return len(data)
