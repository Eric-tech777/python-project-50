from gendiff.formaters.plain import get_paths
import ast
from pathlib import Path


def test_find_paths():
    with open(Path(__file__).parent / 'fixtures/ini_dict_for_plain.txt', 'r',
              encoding='utf-8') as ini_dict_1:
        ini_dict = ast.literal_eval(ini_dict_1.read().strip())
    with open(Path(__file__).parent / 'fixtures/key_list_for_plain.txt', 'r',
              encoding='utf-8') as keys_list_1:
        keys_list = ast.literal_eval(keys_list_1.read().strip())
    with open(Path(__file__).parent / 'fixtures/paths_for_plain.txt', 'r',
              encoding='utf-8') as paths_plain:
        result = ast.literal_eval(paths_plain.read().strip())
    assert get_paths(ini_dict, keys_list) == result
