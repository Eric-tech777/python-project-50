from gendiff.formaters.plain import get_data_frame


def test_get_data_frame():
    merged_list = [
        ('- lastname', 'roster1.player1.lastname', 'Taylor'),
        ('- ''sport', 'roster1.player1.sport', 'NFL'),
        ('+ sports', 'roster1.player0.sports', 'NFL'),
        ('- lastname', 'roster1.player1.lastname', 'Miller'),
        ('- sport', 'roster1.player1.sport', 'NFL'),
        ('+ sport', 'roster1.player1.sport', 'NFLO'),
        ('+ surname', 'roster1.player1.surname', 'Miller'),
        ('- firstname', 'roster2.player0.firstname', 'Carson'),
        ('+ firstname', 'roster2.player0.firstname', 'Carlson'),
        ('- player1', 'roster2.player1', {
            'firstname': 'David', 'lastname': 'Johnson', 'sport': 'NFL'}),
        ('+ toto', 'roster2.toto', {
            'company': 'Davidoff', 'lastname': 'Johnson', 'sport': 'NFL'})]

    assert get_data_frame(merged_list) == [
        "Property 'roster1.player1.lastname' was removed",
        "Property 'roster1.player1.sport' was removed",
        "Property 'roster1.player0.sports' was added with value: 'NFL'",
        "Property 'roster1.player1.lastname' was removed",
        "Property 'roster1.player1.sport' was updated. From 'NFL' to 'NFLO'",
        "Property 'roster1.player1.surname' was added with value: 'Miller'",
        "Property"
        " 'roster2.player0.firstname' was updated. From 'Carson' to 'Carlson'",
        "Property 'roster2.player1' was removed",
        "Property 'roster2.toto' was added with value: [complex value]"]
