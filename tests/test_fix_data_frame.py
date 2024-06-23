from gendiff.formaters.plain import fix_frame
import ast
from pathlib import Path


def test_fix_data_frame():
    with open(Path.cwd() / 'fixtures/frame_to_fix1.txt', 'r',
              encoding='utf-8') as frame_1:
        frame_to_fix = ast.literal_eval(frame_1.read().strip())
    with open(Path.cwd() / 'fixtures/fixed_frame.txt', 'r',
              encoding='utf-8') as frame_fixed:
        result = ast.literal_eval(frame_fixed.read().strip())
    assert fix_frame(frame_to_fix) == result
