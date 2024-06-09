from gendiff.diff_generator.get_diff import get_files_type


def test_get_files_type():
    json_file1 = 'file_1.json'
    json_file2 = 'file_2.json'
    yaml_file1 = 'file_1.yaml'
    yaml_file2 = 'file_2.yaml'
    yml_file1 = 'file_1.yml'
    yml_file2 = 'file_2.yml'
    assert get_files_type(json_file1, json_file2) == 'json'
    assert get_files_type(yaml_file1, yaml_file2) == 'yaml'
    assert get_files_type(yml_file1, yml_file2) == 'yaml'
