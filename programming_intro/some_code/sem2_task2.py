from random import randrange
arr = [randrange(10) for i in range(randrange(3, 10))]
i = 0
size = len(arr)
print(arr)
while i <= size // 2 - 1:
    arr[i], arr[size - i - 1] = arr[size - i - 1], arr[i]
    i += 1
print(arr)