from gendiff.formaters.plain import fix_paths_list


def test_fix_paths():
    paths_list = ['  roster1.  player1.- lastname', 'roster1.  player1.- '
                                                    'sport', '  roster1.  '
                                                             'player0.+ '
                                                             'sports',
                  '  roster1.  player1.- lastname', '  roster1.  player1.- '
                                                    'sport', '  roster1.  '
                                                             'player1.+ '
                                                             'sport',
                  '  roster1.  player1.+ surname', '  roster2.  player0.- '
                                                   'firstname', '  roster2.  '
                                                                'player0.+ '
                                                                'firstname',
                  '  roster2.- player1', '  roster2.+ toto']

    assert fix_paths_list(paths_list) == [
        'roster1.player1.lastname', 'roster1.player1.sport', 'roster1'
                                                             '.player0.sports',
        'roster1.player1.lastname', 'roster1.player1.sport',
        'roster1.player1.sport', 'roster1.player1.surname',
        'roster2.player0.firstname', 'roster2.player0.firstname',
        'roster2.player1', 'roster2.toto']
