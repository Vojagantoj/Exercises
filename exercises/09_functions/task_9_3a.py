# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
                if len(line) > 2 and line[-1] == 'access':
                    line1 = line
                elif len(line) > 2 and line[-2] == 'vlan' and line[1] == 'access':
                    k = int(line[-1])
                    m = dict([(j,k)])
                    h.update(m)
                    line1 = [1]
                    continue
                elif len(line) > 2 and line[-2] == 'vlan' and line[1] == 'trunk':
                    k = line[-1]
                    sh = k.split(',')
                    i = 0
                    while i < len(sh):
                        sh[i] = int(sh[i])
                        i += 1
                    m = dict([(j,sh)])
                    t.update(m)
                    continue
                elif len(line) >= 2 and line[0] == 'duplex' and line1[-1] == 'access':
                    m = dict([(j,1)])
                    h.update(m)
                    line1 = [1]
    result = []
    result.append(h)
    result.append(t)
    result = tuple(result)
    return result
print(get_int_vlan_map('config_sw2.txt'))