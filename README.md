# Проект: Вычислитель отличий

## Описание проекта
Программа, которая определяет разницу между двумя структурами данных (в форматах json yaml) с выводом результата в командной строке. Имеется возможность вывода результата в форматах “stylish” (по умолчанию), “plain text” и “json”.

## Инструкция по установке утилиты
1) В консоли перейти в локальную папку, где планируется разместить пакет с программой.
Установить клон пакета программы из реозитория GitHub:
```bash
gitclonegit@github.com:Eric-tech777/python-project-50.git
```
2) Перейти в директорую проекта:
```bash
cdpython-project-50/
```
3) Активировать виртуальное окружение:
```bash
source .venv/bin/activate
```
4) Развернуть утилиту с помощью Poetry:
```bash
poetry install
```
5) Для определения разницы между двумя файлами необходимо набрать в командной строке команду: gendiff и указать пути до каждого из сравниваемых файлов.
Возможно получение результата в трех форматах:
- “stylish” (по умолчанию), команда: **gendiff file1.json file2.json**
C помощью дополнительной опции (-f или --format):
- “plain text”, команда:  **gendiff -f plain file1.json file2.json**
- “json”, команда: **gendiff -f json file1.yml file2.yml**

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Eric-tech777/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Eric-tech777/python-project-50/actions)
[![asciicast](https://asciinema.org/a/k6wASgXXksXP8fTweq7EeZUEY.svg)](https://asciinema.org/a/k6wASgXXksXP8fTweq7EeZUEY)
[![Maintainability](https://api.codeclimate.com/v1/badges/957f4c9a0d7cf059a926/maintainability)](https://codeclimate.com/github/Eric-tech777/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/957f4c9a0d7cf059a926/test_coverage)](https://codeclimate.com/github/Eric-tech777/python-project-50/test_coverage)
[![asciicast](https://asciinema.org/a/KEzkz2aKeiYyMfaW9TugRfeYQ.svg)](https://asciinema.org/a/KEzkz2aKeiYyMfaW9TugRfeYQ)
[![asciicast](https://asciinema.org/a/rMCQGGqVO7AILHynWd5YsZ5RR.svg)](https://asciinema.org/a/rMCQGGqVO7AILHynWd5YsZ5RR)
[![asciicast](https://asciinema.org/a/UxC11cNyFUlzQ85SUBp44jEpd.svg)](https://asciinema.org/a/UxC11cNyFUlzQ85SUBp44jEpd)
[![asciicast](https://asciinema.org/a/MafiMsW3xG2dBkot10TxSLDVV.svg)](https://asciinema.org/a/MafiMsW3xG2dBkot10TxSLDVV)





