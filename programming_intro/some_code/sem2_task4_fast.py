from random import randrange
arr = [randrange(100) for i in range(randrange(10, 30))]

print(f'mean: {sum(arr) / len(arr)}')