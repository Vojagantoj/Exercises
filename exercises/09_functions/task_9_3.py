# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    h = {}
    t = {}
    with open(config_filename) as f:
        for line in f:
            if line.startswith('interface'):
                line = line.split()
                j = line[1]
                continue
            else:
                line = line.split()
                if len(line) > 2 and line[-2] == 'vlan' and line[1] == 'access':
                    k = int(line[-1])
                    m = dict([(j,k)])
                    h.update(m)
                elif len(line) > 2 and line[-2] == 'vlan' and line[1] == 'trunk':
                    k = line[-1]
                    sh = k.split(',')
                    i = 0
                    while i < len(sh):
                        sh[i] = int(sh[i])
                        i += 1
                    m = dict([(j,sh)])
                    t.update(m)
    result = []
    result.append(h)
    result.append(t)
    result = tuple(result)
    return result
print(get_int_vlan_map('config_sw1.txt'))




#


#        while i < len(line):
#            print('{:22}{}'.format(parametr[i], line[i].strip('[]').strip(',')))
#            i += 1