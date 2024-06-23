from gendiff.diff_generator.get_diff import generate_diff
import ast
from pathlib import Path
import os


def test_generate_diff():
	file_path1 = 'jsonfile1.json'
	file_path2 = 'jsonfile2.json'
	format_name = 'stylish'
	with (open(Path.cwd() / 'fixtures/res_file_json.txt', 'r',
							encoding='utf-8') as result_stylish):
		result = ast.literal_eval(result_stylish.read().strip())
	previous = os.getcwd()
	os.chdir(os.path.dirname(os.getcwd()))
	assert generate_diff(file_path1, file_path2, format_name) == result
	os.chdir(previous)
