from collections import Counter
import json
import xml.etree.ElementTree as Et


def read_json(file_name):
    with open(file_name) as file:
        json_data = json.load(file)
    original_text = ''
    for items in json_data['rss']['channel']['items']:
        original_text += items['description']
    words_list = original_text.lower().strip().split()
    return words_list


def read_xml(file_name):
    parser = Et.XMLParser(encoding="utf-8")
    tree = Et.parse("newsafr.xml", parser)
    root = tree.getroot()
    items = root.findall("channel/item")
    original_text = ''
    for item in items:
        original_text += item.find('description').text
    words_list = original_text.lower().strip().split()
    return words_list


def count_len_words(words_list, len_words=6):
    long_words = []
    for word in words_list:
        if len(word) > len_words:
            long_words.append(word)
    return long_words


def sort_top_words(long_words, len_top=10):
    top_list = Counter(long_words)
    return top_list.most_common(len_top)


def main():
    while True:
        file_name = input('Enter file name:  ')
        data = False
        if ".xml" in file_name:
            print('File processing in progress ...')
            data = read_xml(file_name)
        elif ".json" in file_name:
            data = read_json(file_name)
        else:
            print('Incorrect entry, repeat.')
        if data:
            top_repeat_words = sort_top_words(count_len_words(data))
            for i in top_repeat_words:
                print(i[0], ':', i[1])


main()
