#!/usr/bin/env python3
import argparse
import json
import yaml
from gendiff.scripts.comparator import data_parser


def main():  # парсинг путей к файлам
    parser = argparse.ArgumentParser(description='Compares two configuration\
    files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument("-f ", "--format", help='set format of output')
    args = parser.parse_args()

    # вызов функции generate_diff с передачей адресов файлов
    generate_diff(args.first_file, args.second_file)


# вывод словаря1 и словаря2 по результату получения путей к файлу1 и файлу2
def generate_diff(path_file1, path_file2):
    dict1, dict2 = '', ''
    if path_file1.endswith('json') and path_file2.endswith('json'):
        dict1, dict2 = make_json_dicts(path_file1, path_file2)
    if path_file1.endswith('yml') and path_file2.endswith('yml'):
        dict1, dict2 = make_yml_dicts(path_file1, path_file2)
    elif path_file1.endswith('yaml') and path_file2.endswith('yaml'):
        dict1, dict2 = make_yml_dicts(path_file1, path_file2)
    list1, list2 = make_sorted_lists(dict1, dict2)
    data_parser(list1, list2)


# чтение файлов json
def make_json_dicts(path1, path2):
    with open(path1, 'r') as path_1:
        dict1 = json.load(path_1)
    with open(path2, 'r') as path_2:
        dict2 = json.load(path_2)
    return dict1, dict2


# чтение файлов yaml
def make_yml_dicts(path1, path2):
    with open(path1, 'r') as path_1:
        gen_obj1 = yaml.load_all(path_1, Loader=yaml.FullLoader)
        [dict1] = gen_obj1
    with open(path2, 'r') as path_2:
        gen_obj2 = yaml.load_all(path_2, Loader=yaml.FullLoader)
        [dict2] = gen_obj2
    return dict1, dict2


# получение отсортированных списков кортежей с данными из файла1 и файла2
def make_sorted_lists(dict1, dict2):
    sorted_list1 = sorted(dict1.items(), key=lambda x: x[0])
    sorted_list2 = sorted(dict2.items(), key=lambda x: x[0])
    return sorted_list1, sorted_list2


if __name__ == "__main__":
    main()
