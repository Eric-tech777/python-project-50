from gendiff.scripts.gendiff import add_twins


def test_add_twin():
    list1 = [('form', True), ('proxy', '123.234.53.22'), ('title', '')]
    list2 = [('form', True), ('timeout', 20), ('title', '')]
    assert add_twins(list1, list2) == [('form', True), ('title', '')] 

  
def test_add_equal():
    list01 = [('proxy', '123.234.53.22'), ('title', '')]
    list02 = [('timeout', 20), ('title', 'foo')]
    assert add_twins(list01, list02) == []
