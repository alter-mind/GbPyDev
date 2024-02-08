"""
Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет
задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
"""

# a1 = 2
# d = 3
# n = 4

progression = [a1 + (el - 1) * d for el in range(1, n + 1)]
# Условие задачи или автотесты gb не корректны - нужно дополнительно построчно вывести результат.
for el in progression:
    print(el)