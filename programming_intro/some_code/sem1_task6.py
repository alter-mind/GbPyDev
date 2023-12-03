n = int(input())
counter = 1
factorial = 1
while counter <= n:
    factorial *= counter
    counter += 1
print(f'factorial = {factorial}')