import json


# Форматер stylish
def stylish(ini_dict, replacer=' ', count_space=4, rank=1):
    if isinstance(ini_dict, dict):
        result = '{\n'
        for elem, value in ini_dict.items():
            if elem[0:2] in ['+ ', '- ', '  ']:
                some = 2
            else:
                some = 0
            if value is False:
                value = json.dumps(False)
            if value is None:
                value = json.dumps(None)
            if value is True:
                value = json.dumps(True)
            result += f'{replacer * (count_space * rank - some)}{elem}: '
            result += stylish(value, replacer, count_space, rank + 1) + '\n'
        result += replacer * count_space * (rank - 1) + '}'
    else:
        result = str(ini_dict)

    return result
