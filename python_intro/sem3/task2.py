'''
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его
'''
# from random import randint
# list_1 = [randint(1, 10) for el in range(randint(10, 20))]
# k = randint(1, 10)
# print(list_1, k)
dev = abs(list_1[0] - k)
element = list_1[0]
for num in list_1[1:]:
    current_dev = abs(num - k)
    if current_dev < dev:
        dev = current_dev
        element = num
print(element)