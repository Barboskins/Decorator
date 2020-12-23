'''
Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт

Должен получится следующий словарь

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
'''

from pprint import pprint
from decorator import creating_a_decorator_with_arguments
import os

with open ('recipes.txt', encoding = 'utf-8') as f:
    file_ = f.read()
    file_ = file_.split('\n\n')
# print(file_)

class Dish:
    def __init__(self,name_d, list_ing):
        self.name_d = name_d
        self.list_ing = list_ing

class Ingredient:
    def __init__(self, name_i, quantity, measure):
        self.name_i = name_i
        self.quantity = quantity
        self.measure = measure

file_path = os.path.join(os.getcwd(), "data_something_func_3.txt")
@creating_a_decorator_with_arguments(file_path)
def cooking():
    cook_book = {}
    for dish in file_:
        dish = dish.split('\n')
        # print(dish)
        dish = Dish(dish[0], dish[2:])
        list_ing = []
        for ingr in dish.list_ing:
            ingr = ingr.split('|')
            # print(ingr)
            ingr = Ingredient(ingr[0], ingr[1], ingr[2])
            dish_ingredients = {'ingredient_name': ingr.name_i.strip(), 'quantity': int(ingr.quantity),
                                'measure': ingr.measure.strip()}
            # print(dish_ingredients)
            list_ing.append(dish_ingredients)
            # print(list_ing)
        cook_book[dish.name_d] = list_ing
    return cook_book

if __name__ == '__main__':
 cooking()




