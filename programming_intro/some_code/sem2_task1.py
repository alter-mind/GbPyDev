from random import randrange
arr = [randrange(100) for i in range(randrange(10, 30))]
'''
В первых двух строчках мы импортировали функцию из модуля random и сгенерировали список случайной длины (в дипазоне от 
10 до 30) из случайных элементов (в диапазоне от 0 до 100)
'''
el_max = arr[0]
el_min = arr[0]
i_max = 0
i_min = 0
i = 0
while i < len(arr) - 1:
    if el_max < arr[i+1]:
        el_max = arr[i+1]
        i_max = i + 1
    if el_min > arr[i+1]:
        el_min = arr[i+1]
        i_min = i + 1
    i += 1
print(arr)
print(f'max index: {i_max}, min index: {i_min}')