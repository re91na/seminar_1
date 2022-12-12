# 1) Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#a = int(input('a = '))
#b = int(input('b = '))
# if (a == b**2 or b == a**2):
#    print('да')
# else:
#    print('нет')

# 2) Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = int(input('d = '))
# e = int(input('e = '))
# list = [a,b,c,d,e]
# print(list)
# max = list[0]
# for i in range(len(list)):
#     if list[i] > max:
#         max = list[i]
# print(max)


# max = list[0]
# for i in list:
#     if max < i:
#         max = i
# print(max)

# 3) Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# n = int(input('n = '))
# for i in range(-n, n):
#     print(i, end=', ')
# print(n)


# 4) Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# n = float(input('n = '))
# n = (n*100)//10%10
# if n == 0:
#     print('нет')
# else:
#     print(int(n))

# 5) Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
n = int(input('n = '))
if (n%5==0 and n%10==0 or n%15==0):
    if(n%30!=0):
        print('да')
    else:
        print('нет')
else:
    print('нет')