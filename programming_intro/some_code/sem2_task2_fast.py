from random import randrange
arr = [randrange(10) for i in range(randrange(3, 10))]
print(arr)
print(arr[::-1])
'''
Это решение берёт срез массива целиком в обратном порядке. 
'''