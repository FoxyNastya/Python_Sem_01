# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


a = input("Введите любое трехзначное число: ")
sum = 0
for i in a:
    sum += int(i)
    print(sum)
# Второе решение
b = int(input("Введите любое трехзначное число: "))
c = b % 10
d = b // 10 % 10
f = b // 100
sum = f + d + c
print(f'Сумма цифр числа {b}, а именно: {f}, {d}, {c}, составит {sum}')
