from gendiff.formaters.plain import get_paths


def test_find_paths():
    ini_dict = {'  roster1': {'  player0': {
        '  firstname': 'Tyrod', '- lastname': 'Taylor', '- sport': 'NFL',
        '+ sports': 'NFL'}, '  player1': {
        '  firstname': 'Lamar', '- lastname': 'Miller', '- sport': 'NFL',
        '+ sport': 'NFLO', '+ surname': 'Miller'}}, '  roster2': {
        '  player0': {'- firstname': 'Carson', '+ firstname': 'Carlson',
                      '  lastname': 'Palmer', '  sport': 'NFL'},
        '- player1': {'firstname': 'David', 'lastname': 'Johnson',
                      'sport': 'NFL'}, '+ toto': {'company': 'Davidoff',
                                                  'lastname': 'Johnson',
                                                  'sport': 'NFL'}}}
    keys_list = ['- lastname', '- sport', '+ sports', '- lastname',
                 '- sport', '+ sport', '+ surname', '- firstname',
                 '+ firstname', '- player1', '+ toto']

    assert get_paths(ini_dict, keys_list) == [
        '  roster1.  player1.- lastname', '  roster1.  player1.- sport',
        '  roster1.  player0.+ sports', '  roster1.  player1.- lastname',
        '  roster1.  player1.- sport', '  roster1.  player1.+ sport',
        '  roster1.  player1.+ surname', '  roster2.  player0.- firstname',
        '  roster2.  player0.+ firstname', '  roster2.- player1',
        '  roster2.+ toto']
