# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

a = int(input("Введите 6 цифр вашего возможно счастливого билета: "))
b = a % 10
c = a // 10 % 10
d = a // 100 % 10
f = a // 1000 % 10
g = a // 10000 % 10
h = a // 100000
# print(b)
# print(c)
# print(d)
# print(f)
# print(g)
# print(h)

if (b + c + d) == (f + g + h):
    print("Yes! У вас на руках счастливый билетик, ешьте его")
else:
    print("No, просто едьте по делам")
