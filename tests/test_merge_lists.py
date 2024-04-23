from gendiff.formaters.plain import merge_list_to_sort


def test_merge_list_to_sort():
    list_keys = [
        '- lastname', '- sport', '+ sports', '- lastname', '- sport',
        '+ sport', '+ surname', '- firstname', '+ firstname', '- player1',
        '+ toto']
    list_of_paths = [
        'roster1.player1.lastname', 'roster1.player1.sport',
        'roster1.player0.sports', 'roster1.player1.lastname',
        'roster1.player1.sport', 'roster1.player1.sport',
        'roster1.player1.surname', 'roster2.player0.firstname',
        'roster2.player0.firstname', 'roster2.player1', 'roster2.toto']
    list_values = [
        'Taylor', 'NFL', 'NFL', 'Miller', 'NFL', 'NFLO', 'Miller', 'Carson',
        'Carlson', {'firstname': 'David', 'lastname': 'Johnson',
                    'sport': 'NFL'}, {'company': 'Davidoff',
                                      'lastname': 'Johnson', 'sport': 'NFL'}]
    assert merge_list_to_sort(list_keys, list_of_paths, list_values) == [
        ('- lastname', 'roster1.player1.lastname', 'Taylor'),
        ('- sport', 'roster1.player1.sport', 'NFL'),
        ('+ sports', 'roster1.player0.sports', 'NFL'),
        ('- lastname', 'roster1.player1.lastname', 'Miller'),
        ('- sport', 'roster1.player1.sport', 'NFL'),
        ('+ sport', 'roster1.player1.sport', 'NFLO'),
        ('+ surname', 'roster1.player1.surname', 'Miller'),
        ('- firstname', 'roster2.player0.firstname', 'Carson'),
        ('+ firstname', 'roster2.player0.firstname', 'Carlson'),
        ('- player1', 'roster2.player1', {
            'firstname': 'David', 'lastname': 'Johnson', 'sport': 'NFL'}),
        ('+ toto', 'roster2.toto', {'company': 'Davidoff',
                                    'lastname': 'Johnson', 'sport': 'NFL'})]
