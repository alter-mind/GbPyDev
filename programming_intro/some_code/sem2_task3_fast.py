from random import randrange
arr = [randrange(100) for i in range(randrange(10, 30))]
print(arr)
start = arr.index(min(arr))
stop = arr.index(max(arr))
if stop < start:
    start, stop = stop, start
print(f'Сумма между элементов, лежащих на отрезке между максимумом и минимумом: {sum(arr[start:stop + 1])}')
# print(f'max index: {arr.index(max(arr))}, min index: {arr.index(min(arr))}')
'''
Находим сумму элементов соответствующего среза
'''
