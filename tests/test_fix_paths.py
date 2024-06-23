from gendiff.formaters.plain import fix_paths_list
import ast
from pathlib import Path


def test_fix_paths():
    with open(Path.cwd() / 'fixtures/paths_list1.txt', 'r',
              encoding='utf-8') as list_of_paths:
        paths_list = ast.literal_eval(list_of_paths.read().strip())
    with open(Path.cwd() / 'fixtures/fixed_paths_list.txt', 'r',
              encoding='utf-8') as fixed_paths_list:
        result = ast.literal_eval(fixed_paths_list.read().strip())
    assert fix_paths_list(paths_list) == result
