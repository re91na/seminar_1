# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти от 1 до 4: '))
if 1<=num<=4:
    if num==1:
        x = 'x > 0'
        y = 'y > 0'
    elif num==2:
        x = 'x < 0'
        y = 'y > 0'
    elif num==3:
        x = 'x < 0'
        y = 'y < 0'
    else:
        x = 'x > 0'
        y = 'y < 0'        
    print(f'В {num} четверти {x}, а {y}')
