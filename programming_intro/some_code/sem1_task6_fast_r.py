factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)  # обзывать labmda плохо
print(f'factorial = {factorial(int(input()))}')
