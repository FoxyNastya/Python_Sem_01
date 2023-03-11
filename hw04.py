# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
#Если от шоколадки размером n x m можно отломить k долек, 
# то k должно делиться на n или на m без остатка. 
# Также следует учесть, что при k > n x m программа должна выдать отрицательный ответ (NO).
n = int(input("Введите значение стороны шоколадки n: "))
m = int(input("Введите значение стороны шоколадки m: "))
k = int(input("Введите значение k долек от этой шоколадки: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')