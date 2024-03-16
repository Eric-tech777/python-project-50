from gendiff.scripts.comparator import add_moved_from_file1


def test_add_moved():
    list_1 = [('mark', 2), ('bobby', '3'), ('rohith', 4), ('ganesh', 5),
              ('pro', 6)]
    res_list = [('mark', 2), ('rohith', 4), ('ganesh', 5)]
    assert add_moved_from_file1(list_1, res_list) == [('mark', 2),
                    ('bobby', '3'), ('rohith', 4), ('ganesh', 5), ('pro', 6)]


def test_add_no_move():
    list01 = [('bobby', '3'), ('rohith', 4), ('ganesh', 5)]
    res_list1 = [('bobby', '3'), ('rohith', 4), ('ganesh', 5),
                 ('timeout', 202)]
    assert add_moved_from_file1(list01, res_list1) == [('bobby', '3'),
                       ('rohith', 4), ('ganesh', 5), ('timeout', 202)]
