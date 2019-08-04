"""
Лабораторная работа 1 - домашнее задание
Задание 1 Вариант 13: Мы нашли К грибов в лесу
"""

print("---Задание 1 Вариант 13---")
K = int(input("Введите количество грибов:\n"))

T = divmod(K, 10)
if T[0] == 1:
    s = "грибов"
elif T[1] == 0:
    s = "грибов"
elif T[1] == 1:
    s = "гриб"
elif 1 < T[1] < 5:
    s = "гриба"
else:
    s = "грибов"
print("Мы нашли " + str(K) + " " + s + " в лесу")

# Задание 2 Вариант 13:

print("---Задание 2 Вариант 13---")
import math
import numpy
a = 8
m = 6
b = 5*10**3

print("Исходные данные:")
print("a=" + str(a))
print("m=" + str(m))
print("b=" + str(b))

# for loop
print("--- for loop ---")
list_of_k = [1.6, 9.1, 8]
for k in list_of_k:
    d = math.sin(k/a)/math.cos(m*b)
    c = d/(d**2+1)/(1-math.exp(k))
    print("k=" + str(k) + "  d=" + str(d) + "  c=" + str(c))

# while loop
print("--- while loop ---")
k = a
while (k >= 3):
    d = math.sin(k/a)/math.cos(m*b)
    c = d/(d**2+1)/(1-math.exp(k))
    print("k=" + str(k) + "  d=" + str(d) + "  c=" + str(c))
    k = k - 0.5

# double loop
print("--- double loop ---")
list_of_k = [1.7, 5, -2]
for a in numpy.arange(2.0, 3.0, 0.2):
    for k in list_of_k:
        d = math.sin(k/a)/math.cos(m*b)
        c = d/(d**2+1)/(1-math.exp(k))
        print("a=" + str(a) + " k=" + str(k) + "  d=" + str(d) + "  c=" + str(c))

# Задание 3 Вариант 6:

print("---Задание 3 Вариант 6---")
# ввод
k = int(input("Введите число:\n"))
l = i = 0
while l < k:
    s = str(2**i)
    l = l + len(s)
    i += 1
nn = s[k-l-1]
print(str(k) + "-ая цифра в последовательности степеней двойки: " + nn)

# Задание 4 Вариант 13:

print("---Задание 4 Вариант 13---")
import random
# ввод
n = int(input("Введите размер списка:\n"))
A = []
B = []
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)
print("Исходный список: " )
print(A)
B.append(0)
i = 1
while i < n:
    sm = sum(A[0:i])
    B.append(sm)
    i += 1
print("Новый список- суммы предыдущих элементов: " )
print(B)


