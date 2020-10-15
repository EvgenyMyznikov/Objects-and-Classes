import json
from collections import Counter


def read_file_to_top_10(file_name):
    with open(file_name) as file:
        json_data = json.load(file)
        original_text = ''
        for items in json_data['rss']['channel']['items']:
            original_text += items['description']
            words_list = original_text.lower().split(' ')
            long_words = []
            for word in words_list:
                if len(word) > 6:
                    long_words.append(word)
                    top_list = Counter(long_words)
                    top_10_list = sorted(top_list.items(), key=lambda x: x[1], reverse=True)
        return top_10_list[0:10]


print(read_file_to_top_10('newsafr.json'))


