#!/usr/bin/env python3
import argparse
import json
import yaml
from gendiff.scripts.comparator import comparator, order_dict
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import make_json


def main():  # парсинг путей к файлам и указание форматера по умолчанию
    parser = argparse.ArgumentParser(description='Compares two configuration\
    files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument("-f", "--format", type=str,
                        default="stylish", help='set format of output')
    args = parser.parse_args()

    # вызов функции generate_diff с передачей адресов файлов и формата вывода
    generate_diff(args.first_file, args.second_file, args.format)


# вывод словаря1 и словаря2 по результату получения путей к файлу1 и файлу2
def generate_diff(path_file1, path_file2, format_name):
    dict1, dict2 = '', ''
    if path_file1.endswith('json') and path_file2.endswith('json'):
        dict1, dict2 = make_json_dicts(path_file1, path_file2)

    if path_file1.endswith('yml') and path_file2.endswith('yml'):
        dict1, dict2 = make_yml_dicts(path_file1, path_file2)

    elif path_file1.endswith('yaml') and path_file2.endswith('yaml'):
        dict1, dict2 = make_yml_dicts(path_file1, path_file2)

# **вызов модуля comparator для получения представления (словаря с diff)**
    comparator(dict1, dict2)
    data1 = comparator(dict1, dict2)
    data2 = order_dict(data1)

# вызов форматеров
    if format_name == 'plain':
        plain(data2)
    elif format_name == 'json':
        print(make_json(data2))
    else:
        print(stylish(data2))


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


if __name__ == "__main__":
    main()
