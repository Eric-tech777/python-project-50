from gendiff.scripts.gendiff import make_sorted_lists


def test_lists_happy_path():
    dict_1 = {'form': '', 'title': 0, 'proxy': '123.234.53.22'}
    dict_2 = {'timeout': 20, 'title': 3.65, 'color': 'Black'}
    assert make_sorted_lists(dict_1, dict_2) == ([('form', ''),
    ('proxy', '123.234.53.22'), ('title', 0)], [('color', 'Black'),
    ('timeout', 20), ('title', 3.65)])


def test_lists_empty():
    dict01 = {}
    dict02 = {}
    assert make_sorted_lists(dict01, dict02) == ([], [])
