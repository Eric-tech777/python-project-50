from gendiff.diff_generator.comparator import order_dict
import ast


def test_order_diff():
    with (open('fixtures/dict_to_order_1.txt', 'r', encoding='utf-8')
          as dict_to_sort):
        dict_to_order = ast.literal_eval(dict_to_sort.read().strip())
    with (open('fixtures/sorted_dict_1.txt', 'r', encoding='utf-8')
          as sorted_dict):
        result = ast.literal_eval(sorted_dict.read().strip())
    assert order_dict(dict_to_order) == result
