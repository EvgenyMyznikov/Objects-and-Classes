from collections import Counter
import xml.etree.ElementTree as Et
parser = Et.XMLParser(encoding="utf-8")
tree = Et.parse("newsafr.xml", parser)
root = tree.getroot()
items = root.findall("channel/item")


def read_file_to_top_10(top_10_list, len_words=6, k=10):
    top_list = []
    for item in items:
        original_text = item.find('description').text.lower().split(' ')
        for word in original_text:
            if len(word) > len_words:
                top_list.append(word)
                top_word_list = Counter(top_list)
                top_10_list = sorted(top_word_list.items(), key=lambda x: x[1], reverse=True)
    return top_10_list[0:k]


def main():
    while True:
        name = input('Введите имя файла: newsafr.xml. Выход - exit: ')
        if name == 'newsafr.xml':
            print('Идет обработка файла ...')
            top_10_words = read_file_to_top_10(name)
            for i in top_10_words:
                print(i[0], ':', i[1])
        elif name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')


main()
