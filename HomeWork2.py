"""
Лабораторная работа 2 - домашнее задание
Сравнение алгоритмов сортировки:
- вставками InsertSort
- выбором SelectSort
"""
import random
import datetime
import prettytable                      # пакет для таблицы
import matplotlib.pyplot as plt         # библиотека для графика

def InsertSort(A):                      # сортировка вставками Insert
    for i in range(1, len(A)):
        t = A[i]
        j = i - 1
        while (j >= 0)  and (A[j]>t):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = t


def SelectSort(A):                      # сортировка выбором Select
    for i in range(len(A)-1):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
        A[m], A[i] = A[i], A[m]
# main
table = prettytable.PrettyTable(["Размер списка", "Время InsertSort", "Bремя SelectSort"])
x = []
y1 = []
y2 = []

for N in range(1000,5001,1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    B=A.copy()

    t1 =datetime.datetime.now()
    InsertSort(A)
    t2 =datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    #print("Insert сортировка   " + str(N) + "  заняла   "+str((t2-t1).total_seconds())+"c")

    t3 =datetime.datetime.now()
    SelectSort(B)
    t4 =datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    #print("Select сортировка   " + str(N)+ "  заняла   "+str((t4-t3).total_seconds())+"c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()



