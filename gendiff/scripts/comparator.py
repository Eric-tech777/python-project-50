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
