# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5.61, 10.01]
min_val = int(str(list[0]).split('.')[1])
max_val = int(str(list[0]).split('.')[1])

for i in range(len(list)):
    vrem_val = int(str(list[i]).split('.')[1])
    if(min_val > vrem_val):
        min_val = vrem_val
    if(max_val < vrem_val):
        max_val = vrem_val

print(f"Наибольший: {max_val} \r\nНаименьший: {min_val}")
print(f"Разница между наибольшим и наименьшим: {max_val - min_val}")