# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input("Введите k = "))
itog_list = [0] * (k * 2 + 1)

for i in range(k + 1):
    if i == 0:
        continue
    elif i == 1:
        itog_list[k + i] = 1
        itog_list[k - i] = 1
    else:
        itog_list[k + i] = itog_list[k + i - 1] + itog_list[k + i - 2]
        itog_list[k - i] = itog_list[k - i + 2] - itog_list[k - i + 1]
    
print(itog_list)