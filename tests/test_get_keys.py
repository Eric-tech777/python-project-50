from gendiff.formaters.plain import get_keys_list
import ast
from pathlib import Path


def test_get_keys_list():
    with open(Path.cwd() / 'tests/fixtures/ini_dict_1.txt', 'r',
              encoding='utf-8') as dict_ini:
        ini_dict = ast.literal_eval(dict_ini.read().strip())
    with (open(Path.cwd() / 'tests/fixtures/keys_list_1.txt', 'r',
               encoding='utf-8') as list_of_keys):
        result = ast.literal_eval(list_of_keys.read().strip())
    assert get_keys_list(ini_dict) == result
