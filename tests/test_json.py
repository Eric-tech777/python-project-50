from gendiff.formaters.json import make_json


def test_json():
    data_frame = {'  roster1': {'  player0': {
        '  firstname': 'Tyrod', '- lastname': 'Taylor', '- sport': 'NFL',
        '+ sports': 'NFL'},
        '  player1': {'  firstname': 'Lamar', '- lastname': 'Miller',
                      '- sport': 'NFL', '+ sport': 'NFLO',
                      '+ surname': 'Miller'}}, '  roster2': {
        '  player0': {'- firstname': 'Carson', '+ firstname': 'Carlson',
                      '  lastname': 'Palmer', '  sport': 'NFL'},
        '- player1': {'firstname': 'David', 'lastname': 'Johnson',
                      'sport': 'NFL'}, '+ toto': {
            'company': 'Davidoff', 'lastname': 'Johnson', 'sport': 'NFL'}}}

    master_file = """{
    "  roster1": {
        "  player0": {
            "  firstname": "Tyrod",
            "- lastname": "Taylor",
            "- sport": "NFL",
            "+ sports": "NFL"
        },
        "  player1": {
            "  firstname": "Lamar",
            "- lastname": "Miller",
            "- sport": "NFL",
            "+ sport": "NFLO",
            "+ surname": "Miller"
        }
    },
    "  roster2": {
        "  player0": {
            "- firstname": "Carson",
            "+ firstname": "Carlson",
            "  lastname": "Palmer",
            "  sport": "NFL"
        },
        "- player1": {
            "firstname": "David",
            "lastname": "Johnson",
            "sport": "NFL"
        },
        "+ toto": {
            "company": "Davidoff",
            "lastname": "Johnson",
            "sport": "NFL"
        }
    }
}"""
    assert make_json(data_frame) == master_file
