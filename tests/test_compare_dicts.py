from gendiff.diff_generator.comparator import dicts_compare
import ast
from pathlib import Path


def test_compare_dicts():
    with open(Path.cwd() / 'tests/fixtures/compare_dict_1.txt', 'r',
              encoding='utf-8') as dict1_to_compare:
        dict_1 = ast.literal_eval(dict1_to_compare.read().strip())
    with open(Path.cwd() / tests/fixtures/compare_dict_2.txt', 'r',
              encoding='utf-8') as dict2_to_compare:
        dict_2 = ast.literal_eval(dict2_to_compare.read().strip())
    with open(Path.cwd() / tests/fixtures/compare_dicts_result.txt', 'r',
              encoding='utf-8') as dicts_compare_result:
        result = ast.literal_eval(dicts_compare_result.read().strip())
    assert dicts_compare(dict_1, dict_2) == result
