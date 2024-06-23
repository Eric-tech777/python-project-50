from gendiff.formaters.plain import merge_list_to_sort
import ast
from pathlib import Path


def test_merge_list_to_sort():
    with open(Path.cwd() / 'fixtures/list_keys1.txt', 'r',
              encoding='utf-8') as keys_list:
        list_keys = ast.literal_eval(keys_list.read().strip())
    with (open(Path.cwd() / 'fixtures/list_of_paths1.txt', 'r',
               encoding='utf-8') as paths_list):
        list_of_paths = ast.literal_eval(paths_list.read().strip())
    with (open(Path.cwd() / 'fixtures/list_values1.txt', 'r',
               encoding='utf-8') as values_list):
        list_values = ast.literal_eval(values_list.read().strip())
    with (open(Path.cwd() / 'fixtures/list_merged_to_sort.txt', 'r',
               encoding='utf-8') as merged_list_to_sort):
        result = ast.literal_eval(merged_list_to_sort.read().strip())
    assert merge_list_to_sort(list_keys, list_of_paths, list_values) == result
