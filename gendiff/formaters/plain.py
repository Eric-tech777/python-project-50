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


def fix_paths_list(path_list):
    fin_paths_list = []
    for row in path_list:
        row1 = row.split(".")
        row2 = [i.strip(" +-") for i in row1]
        fin_row = ".".join(row2)
        fin_paths_list.append(fin_row)
    return fin_paths_list


# Получаем выборку ключ, путь, значение для сортировки
def merge_list_to_sort(list_keys, list_of_paths, list_values):
    merged_list = [(list_keys[i], list_of_paths[i], list_values[i])
                   for i in range(0, len(list_keys))]

    return merged_list


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


def fix_frame(frame0):
    frame1 = [x.replace("'False'", "false") for x in frame0]
    frame2 = [x.replace("'None'", "null") for x in frame1]
    fin_frame = [x.replace("'True'", "true") for x in frame2]
    return fin_frame
