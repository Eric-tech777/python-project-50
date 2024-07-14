def plain(ini_dict):
    keys_list = get_keys_list(ini_dict)
    values_list = get_list_of_values(ini_dict)
    keys_value_list = get_key_value(ini_dict)
    row_paths_list = run_getpath(ini_dict, keys_value_list)
    gen_paths_list = get_gen_path_list(row_paths_list)
    fin_paths_list = fix_paths_list(gen_paths_list)
    list_to_sort = merge_list_to_sort(keys_list, fin_paths_list, values_list)
    frame = get_data_frame(list_to_sort)
    string_to_print = '\n'.join(fix_frame(frame))
    return string_to_print


# Получить выборку ключей с изменениями (+/-)
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


# Получить значения для ключей с изменениями
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


key_value_list = []


def get_key_value(some_dict):
    for keys, value in some_dict.items():
        if isinstance(value, dict):
            if keys[0:2] in ['+ ', '- ']:
                key_value_list.append((keys, value))
            get_key_value(value)
        else:
            if keys[0:2] in ['+ ', '- ']:
                key_value_list.append((keys, value))
    return key_value_list


def getpath(nested_dict, search_value):
    for key, value in nested_dict.items():
        if (key, value) == search_value:
            return [key]
        if type(nested_dict[key]) is dict:
            path = getpath(nested_dict[key], search_value)
            if path is not None:
                return [key] + path
    return None


def run_getpath(some_dict, k_v_list):
    row_paths_list = []
    for k in k_v_list:
        row_paths_list.append(getpath(some_dict, k))
    return row_paths_list


def get_gen_path_list(row_paths_list):
    gen_paths_list = []
    for i in row_paths_list:
        gen_paths_list.append('.'.join(i))
    return gen_paths_list


# Очистка путей от маркировки (+/-)
def fix_paths_list(paths_list):
    fin_paths_list = []
    for row in paths_list:
        row1 = row.split(".")
        row2 = [i.strip(" +-") for i in row1]
        fin_row = ".".join(row2)
        fin_paths_list.append(fin_row)
    return fin_paths_list


# Получить сводную выборку - ключ, путь, значение для сортировки
def merge_list_to_sort(list_keys, list_of_paths, list_values):
    merged_list = [(list_keys[i], list_of_paths[i], list_values[i])
                   for i in range(0, len(list_keys))]

    return merged_list


# Получить строки с указанием характера изменений ключей
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


# Приведение bool значений в соответствие с требованием к проекту
def fix_frame(frame0):
    frame1 = [x.replace("'False'", "false") for x in frame0]
    frame2 = [x.replace("'None'", "null") for x in frame1]
    frame3 = [x.replace("'True'", "true") for x in frame2]
    fin_frame = [x.replace("'0'", '0') for x in frame3]
    return fin_frame
