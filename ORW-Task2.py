cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
                       {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
                       {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}],
             'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
                                  {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
                                  {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
                                  {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}],
             'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
                                      {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
                                      {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}],
             'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
                         {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
                         {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
                         {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
                         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]}


def get_shop_list_by_dishes(dishes, person_count):
    dishes = dishes.split(',')
    key_list = []
    quantity_list = []
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            key = ingredient['ingredient_name']
            key_list.append(key)
            quantity = ingredient['quantity']
            quantity = quantity * person_count
            if quantity in quantity_list:
                quantity = quantity * quantity_list.count(quantity)
                quantity_list.append(quantity)
            else:
                quantity_list.append(quantity)
            measure = ingredient['measure']
            shop_list[key] = {'quantity': quantity, 'measure': measure}
    return shop_list


print(get_shop_list_by_dishes((input('Введите названия блюд через запятую: ')),
                              (int(input('Введите количество персон: ')))))
