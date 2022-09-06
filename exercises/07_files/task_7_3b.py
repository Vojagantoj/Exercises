# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
line2 = {}
i = 0
h = 0
with open('CAM_table.txt') as f:
    for line in f:
        line = line.split()
        if len(line) == 0:
            continue
        if line[0].isdigit() == True:
            line.remove('DYNAMIC')
            line[0] = int(line[0])
            k = line[0]
            if k in line2:
                value = line2[k]
                line.remove(line[0])
                value += line
            line.remove(line[0])
            line2.setdefault(k,line)
vlan = int(input('Enter VLAN number: '))
if vlan in line2.keys():
    value = line2[vlan]
    vlan = str(vlan)
h = int(len(value)/2)
if h == 1:
    print('{:9} {:19}{}'.format(vlan, value[0], value[1]))
else:
    while i < 2*h:
        print('{:9} {:19}{}'.format(vlan, value[i], value[i+1]))
        i+= 2
