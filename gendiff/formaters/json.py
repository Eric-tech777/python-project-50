import json


# Форматер json
def make_json(ini_dict):
    dict_to_json = json.dumps(ini_dict, indent=4)
    return dict_to_json
