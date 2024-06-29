from gendiff.diff_generator.get_diff import generate_diff
import ast
from pathlib import Path
import os
import pytest


@pytest.mark.parametrize("file_path1, file_path2, format_name, result_file", [
("jsonfile1.json", "jsonfile2.json", "stylish", "res_file_stylish.txt"),
("jsonfile1.json", "jsonfile2.json", "json", "res_file_json.txt"),
("jsonfile1.json", "jsonfile2.json", "plain", "res_file_plain.txt"),
("ymlfile1.yml", "ymlfile2.yml", "stylish", "res_file_stylish.txt"),
# ("yamlfile1.yaml", "yamlfile2.yaml", "plain", "res_file_plain.txt"),
("ymlfile1.yml", "ymlfile2.yml", "json", "res_file_json.txt")])
def test_generate_diff(file_path1, file_path2, format_name, result_file):
	with (open(Path(__file__).parent / 'fixtures/' / result_file, 'r', encoding='utf-8') as result):
		result_file = ast.literal_eval(result.read().strip())
	previous = os.getcwd()
	os.chdir(os.path.dirname(os.getcwd()))
	assert generate_diff(file_path1, file_path2, format_name) == result_file
	os.chdir(previous)
