from gendiff.diff_generator.get_diff import perform_compare
import ast
from pathlib import Path


def test_perform_compare():
    with open(Path(__file__).parent / 'fixtures/compare_dict1.txt', 'r',
              encoding='utf-8') as dict1_to_compare:
        dict_1 = ast.literal_eval(dict1_to_compare.read().strip())
    with open(Path(__file__).parent / 'fixtures/compare_dict2.txt', 'r',
              encoding='utf-8') as dict2_to_compare:
        dict_2 = ast.literal_eval(dict2_to_compare.read().strip())
    with open(Path(__file__).parent / 'fixtures/check_perform_compare.txt', 'r',
              encoding='utf-8') as dicts_compare_result:
        result = ast.literal_eval(dicts_compare_result.read().strip())
    assert perform_compare(dict_1, dict_2) == result
