from gendiff.scripts.comparator import tip_out


def test_get_result():
    list1 = [('image', False), ('job', '45.56.33'), ('skill', 24)]
    list2 = [('job', ' '), ('port', 0), ('skill', 24)]
    sort_result_list = [('image', False), ('job', '45.56.33'), ('job', ' '),
                        ('port', 0), ('skill', 24)]
    with open("check_json.txt", 'r') as file_to_check:
        assert tip_out(sort_result_list, list1, list2) == file_to_check.read()
