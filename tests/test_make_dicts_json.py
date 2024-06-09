from gendiff.diff_generator.get_diff import make_dicts
import ast


def test_json_dicts():
    with (open('/home/irken/Hexlet_2/Version_1/'
               'python-project-50/tests/fixtures/dicts_from_json.txt',
               'r', encoding='utf-8') as json_dicts):
        dict1, dict2 = ast.literal_eval(json_dicts.read().strip())
    assert make_dicts('file_1.json', 'file_2.json', 'json') == (dict1, dict2)
