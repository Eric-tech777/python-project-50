from gendiff.formaters.plain import get_list_of_values


def test_get_values():
    ini_dict = {
        '  roster1': {'  player0': {
            '  firstname': 'Tyrod', '- lastname': 'Taylor', '- sport': 'NFL',
            '+ sports': 'NFL'}, '  player1': {
            '  firstname': 'Lamar', '- lastname': 'Miller', '- sport': 'NFL',
            '+ sport': 'NFLO', '+ surname': 'Miller'}}, '  roster2': {
            '  player0': {'- firstname': 'Carson', '+ firstname': 'Carlson',
                          '  lastname': 'Palmer', '  sport': 'NFL'},
            '- player1': {'firstname': 'David', 'lastname': 'Johnson',
                          'sport': 'NFL'}, '+ toto': {
                'company': 'Davidoff', 'lastname': 'Johnson', 'sport': 'NFL'}}}

    assert get_list_of_values(ini_dict) == [
        'Taylor', 'NFL', 'NFL', 'Miller', 'NFL', 'NFLO', 'Miller', 'Carson',
        'Carlson', {'firstname': 'David', 'lastname': 'Johnson',
                    'sport': 'NFL'}, {'company': 'Davidoff',
                                      'lastname': 'Johnson', 'sport': 'NFL'}]
