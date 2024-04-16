from gendiff.scripts.comparator import order_dict


def test_order_diff():
    dict_to_order = {
        '  roster1': {'  player0': {'  firstname': 'Tyrod', '+ sports': 'NFL',
                                    '- lastname': 'Taylor', '- sport': 'NFL'},
                      '  player1': {'  firstname': 'Lamar', '- sport': 'NFL',
                                    '+ sport': 'NFLO', '+ surname': 'Miller',
                                    '- lastname': 'Miller'}},
        '  roster2': {'  player0': {'  lastname': 'Palmer', '  sport': 'NFL',
                                    '- firstname': 'Carson',
                                    '+ firstname': 'Carlson'},
                      '+ toto': {'sport': 'NFL', 'company': 'Davidoff',
                                 'lastname': 'Johnson'},
                      '- player1': {'sport': 'NFL', 'firstname': 'David',
                                    'lastname': 'Johnson'}}}
    assert order_dict(dict_to_order) == {
        '  roster1': {'  player0': {'  firstname': 'Tyrod',
                                    '- lastname': 'Taylor', '- sport': 'NFL',
                                    '+ sports': 'NFL'},
                      '  player1': {'  firstname': 'Lamar',
                                    '- lastname': 'Miller', '- sport': 'NFL',
                                    '+ sport': 'NFLO', '+ surname': 'Miller'}},
        '  roster2': {'  player0': {'- firstname': 'Carson',
                                    '+ firstname': 'Carlson',
                                    '  lastname': 'Palmer', '  sport': 'NFL'},
                      '- player1': {'firstname': 'David',
                                    'lastname': 'Johnson', 'sport': 'NFL'},
                      '+ toto': {'company': 'Davidoff', 'lastname': 'Johnson',
                                 'sport': 'NFL'}}}
