# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

N = int(input('Введите количество элементов массива N: '))

print('Введите массив: ')
A = [int(i) for i in input().split()]

X = int(input('Введите число X: '))

B = A.count(X)
print('Число X в массиве встречается', B, 'раз')