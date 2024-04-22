from gendiff.formaters.plain import get_keys_list


def test_order_diff():
    ini_dict = {'  roster1': {'  player0': {'  firstname': 'Tyrod', '- lastname': 'Taylor', '- sport': 'NFL', '+ sports': 'NFL'}, '  player1': {'  firstname': 'Lamar', '- lastname': 'Miller', '- sport': 'NFL', '+ sport': 'NFLO', '+ surname': 'Miller'}}, '  roster2': {'  player0': {'- firstname': 'Carson', '+ firstname': 'Carlson', '  lastname': 'Palmer', '  sport': 'NFL'}, '- player1': {'firstname': 'David', 'lastname': 'Johnson', 'sport': 'NFL'}, '+ toto': {'company': 'Davidoff', 'lastname': 'Johnson', 'sport': 'NFL'}}}

    assert get_keys_list(ini_dict) == ['- lastname', '- sport', '+ sports', '- lastname', '- sport', '+ sport', '+ surname', '- firstname', '+ firstname', '- player1', '+ toto']

