from gendiff.formaters.stylish import stylish
import ast
from pathlib import Path


def test_stylish():
    with open(Path.cwd() / 'fixtures/data_frame_stylish1.txt', 'r',
              encoding='utf-8') as stylish_frame:
        data_frame = ast.literal_eval(stylish_frame.read().strip())
    with open(Path.cwd() / 'fixtures/stylish_master_file1.txt', 'r',
              encoding='utf-8') as stylish_master_file:
        result = ast.literal_eval(stylish_master_file.read().strip())
    assert stylish(data_frame, count_space=4) == result
