from gendiff.formaters.plain import get_data_frame
import ast
from pathlib import Path


def test_get_data_frame():
    with open(Path(__file__).parent / 'fixtures/data_frame1.txt', 'r',
              encoding='utf-8') as frame_of_data:
        merged_list = ast.literal_eval(frame_of_data.read().strip())
    with open(Path(__file__).parent / 'fixtures/merged_list1.txt', 'r',
              encoding='utf-8') as list_merged:
        result = ast.literal_eval(list_merged.read().strip())
    assert get_data_frame(merged_list) == result
