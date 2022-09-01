# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
p = input('Введите адрес в формате x.x.x.x: ')
m = p.split('.')
if (len(m) == 4) and m[0].isdigit() and int(m[0]) <= 255 and m[1].isdigit() and m[2].isdigit() and m[3].isdigit() == True:
    k = int(m[0])
    if 1 <= k <= 223:
        print('unicast')
    elif 224 <= k <= 239:
        print('multicast')
    elif int(m[0]) == int(m[1]) == int(m[2]) == int(m[3]) == 255:
        print('local broadcast')
    elif int(m[0]) == int(m[1]) == int(m[2]) == int(m[3]) == 0:
        print('unassigned')
    else:
        print('unused')
else:
    print('Неправильный IP-адрес')