"""
Напишите программу, определяющую цвет клетки шахматного поля.
"""

coordinates = input('Введите координаты шахматной клетки: ')
number = int(coordinates[1])


def converter(letter):
    match letter:
        case 'a':
            value = 1
        case 'b':
            value = 2
        case 'c':
            value = 3
        case 'd':
            value = 4
        case 'e':
            value = 5
        case 'f':
            value = 6
        case 'g':
            value = 7
        case 'h':
            value = 8
        case _:
            value = 'eror'
    return value


letter = converter(coordinates[0])
if letter == 'eror' or number > 8:
    print('ERROR')
elif (number % 2 == 0 and letter % 2 == 0) or (number % 2 != 0 and letter % 2 != 0):
    print('черный')
else:
    print('белый')
