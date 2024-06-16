from gendiff.diff_generator.get_diff import make_dicts
import ast
import os
from pathlib import Path


def test_yaml_dicts():
    with open(Path.cwd() / 'tests/fixtures/dicts_from_json.txt', 'r',
              encoding='utf-8') as yaml_dicts:
        dict1, dict2 = ast.literal_eval(yaml_dicts.read().strip())
    previous = os.getcwd()
    os.chdir(os.path.dirname(os.getcwd()))
    assert make_dicts('yamlfile1.yaml', 'yamlfile2.yaml', 'yaml') == (dict1, dict2)
    os.chdir(previous)
