from gendiff.scripts.gendiff import make_json_dicts


def test_json_dicts():
    path_json1 = "file_1.json"
    path_json2 = "file_2.json"
    assert make_json_dicts(path_json1, path_json2) == (
        {'roster1': {'player0': {'sport': 'NFL', 'firstname': 'Tyrod',
                                 'lastname': 'Taylor'},
                     'player1': {'sport': 'NFL', 'firstname': 'Lamar',
                                 'lastname': 'Miller'}},
         'roster2': {'player0': {'sport': 'NFL', 'firstname': 'Carson',
                                 'lastname': 'Palmer'},
                     'player1': {'sport': 'NFL', 'firstname': 'David',
                                 'lastname': 'Johnson'}}},
        {'roster1': {'player0': {'sports': 'NFL', 'firstname': 'Tyrod'},
                     'player1': {'sport': 'NFLO', 'firstname': 'Lamar',
                                 'surname': 'Miller'}},
         'roster2': {'player0': {'sport': 'NFL', 'firstname': 'Carlson',
                                 'lastname': 'Palmer'},
                     'toto': {'sport': 'NFL', 'company': 'Davidoff',
                              'lastname': 'Johnson'}}})
