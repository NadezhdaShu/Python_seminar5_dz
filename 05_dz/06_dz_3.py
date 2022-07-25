#Напишите программу, кот принимает на вход число N и выдает последовательность из N членов

# для н = 5: 1, -3, 9, -27, 81 (умножить на -3)

number = int(input('введите число n - '))

def list_from(number):
    list_numbers = []
    f = [list_numbers.append((-3) ** x) for x in range (0, number)]  # тут сократила код благодаря новым знаниям :)
    return list_numbers

print(list_from(number))
