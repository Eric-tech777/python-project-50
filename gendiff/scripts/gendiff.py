#!/usr/bin/env python3
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration\
    files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument("-f ", "--format", help='set format of output')
    args = parser.parse_args()

    # вызов функции generate_diff с передачей адресов файлов
    generate_diff(args.first_file, args.second_file)


# вывод словаря1 и словаря2 по результату получения путей к файлу1 и файлу2
def generate_diff(path_file1, path_file2):
    dict1, dict2 = make_dicts(path_file1, path_file2)
    list1, list2 = make_sorted_lists(dict1, dict2)
    res_list = add_twins(list1, list2)
    res1_list = add_same_keys(res_list, list1, list2)
    res2_list = add_moved_from_file1(res1_list, list1)
    res3_list = add_new_to_file2(res2_list, list2)
    sorted_result_list = sort_result_list(res3_list)
    result_string = tip_out(sorted_result_list, list1, list2)
    return result_string


def make_dicts(path1, path2):
    dict1 = json.load(open(path1))
    dict2 = json.load(open(path2))
    return dict1, dict2


# получение отсортированных списков кортежей с данными из файла1 и файла2
def make_sorted_lists(dict1, dict2):
    sorted_list1 = sorted(dict1.items(), key=lambda x: x[0])
    sorted_list2 = sorted(dict2.items(), key=lambda x: x[0])
    return sorted_list1, sorted_list2


def add_twins(list1, list2):  # вносим в список одинаковые кортежи
    res_list = []
    [res_list.append(i) for i in list1 for j in list2 if i == j]
    return res_list


# вносим в список кортежи с измененным значением
def add_same_keys(res_list, list1, list2):
    for i in list1:
        for j in list2:
            if i[0] == j[0] and i[1] != j[1]:
                res_list.append(i)
                res_list.append(j)

    return res_list


# вносим в список кортежи сo значениями удаленными из файла1
def add_moved_from_file1(res1_list, list1):
    [res1_list.append(i) for i in list1 if i in list1 and i not in res1_list]
    return res1_list


# вносим в список кортежи с новыми значениями (добавленными элементами)
def add_new_to_file2(res2_list, list2):
    [res2_list.append(j) for j in list2 if j in list2 and j not in res2_list]
    return res2_list


# сортировка списка элементов для формирования отчета
def sort_result_list(result_list):
    sorted_result_list = sorted(result_list, key=lambda elem: elem[0])
    return sorted_result_list


# формирование отчета по разнице файлов
def tip_out(sorted_result_list, list1, list2):
    def get_mark(item):  # получить знак статуса элементов (' ', '-', '+')
        mark = '0'
        if item in list1 and item in list2:
            mark = ' '
        if item in list1 and item not in list2:
            mark = '-'
        if item in list2 and item not in list1:
            mark = '+'
        return mark

# генератор отчета по каждому элементу для отчета
    string_to_join = [f'  {get_mark(item)} {item[0]}:\
 {str(item[1]).lower()}\n' for item in sorted_result_list]
# сбор отчета для вывода на печать
    result = f"{{\n{''.join(string_to_join)}}}"
    return result


if __name__ == "__main__":
    main()
