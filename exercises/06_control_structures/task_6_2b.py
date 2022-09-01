# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
p = input('Введите адрес в формате x.x.x.x: ')
m = p.split('.')
ip_add = False
i = 0
while not ip_add and i <= 1:
    if (len(m) == 4) and m[0].isdigit() and int(m[0]) <= 255 and m[1].isdigit() and m[2].isdigit() and m[3].isdigit() == True:
        k = int(m[0])
        ip_add = True
        if 1 <= k <= 223:
            m = ('unicast')
        elif 224 <= k <= 239:
            m = ('multicast')
        elif int(m[0]) == int(m[1]) == int(m[2]) == int(m[3]) == 255:
            m = ('local broadcast')
        elif int(m[0]) == int(m[1]) == int(m[2]) == int(m[3]) == 0:
            m = ('unassigned')
        else:
            m = ('unused')
    elif i == 1:
        m = ()
        break
    else:
        print('Неправильный IP-адрес')
        p = input('Введите адрес в формате x.x.x.x: ')
        m = p.split('.')
        i +=1
print(m)