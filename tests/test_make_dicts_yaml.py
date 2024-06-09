from gendiff.diff_generator.get_diff import make_dicts
import ast


def test_yaml_dicts():
    with (open('/home/irken/Hexlet_2/Version_1/'
               'python-project-50/tests/fixtures/dicts_from_json.txt',
               'r', encoding='utf-8') as yaml_dicts):
        dict1, dict2 = ast.literal_eval(yaml_dicts.read().strip())
    assert make_dicts('file_1.yaml', 'file_2.yaml', 'yaml') == (dict1, dict2)
