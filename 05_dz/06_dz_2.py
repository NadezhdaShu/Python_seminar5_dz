# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
len_list = math.ceil(len(list)/2)
new_list = []

f = [new_list.append(list[i] * list[-i - 1]) for i in range(len_list)] # тут новые знания к задаче 

print(f"Список:\n {list}") 
print(f"Произведение пар: \r\n {new_list}")
