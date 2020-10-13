import json
import chardet


def read_files(name):
    with open(name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = json.loads(data)
        original_text = ''
        for items in data['rss']['channel']['items']:
            original_text += ' ' + items['description']
        return original_text


def count_word(original_text):
    to_list = original_text.split(' ')
    word_value = {}
    for word in to_list:
        if len(word) > 6:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value


def sort_top(word_value):
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key=l, reverse=True)
    count = 1
    top_10 = {}
    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == 10:
            break
    return top_10


def main():
    while True:
        name = input('Введите имя файла: ,Выход - exit: ')
        if name == 'newsafr.json':
            print('Идет обработка файла ...')
            top_10 = sort_top(count_word(read_files(name)))
            for i in top_10.values():
                print(i[1], ': ', i[0])
        elif name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')


main()
