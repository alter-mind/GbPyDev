numbers = [2, 5, 13, 7, 6, 4]
size = 6
sum = 0  # переопределять зарезервированные элементы языка плохо
avg = 0
index = 0
while index < size:
    sum += numbers[index]
    index += 1
avg = sum / size
print(avg)