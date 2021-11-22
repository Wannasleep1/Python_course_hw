import os
from pprint import pprint


def get_list_of_food(file):
    list_of_all_food = []
    qty = int(file.readline())
    for i in range(qty):
        food_list = [food.strip() for food
                     in file.readline().split(' | ')]
        food_dict = {'ingredient_name': food_list[0],
                     'quantity': int(food_list[1]),
                     'measure': food_list[2],
                     }
        list_of_all_food.append(food_dict)
    return list_of_all_food


def convert_file_into_dict(path):
    cook_book = {}
    with open(path, 'r', encoding='utf-8') as file:
        name = file.readline()
        while name:
            list_of_food = get_list_of_food(file)
            cook_book[name.strip()] = list_of_food
            file.readline()
            name = file.readline()
    return cook_book


def get_cook_book(path=None):
    if path:
        cook_book = convert_file_into_dict(path)
    else:
        path = input('Enter path to cook book file: ')
        cook_book = convert_file_into_dict(path)
    return cook_book


def add_food_to_shop_dict(food_lst, shop_dict, person_count):
    for food_dict in food_lst:
        quantity = person_count * food_dict['quantity']
        name = food_dict['ingredient_name']
        if name in shop_dict:
            shop_dict[name]['quantity'] += quantity
        else:
            shop_dict[name] = {'measure': food_dict['measure'], 'quantity': quantity}


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    failed_to_add = []
    cook_book = get_cook_book(os.path.join(os.getcwd(), 'recipes.txt'))
    for dish in dishes:
        if dish in cook_book:
            food_lst = cook_book[dish]
            add_food_to_shop_dict(food_lst, shop_dict, person_count)
        else:
            failed_to_add.append(dish)
    print(f'Failed to add the folowing dishes: {", ".join(failed_to_add)}.\n'
          if failed_to_add else '', end='')
    return shop_dict


pprint(convert_file_into_dict(os.path.join(os.getcwd(), 'recipes.txt')))
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))