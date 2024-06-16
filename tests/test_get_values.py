from gendiff.formaters.plain import get_list_of_values
import ast
from pathlib import Path


def test_get_values():
    with (open(Path.cwd() / 'tests/fixtures/ini_dict_values_1.txt', 'r',
               encoding='utf-8')
          as dict_1):
        ini_dict = ast.literal_eval(dict_1.read().strip())
    with (open(Path.cwd() / 'tests/fixtures/for_list_of_values_1.txt', 'r',
               encoding='utf-8')
          as list_1):
        result = ast.literal_eval(list_1.read().strip())
    assert get_list_of_values(ini_dict) == result
