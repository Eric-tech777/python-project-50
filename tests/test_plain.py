from gendiff.formaters.plain import plain
from pathlib import Path
import ast


def test_plain():
    with open(Path(__file__).parent / 'fixtures/ini_dict_plain.txt', 'r',
              encoding='utf-8') as dict_plain:
        ini_dict = ast.literal_eval(dict_plain.read().strip())
    with open(Path(__file__).parent / 'fixtures/plain_result.txt', 'r',
              encoding='utf-8') as plain_result:
        result = plain_result.read().strip()
    assert plain(ini_dict) == result
