from random import randrange
arr = [randrange(100) for i in range(randrange(10, 30))]
summa = 0
i = 0
while i < len(arr):
    summa += arr[i]
    i += 1
mean = summa / len(arr)
print(f'mean: {mean}')