# Задание №1
# Предлагаем пользователю ввести два числа
n = int(input('Введите первое положительное число: '))
m = int(input('Введите второе положительное число: '))
# Инициализируем переменную d меньшим из чисел n и m
d = min(n, m)
# Пока остаток от деления не равен нулю, уменьшаем делитель
while n % d != 0 or m % d != 0:
    d = d - 1

print(d, 'наибольший общий делитель')

# Задание №2
# Предлагаем пользователю ввести положительное число
n = int(input('Введите целое число (2 или больше): '))
# Простые множители представляем ввиде списка
list_factor = []
factor = 2

while factor <= n:
    if n % factor == 0:
        n = n / 2
        list_factor.append(factor)
    else:
        factor += 1
print('Простые множители числа: ', list_factor)

# Задание №3
# Предлагаем пользователю ввести число в двоичном виде
number = str(input('Введите число в двоичном виде: '))
number = list(str(number))
length = len(number)
num = 0

for i in range(0, length):
    num += int(number[i]) * (2 ** (length - i - 1))

print('Десятичное число: ', num)

# Задание №4
# Предлагаем пользователю ввести целое число
q = int(input('Введите целое число: '))
# Инициируем переменную как пустую строку
result = ' '

while q > 0:
    r = q % 2
    result = str(r) + result
    q = q // 2

print('Двоичное представление исходного числа: ', result)

# Задание №5
# Импортируем модуль random в программу
import random
from  random import randrange

numbers = 100
max_num = randrange(1, numbers + 1)
new_num = 0

for i in range(1, numbers):
    current = randrange(1, numbers + 1)
    if current > max_num:
        max_num = current
        new_num = new_num + 1
        print(current, 'обновление')
    else:
        print(current)

print('Максимальное число в ряду: ', max_num)
print('Количество смен максимального числа: ', new_num)
