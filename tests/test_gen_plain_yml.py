from gendiff.diff_generator.get_diff import generate_diff
import ast
from pathlib import Path
import os


def test_generate_plain_diff():
	file_path1 = 'ymlfile1.yml'
	file_path2 = 'ymlfile2.yml'
	format_name = 'plain'
	with open(Path.cwd() / 'fixtures/res_plain_yml.txt', 'r',
						encoding='utf-8') as result_plain:
		plain_result = ast.literal_eval(result_plain.read().strip())
	previous = os.getcwd()
	os.chdir(os.path.dirname(os.getcwd()))
	assert generate_diff(file_path1, file_path2, format_name) == plain_result
	os.chdir(previous)
