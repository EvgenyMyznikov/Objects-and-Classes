with open('recipes.txt', encoding='utf-8') as file:
    recipes = file.read()
    recipes = recipes.split('\n\n')
    cook_book = {}
for item in recipes:
    item = item.split('\n')
    dish = item[0].strip()
    list_ing = item[2:]
    ingredient_list = []
    for elem in list_ing:
        elem = elem.split('|')
        elem_dict = {
            'ingredient_name': elem[0].strip(),
            'quantity': int(elem[1].strip()),
            'measure': elem[2].strip()}
        ingredient_list.append(elem_dict)
        cook_book[dish] = ingredient_list
print(cook_book)
