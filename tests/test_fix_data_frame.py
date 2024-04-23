from gendiff.formaters.plain import fix_frame


def test_fix_data_frame():
    frame_to_fix = [
        "Property 'roster1.player1.lastname' was removed",
        "Property 'roster1.player1.sport' was removed",
        "Property 'roster1.player0.sports' was added with value: 'False'",
        "Property 'roster1.player1.lastname' was removed",
        "Property 'roster1.player1.sport' was updated. From 'None' to 'True'",
        "Property 'roster1.player1.surname' was added with value: 'Miller'",
        "Property 'roster2.player0.firstname' was updated."
        " From 'Carson' to 'Carlson'",
        "Property 'roster2.player1' was removed",
        "Property 'roster2.toto' was added with value: [complex value]"]

    assert fix_frame(frame_to_fix) == [
        "Property 'roster1.player1.lastname' was removed",
        "Property 'roster1.player1.sport' was removed",
        "Property 'roster1.player0.sports' was added with value: false",
        "Property 'roster1.player1.lastname' was removed",
        "Property 'roster1.player1.sport' was updated. From null to true",
        "Property 'roster1.player1.surname' was added with value: 'Miller'",
        "Property 'roster2.player0.firstname' was updated."
        " From 'Carson' to 'Carlson'",
        "Property 'roster2.player1' was removed",
        "Property 'roster2.toto' was added with value: [complex value]"]
