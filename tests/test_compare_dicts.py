from gendiff.scripts.comparator import comparator


def test_compare_dicts():
    dict_1 = {'roster1': {'player0': {
        'sport': 'NFL', 'firstname': 'Tyrod', 'lastname': 'Taylor'},
        'player1': {'sport': 'NFL', 'firstname': 'Lamar',
                    'lastname': 'Miller'}},
        'roster2': {'player0': {'sport': 'NFL', 'firstname': 'Carson',
                                'lastname': 'Palmer'},
                    'player1': {'sport': 'NFL', 'firstname': 'David',
                                'lastname': 'Johnson'}}}
    dict_2 = {'roster1': {'player0': {'sports': 'NFL', 'firstname': 'Tyrod'},
                          'player1': {'sport': 'NFLO', 'firstname': 'Lamar',
                                      'surname': 'Miller'}},
              'roster2': {'player0': {'sport': 'NFL',
                                      'firstname': 'Carlson',
                                      'lastname': 'Palmer'},
                          'toto': {'sport': 'NFL', 'company': 'Davidoff',
                                   'lastname': 'Johnson'}}}
    assert comparator(dict_1, dict_2) == {
        '  roster2': {
            '  player0': {'  lastname': 'Palmer', '  sport': 'NFL',
                          '- firstname': 'Carson', '+ firstname': 'Carlson'},
            '+ toto': {'sport': 'NFL', 'company': 'Davidoff',
                       'lastname': 'Johnson'},
            '- player1': {'sport': 'NFL', 'firstname': 'David',
                          'lastname': 'Johnson'}},
        '  roster1': {'  player1': {
            '  firstname': 'Lamar', '- sport': 'NFL', '+ sport': 'NFLO',
            '+ surname': 'Miller', '- lastname': 'Miller'}, '  player0': {
            '  firstname': 'Tyrod', '+ sports': 'NFL', '- lastname': 'Taylor',
            '- sport': 'NFL'}}}
