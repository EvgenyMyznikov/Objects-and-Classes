def read_files(file_name):
    import json
    with open(file_name) as file:
        json_data = json.load(file)
        original_text = ''
        for items in json_data['rss']['channel']['items']:
            original_text += items['description']
            words_list = original_text.lower().split(' ')
        return words_list


def count_len_words(words_list):
    long_words = []
    for word in words_list:
        if len(word) > 6:
            long_words.append(word)
    return long_words


def sort_top_words(long_words):
    from collections import Counter
    top_list = Counter(long_words)
    top_10_list = sorted(top_list.items(), key=lambda x: x[1], reverse=True)
    top_10_words = top_10_list[0:10]
    return top_10_words


def main():
    while True:
        name = input('Введите имя файла: newsafr.json. Выход - exit: ')
        if name == 'newsafr.json':
            print('Идет обработка файла ...')
            top_10_words = sort_top_words(count_len_words(read_files(name)))
            for i in top_10_words:
                print(i[0], ':', i[1])
        elif name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')


main()



