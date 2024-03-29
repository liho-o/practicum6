"""
На цирковой арене радиуса 6,5 метров пытаются разместить ковровую дорожку
(покрытие) размером A x B метров.
Получится ли разместить покрытие без его обрезки или подгибов?
"""

r = 6.5
d = r * 2
p1, p2 = map(int, input('Введите размер дорожки в формате АхВ: ').split('x'))

if d - p1 - p2 >= 0:
    print('да')
else:
    print('нет')
