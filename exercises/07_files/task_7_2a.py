# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

f = open(argv[1])
p = f.read().split('\n')
i = 0
j = 0
k = len(p)
while i < k:
    for  j in range(3):
        if ignore[j] in p[i]:
            p.remove(p[i])
            i -= 1
            break
    i += 1
    k = len(p)
i = 0
while i < len(p):
    if p[i] != '!' and p[i].startswith('!') == False:
        print(p[i])
        i+=1
    else:
        i+=1