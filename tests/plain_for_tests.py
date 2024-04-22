ini_dict = {'  roster1': {'  player0': {'  firstname': 'Tyrod', '- lastname': 'Taylor', '- sport': 'NFL', '+ sports': 'NFL'}, '  player1': {'  firstname': 'Lamar', '- lastname': 'Miller', '- sport': 'NFL', '+ sport': 'NFLO', '+ surname': 'Miller'}}, '  roster2': {'  player0': {'- firstname': 'Carson', '+ firstname': 'Carlson', '  lastname': 'Palmer', '  sport': 'NFL'}, '- player1': {'firstname': 'David', 'lastname': 'Johnson', 'sport': 'NFL'}, '+ toto': {'company': 'Davidoff', 'lastname': 'Johnson', 'sport': 'NFL'}}}

keys_list = ['- lastname', '- sport', '+ sports', '- lastname', '- sport', '+ sport', '+ surname', '- firstname', '+ firstname', '- player1', '+ toto']

values_list = ['Taylor', 'NFL', 'NFL', 'Miller', 'NFL', 'NFLO', 'Miller', 'Carson', 'Carlson', {'firstname': 'David', 'lastname': 'Johnson', 'sport': 'NFL'}, {'company': 'Davidoff', 'lastname': 'Johnson', 'sport': 'NFL'}]

paths_list = ['  roster1.  player1.- lastname', '  roster1.  player1.- sport', '  roster1.  player0.+ sports', '  roster1.  player1.- lastname', '  roster1.  player1.- sport', '  roster1.  player1.+ sport', '  roster1.  player1.+ surname', '  roster2.  player0.- firstname', '  roster2.  player0.+ firstname', '  roster2.- player1', '  roster2.+ toto']

fixed_paths_list = ['roster1.player1.lastname', 'roster1.player1.sport', 'roster1.player0.sports', 'roster1.player1.lastname', 'roster1.player1.sport', 'roster1.player1.sport', 'roster1.player1.surname', 'roster2.player0.firstname', 'roster2.player0.firstname', 'roster2.player1', 'roster2.toto']

merged_list = [('- lastname', 'roster1.player1.lastname', 'Taylor'), ('- sport', 'roster1.player1.sport', 'NFL'), ('+ sports', 'roster1.player0.sports', 'NFL'), ('- lastname', 'roster1.player1.lastname', 'Miller'), ('- sport', 'roster1.player1.sport', 'NFL'), ('+ sport', 'roster1.player1.sport', 'NFLO'), ('+ surname', 'roster1.player1.surname', 'Miller'), ('- firstname', 'roster2.player0.firstname', 'Carson'), ('+ firstname', 'roster2.player0.firstname', 'Carlson'), ('- player1', 'roster2.player1', {'firstname': 'David', 'lastname': 'Johnson', 'sport': 'NFL'}), ('+ toto', 'roster2.toto', {'company': 'Davidoff', 'lastname': 'Johnson', 'sport': 'NFL'})]

frame_to_fix = ["Property 'roster1.player1.lastname' was removed", "Property 'roster1.player1.sport' was removed", "Property 'roster1.player0.sports' was added with value: 'False'", "Property 'roster1.player1.lastname' was removed", "Property 'roster1.player1.sport' was updated. From 'None' to 'True'", "Property 'roster1.player1.surname' was added with value: 'Miller'", "Property 'roster2.player0.firstname' was updated. From 'Carson' to 'Carlson'", "Property 'roster2.player1' was removed", "Property 'roster2.toto' was added with value: [complex value]"]
fin_fixed_frame = ["Property 'roster1.player1.lastname' was removed", "Property 'roster1.player1.sport' was removed", "Property 'roster1.player0.sports' was added with value: false", "Property 'roster1.player1.lastname' was removed", "Property 'roster1.player1.sport' was updated. From null to true", "Property 'roster1.player1.surname' was added with value: 'Miller'", "Property 'roster2.player0.firstname' was updated. From 'Carson' to 'Carlson'", "Property 'roster2.player1' was removed", "Property 'roster2.toto' was added with value: [complex value]"]

'''
def plain(ini_dict):
    keys_list = get_keys_list(ini_dict)
    values_list = get_list_of_values(ini_dict)
    list_of_paths = get_paths(ini_dict, keys_list)
    fin_paths_list = fix_paths_list(list_of_paths)
    list_to_sort = merge_list_to_sort(keys_list, fin_paths_list, values_list)
    frame = get_data_frame(list_to_sort)
    data_frame = fix_frame(frame)
    for i in data_frame:
        print(i)


# Получить выборку ключей с +/-
list_of_keys = []


def get_keys_list(some_dict):
    for keys, value in some_dict.items():
        if isinstance(value, dict):
            if keys[0:2] in ['+ ', '- ']:
                list_of_keys.append(keys)
            get_keys_list(value)
        else:
            if keys[0:2] in ['+ ', '- ']:
                list_of_keys.append(keys)
    return list_of_keys

print(get_keys_list(ini_dict))


# Получить значения для ключей с +/-
list_of_values = []


def get_list_of_values(some_dict):
    for keys, value in some_dict.items():
        if isinstance(value, dict):
            if keys[0:2] in ['+ ', '- ']:
                list_of_values.append(value)
            get_list_of_values(value)
        else:
            if keys[0:2] in ['+ ', '- ']:
                list_of_values.append(value)
    return list_of_values

print(get_list_of_values(ini_dict))


# Получить путь до ключа (включая сам ключ)
paths_list = []


def find_path(in_dict, key):
    if not isinstance(in_dict, dict):
        return None
    if key in in_dict.keys():
        return key
    resp = None
    for in_dict_key in in_dict.keys():
        rep = find_path(in_dict[in_dict_key], key)
        if rep is None:
            continue
        else:
            resp = "{}.{}".format(in_dict_key, rep)
    return resp


def get_paths(in_dict, k_list):
    for key in k_list:
        paths_list.append(find_path(in_dict, key))
    return paths_list

print(get_paths(ini_dict, keys_list))


def fix_paths_list(path_list):
    fin_paths_list = []
    for row in path_list:
        row1 = row.split(".")
        row2 = [i.strip(" +-") for i in row1]
        fin_row = ".".join(row2)
        fin_paths_list.append(fin_row)
    return fin_paths_list

print(fix_paths_list(paths_list))

# Получаем выборку ключ, путь, значение для сортировки
def merge_list_to_sort(list_keys, list_of_paths, list_values):
    merged_list = [(list_keys[i], list_of_paths[i], list_values[i])
                   for i in range(0, len(list_keys))]

    return merged_list

print(merge_list_to_sort(keys_list, fixed_paths_list, values_list))

def get_data_frame(d):
    frame_of_data = []
    for i in range(len(d)):
        # 1
        if d[i][0][0:2] == '- ' and d[i + 1][0] != '+ ' + d[i][0][2:]:
            frame_of_data.append(f"Property '{d[i][1]}' was removed")
        # 2
        elif d[i][0][0:2] == '- ' and d[i + 1][0] == '+ ' + d[i][0][2:]:
            continue
        # 3
        elif (d[i][0][0:2] == '+ ' and d[i - 1][0] != '- ' + d[i][0][2:]
              and not isinstance(d[i][2], dict)):
            frame_of_data.append(f"Property '{d[i][1]}' was added with value:"
                                 f" '{(d[i][2])}'")

        # 4
        elif (d[i][0][0:2] == '+ ' and d[i - 1][0] != '- ' + d[i][0][2:]
              and isinstance(d[i][2], dict)):
            frame_of_data.append(f"Property '{d[i][1]}' was added with value:"
                                 f" [complex value]")

        # 5
        elif (d[i][0][0:2] == '+ ' and d[i - 1][0] == '- ' + d[i][0][2:]
              and not isinstance(d[i][2], dict) and not isinstance(d[i - 1][2],
                                                                   dict)):
            frame_of_data.append(f"Property '{d[i][1]}' was updated."
                                 f" From '{d[i - 1][2]}' to '{d[i][2]}'")

        # 6
        elif (d[i][0][0:2] == '+ ' and d[i - 1][0] == '- ' + d[i][0][2:]
              and isinstance(d[i][2], dict) and not isinstance(d[i - 1][2],
                                                               dict)):
            frame_of_data.append(f"Property '{d[i][1]}' was updated."
                                 f" From '{d[i - 1][2]}' to [complex value]")

        # 7
        elif (d[i][0][0:2] == '+ ' and d[i - 1][0] == '- ' + d[i][0][2:]
              and not isinstance(d[i][2], dict) and isinstance(d[i - 1][2],
                                                               dict)):
            frame_of_data.append(f"Property '{d[i][1]}' was updated."
                                 f" From [complex value] to '{d[i][2]}'")

        # 8
        elif (d[i][0][0:2] == '+ ' and d[i - 1][0] == '- ' + d[i][0][2:]
              and isinstance(d[i][2], dict) and isinstance(d[i - 1][2], dict)):
            frame_of_data.append(f"Property '{d[i][1]}' was updated."
                                 f" From [complex value] to [complex value]")

    return frame_of_data

print(get_data_frame(merged_list))
'''
def fix_frame(frame0):
    frame1 = [x.replace("'False'", "false") for x in frame0]
    frame2 = [x.replace("'None'", "null") for x in frame1]
    fin_frame = [x.replace("'True'", "true") for x in frame2]
    return fin_frame
print(fix_frame(frame_to_fix))
