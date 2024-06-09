from gendiff.formaters.json import make_json
import ast


def test_json():
    with (open('fixtures/data_frame_json_1.txt', 'r', encoding='utf-8')
          as json_frame):
        data_frame = ast.literal_eval(json_frame.read().strip())
    with (open('fixtures/master_file_json_1.txt', 'r', encoding='utf-8')
          as json_master_file):
        result = ast.literal_eval(json_master_file.read().strip())
    assert make_json(data_frame) == result
