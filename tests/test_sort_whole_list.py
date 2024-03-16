from gendiff.scripts.comparator import sort_result_list


def test_sort_res_list():
    res_list = [('mark', 2), ('bobby', '3'), ('rohith', 4), ('ganesh', 5)]
    assert (sort_result_list(res_list) == [('bobby', '3'), ('ganesh', 5),
                                           ('mark', 2), ('rohith', 4)])
