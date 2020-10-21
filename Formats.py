from collections import Counter
import json
import xml.etree.ElementTree as Et


def read_json(file_name):
    with open(file_name) as file:
        json_data = json.load(file)
        original_text = ''
        for items in json_data['rss']['channel']['items']:
            original_text += items['description']
            words_list = original_text.lower().split(' ')
        return words_list


def read_xml(file_name):
    parser = Et.XMLParser(encoding="utf-8")
    tree = Et.parse("newsafr.xml", parser)
    root = tree.getroot()
    items = root.findall("channel/item")
    original_text = ''
    for item in items:
        original_text += item.find('description').text
        words_list = original_text.lower().split(' ')
    return words_list


def count_len_words(words_list, len_words=6):
    long_words = []
    for word in words_list:
        if len(word) > len_words:
            long_words.append(word)
    return long_words


def sort_top_words(long_words, len_top=10):
    top_list = Counter(long_words)
    repeat_list = sorted(top_list.items(), key=lambda x: x[1], reverse=True)
    top_repeat_words = repeat_list[0:len_top]
    return top_repeat_words


def main():
    file_name = input('Enter file name:  ')
    if file_name == 'newsafr.xml':
        print('File processing in progress ...')
        top_repeat_words = sort_top_words(count_len_words(read_xml(file_name)))
        for i in top_repeat_words:
            print(i[0], ':', i[1])
    elif file_name == 'newsafr.json':
        top_repeat_words = sort_top_words(count_len_words(read_json(file_name)))
        for i in top_repeat_words:
            print(i[0], ':', i[1])
    else:
        print('Incorrect entry, repeat.')


main()
