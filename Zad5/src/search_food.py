import requests
import json
from src.check_string import check_string


class search_food:

    def search_meal_by_name(self, name):
        if check_string(name):
            result = []
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?s={name}').text)['meals']
            for i in data:
                result.append({
                    'id': i['idMeal'],
                    'meal': i['strMeal'],
                    'category': i['strCategory'],
                    'area': i['strArea']
                })
            return result

    def search_meal_by_name_with_all_details(self, name):
        if check_string(name):
            result = []
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?s={name}').text)['meals']
            for i in data:
                ingredients = []
                counter = 0
                for j in list(i.keys()):
                    if j[0:13] == 'strIngredient':
                        if i[j] != 'null' and i[j] != '' and i[j] != None:
                            ingredients.append(i[j])
                    if j[0:10] == 'strMeasure':
                        if i[j] != 'null' and i[j] != '' and i[j] != ' ' and i[j] != None:
                            ingredients[counter] = str(ingredients[counter]) + ' ' + str(i[j])
                            counter += 1
                result.append({
                    'id': i['idMeal'],
                    'meal': i['strMeal'],
                    'category': i['strCategory'],
                    'area': i['strArea'],
                    'instructions': i['strInstructions'],
                    'photoLink': i['strMealThumb'],
                    'youtubeLink': i['strYoutube'],
                    'ingredients': ingredients,
                    'sourceLink': i['strSource'],
                    'imageSourceLink': i['strImageSource'],
                    'creativeCommonsConfirmed': i['strCreativeCommonsConfirmed'],
                    'dateModified': i['dateModified']
                })
            return result

    def search_meal_by_id(self, id):
        if isinstance(id, int) and str(id) != 'True' and str(id) != 'False':
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}').text)['meals'][0]
            result = {
                'id': data['idMeal'],
                'meal': data['strMeal'],
                'category': data['strCategory'],
                'area': data['strArea']
            }
            return result
        else:
            raise TypeError("Id nie jest typu int")

    def search_meal_by_id_with_all_details(self, id):
        if isinstance(id, int) and str(id) != 'True' and str(id) != 'False':
            data = \
                json.loads(requests.get(f'http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}').text)['meals'][0]
            ingredients = []
            counter = 0
            for j in list(data.keys()):
                if j[0:13] == 'strIngredient':
                    if data[j] != 'null' and data[j] != '' and data[j] != None:
                        ingredients.append(data[j])
                if j[0:10] == 'strMeasure':
                    if data[j] != 'null' and data[j] != '' and data[j] != ' ' and data[j] != None:
                        ingredients[counter] = str(ingredients[counter]) + ' ' + str(data[j])
                        counter += 1
            result = {
                'id': data['idMeal'],
                'meal': data['strMeal'],
                'category': data['strCategory'],
                'area': data['strArea'],
                'instructions': data['strInstructions'],
                'photoLink': data['strMealThumb'],
                'youtubeLink': data['strYoutube'],
                'ingredients': ingredients,
                'sourceLink': data['strSource'],
                'imageSourceLink': data['strImageSource'],
                'creativeCommonsConfirmed': data['strCreativeCommonsConfirmed'],
                'dateModified': data['dateModified']
            }
            return result
        else:
            raise TypeError("Id nie jest typu int")
