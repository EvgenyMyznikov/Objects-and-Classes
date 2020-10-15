from collections import Counter
import xml.etree.ElementTree as Et
parser = Et.XMLParser(encoding="utf-8")
tree = Et.parse("newsafr.xml", parser)
root = tree.getroot()


def read_file_to_top_10(file_name):
    with open(file_name) as file:
        items = root.findall("channel/item")
        top_list = []
        for item in items:
            original_text = item.find('description').text
            long_words = original_text.lower().split(' ')
            for word in long_words:
                if len(word) > 6:
                    top_list.append(word)
                    top_word_list = Counter(top_list)
                    top_10_list = sorted(top_word_list.items(), key=lambda x: x[1], reverse=True)
        return top_10_list[0:10]


print(read_file_to_top_10('newsafr.xml'))

