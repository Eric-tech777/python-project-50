import json


def data_parser(dict1, dict2):
    data1 = comparator(dict1, dict2)
    data2 = order_dict(data1)
    result_string = stylish(data2, count_space=4)
    print(result_string)
    return result_string


def comparator(dict1, dict2):
    the_same = (list(dict1.keys() & dict2.keys()))
    removed = (list(dict1.keys() - dict2.keys()))
    added = (list(dict2.keys() - dict1.keys()))
    result = {}
    for i in the_same:
        if dict1[i] == dict2[i]:
            result["  " + i] = str(dict1[i])
    for i in the_same:
        if dict1[i] != dict2[i]:
            if isinstance(dict1[i], dict) and isinstance(dict2[i], dict):
                result["  " + i] = comparator(dict1[i], dict2[i])
            else:
                result["- " + i] = dict1[i]
                result["+ " + i] = dict2[i]
    for i in added:
        result["+ " + i] = dict2[i]
    for i in removed:
        result["- " + i] = dict1[i]
    return result


# Получение Отсортированного представления для Форматера
def order_dict(d):
    result = {}
    for key, val in sorted(d.items(), key=lambda x: x[0].strip(" -+")):
        if isinstance(val, dict):
            result[key] = order_dict(val)
        else:
            result[key] = val
    return result


# Форматер stylish
def stylish(data2, replacer=' ', count_space=1, rank=1):
    if isinstance(data2, dict):
        result = '{\n'
        for elem, value in data2.items():
            if elem[0:2] in ['+ ', '- ', '  ']:
                some = 2
            else:
                some = 0
            if value == 'False':
                value = json.dumps(False)
            if value == 'None':
                value = json.dumps(None)
            if value == 'True':
                value = json.dumps(True)
            result += f'{replacer * (count_space * rank - some)}{elem}: '
            result += stylish(value, replacer, count_space, rank + 1) + '\n'
        result += replacer * count_space * (rank - 1) + '}'
    else:
        result = str(data2)
    return result
