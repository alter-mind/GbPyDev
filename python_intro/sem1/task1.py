'''
Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res.
'''
n = int(input())
res = sum([int(el) for el in str(n)])
print(res)