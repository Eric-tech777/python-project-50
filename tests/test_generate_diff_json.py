from gendiff.diff_generator.get_diff import generate_diff
import ast
from pathlib import Path
import pytest


@pytest.fixture
def plain_path1():
    yield "jsonfile1.json"


@pytest.fixture
def plain_path2():
    yield "jsonfile2.json"


@pytest.fixture
def format_name():
    yield "plain"


def test_generate_diff(plain_path1, plain_path2, format_name):
    func_result = generate_diff(plain_path1, plain_path2, format_name)
    with open(Path(__file__).parent / 'fixtures/res_file_plain.txt', 'r',
              encoding='utf-8') as result:
        result_file = ast.literal_eval(result.read().rstrip())
    assert func_result == result_file
