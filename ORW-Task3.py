import os
from operator import itemgetter


def glue_files(file_list):
    all_files = file_name_path_count(file_list)
    file_path_result = os.path.join(os.getcwd(), 'result.txt')
    with open(file_path_result, 'w', encoding='utf-8') as f_write:
        for file in all_files:
            f_write.write(file[0] + '\n')
            f_write.write(str(file[2]) + '\n')
            with open(file[1], 'r', encoding='utf-8') as f_read:
                for line in f_read:
                    f_write.write(line)


def get_count_str(path):
    count = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
    return count


def file_name_path_count(file_list):
    all_files = []
    for file in file_list:
        file_path = os.path.join(os.getcwd(), file)
        count_str = get_count_str(file_path)
        all_files.append((file, file_path, count_str))
    return sorted(all_files, key=itemgetter(2))


files = ['1.txt', '2.txt', '3.txt']
glue_files(files)