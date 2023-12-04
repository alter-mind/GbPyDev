from random import randrange

arr = [randrange(100) for i in range(randrange(10, 30))]
el_max = arr[0]
el_min = arr[0]
i_max = 0
i_min = 0
i = 0
summa = 0
while i < len(arr) - 1:
    if el_max < arr[i + 1]:
        el_max = arr[i + 1]
        i_max = i + 1
    if el_min > arr[i + 1]:
        el_min = arr[i + 1]
        i_min = i + 1
    i += 1
print(arr)
print(f'max index: {i_max}, min index: {i_min}')
step = 1 if i_min < i_max else -1
i = i_min
while not i == i_max + step:
    summa += arr[i]
    i += step
print(f'sum between min and max elements: {summa}')
