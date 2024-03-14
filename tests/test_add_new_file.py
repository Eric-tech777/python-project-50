from gendiff.scripts.gendiff import add_new_to_file2

def test_add_new_files():
    list_2 = [('mark', 2), ('bobby', '3'), ('rohith', 4), ('ganesh', 5), ('pro', 6)]
    res_list = [('mark', 2), ('rohith', 4), ('ganesh', 5)]
    assert add_new_to_file2(list_2, res_list) == [('mark', 2), ('bobby', '3'), ('rohith', 4), ('ganesh', 5), ('pro', 6)]

  
def test_no_new_files():
    list02 = [('bobby', '2'), ('rohith', 3), ('ganesh', 4)]
    res_list1 = [('bobby', '2'), ('rohith', 3), ('ganesh', 4), ('timeout', 5)]
    assert add_new_to_file2(list02, res_list1) == [('bobby', '2'), ('rohith', 3), ('ganesh', 4), ('timeout', 5)]

