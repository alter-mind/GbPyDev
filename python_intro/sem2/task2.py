# s = int(input())
# p = int(input())

for x in range(1, p // 2 + 1):
    if (p % x == 0) and (p / x + x == s) and (x <= p / x):
        print(x, int(p / x))
