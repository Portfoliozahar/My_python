# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

querter = int(input('введите четверть: '))

if querter == 1:
    print('x > 0, y > 0')
elif querter == 2:
    print('x < 0, y > 0')
elif querter == 3:
    print('x < 0, y < 0')
elif querter == 4:
    print('x > 0, y < 0')
else:
    print('error')