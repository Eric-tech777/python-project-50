from gendiff.formaters.plain import get_data_frame
import ast


def test_get_data_frame():
    with (open('fixtures/data_frame_1.txt', 'r', encoding='utf-8')
          as frame_of_data):
        merged_list = ast.literal_eval(frame_of_data.read().strip())
    with (open('fixtures/merged_list_1.txt', 'r', encoding='utf-8')
          as list_merged):
        result = ast.literal_eval(list_merged.read().strip())
    assert get_data_frame(merged_list) == result
