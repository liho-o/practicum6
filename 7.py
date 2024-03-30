"""
Служба доставки предлагает суши в коробочках по пять и по семь штук.
Напишите программу, которая определяет можно ли заказать K штук?
"""

k = int(input('Введите количество суши: '))


def check_s(k):
    if k % 7 == 0:
        print('da')
        return
    elif k % 5 == 0:
        print('da')
        return

    while k > 0:
        k -= 5
        if k % 7 == 0:
            print('da')
            return
        elif k % 5 == 0:
            print('da')
            return
    print('net')


check_s(k)
