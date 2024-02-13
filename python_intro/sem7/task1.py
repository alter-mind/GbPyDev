"""
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента
функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции
умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
"""


def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print('\n'.join([' '.join([str(operation(row, column)) for column in range(1, num_columns + 1)])
                         for row in range(1, num_rows + 1)]))


print_operation_table(lambda x, y: x * y, 4, 5)
