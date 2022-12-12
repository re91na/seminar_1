# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# AB = √(xb - xa)2 + (yb - ya)2

xa = int(input('Введите координату х первой точки: '))
ya = int(input('Введите координату y первой точки: '))
xb = int(input('Введите координату х второй точки: '))
yb = int(input('Введите координату y второй точки: '))
ab_distance = round((((xb-xa)**2 + (yb-ya)**2)**(0.5)), 2)
print(ab_distance)