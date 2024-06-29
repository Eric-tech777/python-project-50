#!/usr/bin/env python3
from pathlib import Path
from gendiff.diff_generator.paths_parser import path_parser
import json
import yaml
from gendiff.diff_generator.comparator import run_compare
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import make_json


def start_diff():
    args = path_parser()
    generate_diff(args.first_file, args.second_file, args.format)


def generate_diff(path_file1, path_file2, format_name='stylish'):  # 1
    type_of_files = get_files_type(path_file1, path_file2)  # 2
    dict_1, dict_2 = make_dicts(path_file1, path_file2, type_of_files)  # 3
    frame_to_print = perform_compare(dict_1, dict_2)  # 4
    result = release_diff(frame_to_print, format_name)  # 5
    if format_name == 'plain':
        for i in result:
            print(i)
        return result
    else:
        print(result)
        return result


def get_files_type(path1, path2):  # 2
    file_type = ''
    if path1.endswith('json') and path2.endswith('json'):
        file_type = 'json'
    if (path1.endswith('yml') or path1.endswith('yaml')
            and path2.endswith('yml') or path2.endswith('yaml')):
        file_type = 'yaml'
    return file_type


def make_dicts(path1, path2, type_of_file):  # 3
    dict1 = ''
    dict2 = ''
    with open(Path(__file__).parent.parent.parent / 'tests/fixtures/' / path1,
              'r', encoding='utf-8') as path_1:
        with open(Path(__file__).parent.parent.parent / 'tests/fixtures/'
                  / path2, 'r', encoding='utf-8') as path_2:
            if type_of_file == 'json':
                dict1 = json.load(path_1)
                dict2 = json.load(path_2)
            elif type_of_file == 'yaml':
                gen_obj1 = yaml.load_all(path_1, Loader=yaml.FullLoader)
                [dict1] = gen_obj1
                gen_obj2 = yaml.load_all(path_2, Loader=yaml.FullLoader)
                [dict2] = gen_obj2
    return dict1, dict2


# получениe представления (словаря с diff) # 4
def perform_compare(dict1, dict2):
    run_compare(dict1, dict2)
    frame_to_print = run_compare(dict1, dict2)
    return frame_to_print


# вызов форматеров
def release_diff(frame_to_print, format_name):  # 5
    if format_name == 'plain':
        return plain(frame_to_print)
    elif format_name == 'json':
        return make_json(frame_to_print)
    else:
        return stylish(frame_to_print)
