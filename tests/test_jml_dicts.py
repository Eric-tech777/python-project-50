from gendiff.scripts.gendiff import make_yml_dicts


def test_yml_dicts():
    path_yml1 = "file_1.yml"
    path_yml2 = "file_2.yml"
    assert make_yml_dicts(path_yml1, path_yml2) == (
        {'roster1': {'player0': {'sport': 'NFL', 'firstname': 'Tyrod',
                                 'lastname': 'Taylor'}, 'player1': {
            'sport': 'NFL', 'firstname': 'Lamar', 'lastname': 'Miller'}},
         'roster2': {'player0': {'sport': 'NFL', 'firstname': 'Carson',
                                 'lastname': 'Palmer'}, 'player1': {
             'sport': 'NFL', 'firstname': 'David', 'lastname': 'Johnson'}}},
        {'roster1': {'player0': {'sports': 'NFL', 'firstname': 'Tyrod'},
                     'player1': {'sport': 'NFLO', 'firstname': 'Lamar',
                                 'surname': 'Miller'}},
         'roster2': {'player0': {'sport': 'NFL', 'firstname': 'Carlson',
                                 'lastname': 'Palmer'},
                     'toto': {'sport': 'NFL', 'company': 'Davidoff',
                              'lastname': 'Johnson'}}})
