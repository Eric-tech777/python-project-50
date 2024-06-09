#!/usr/bin/env python3
import argparse


def path_parser():  # парсинг путей к файлам и указание форматера по умолчанию
    # создание парсера
    parser = argparse.ArgumentParser(description='Compares two configuration\
    files and shows a difference.')

    # добавление аргументов
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    # аргумент после опции "-f", если не будет указан, будет по умолчанию
    # иметь значение "stylish"
    parser.add_argument("-f", "--format", type=str,
                        default="stylish", help='set format of output')

    # переменная args содержит все аргументы которые были переданы скрипту
    args = parser.parse_args()
    return args
