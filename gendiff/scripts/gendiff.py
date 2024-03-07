#!/usr/bin/env python3
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument("-f ", "--format", help='set format of output')
    args = parser.parse_args()
    # print(args.first_file)
    # print(args.second_file)
    
'''
def generate_diff(path1, path2):
    dict1 = json.load(open(path1))
    sorted_list1 = sorted(dict1.items(), key=lambda x: x[0])

    dict2 = json.load(open(path2))
    sorted_list2 = sorted(dict2.items(), key=lambda x: x[0])

    list3 = []
    for i in sorted_list1:
        for j in sorted_list2:
            if i == j:
                list3.append(i)
            if i[0] == j[0] and i[1] != j[1]:
                list3.append(i)
                list3.append(j)

    for i in sorted_list1:
        if i not in list3:
            list3.append(i)

    for j in sorted_list2:
        if j not in list3:
            list3.append(j)

    sorted_list3 = sorted(list3, key=lambda elem: elem[0])

    def get_mark(item):
        if item in sorted_list1 and item in sorted_list2:
            mark = ' '
        if item in sorted_list1 and item not in sorted_list2:
            mark = '-'
        if item in sorted_list2 and item not in sorted_list1:
            mark = '+'
        return mark

    result_string1 = [f'  {get_mark(item)} {item[0]}: {str(item[1]).lower()}\n' for item in sorted_list3]
    
    return f'{{\n{''.join(result_string1)}}}'


p1 = 'file1.json'
p2 = 'file2.json'

print(generate_diff(p1, p2))
'''

if __name__ == "__main__":
    main()

