from random import randrange
arr = [randrange(100) for i in range(randrange(10, 30))]
print(arr)
print(f'max index: {arr.index(max(arr))}, min index: {arr.index(min(arr))}')
'''
Тут решение проще, мы пользуемся встроенными функциями max() и min(), и методом list.index(element), который возвращает
индекс элемента
'''