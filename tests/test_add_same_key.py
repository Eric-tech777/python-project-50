from gendiff.scripts.comparator import add_same_keys


def test_add_same_key():
    list_earlier = []
    list_1 = [('mark', False), ('proxy', '123.23'), ("owner", 'id')]
    list_2 = [('form', True), ('proxy', '123'), ("owner", 'address')]
    assert add_same_keys(list_earlier, list_1, list_2) == [('proxy', '123.23'),
                    ('proxy', '123'), ("owner", 'id'), ("owner", 'address')]


def test_add_same_first():
    list_before = []
    list01 = [('proxy', '123.234.53.22'), ('mark', '')]
    list02 = [('timeout', 202), ('title', 'foo')]
    assert add_same_keys(list_before, list01, list02) == []
