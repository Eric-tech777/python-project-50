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

### Hexlet tests status:
[![asciicast](https://asciinema.org/a/0Gl8wt7QPPaUbA4asNw4svk5v.svg)](https://asciinema.org/a/0Gl8wt7QPPaUbA4asNw4svk5v)
[![asciicast](https://asciinema.org/a/mkjIbyw6stUpUYR6vhsRBeetx.svg)](https://asciinema.org/a/mkjIbyw6stUpUYR6vhsRBeetx)
[![asciicast](https://asciinema.org/a/mMsEhdvWwcWYu3f9Nnkc4vVE0.svg)](https://asciinema.org/a/mMsEhdvWwcWYu3f9Nnkc4vVE0)






