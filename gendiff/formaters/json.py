import json


# Форматер json
def make_json(diff_dict):
    dict_to_json = json.dumps(diff_dict, indent=4)
    return dict_to_json
