# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах


# алгоритм сжатия данных, заменяющий повторяющиеся символы (серии) на один символ и число его повторов. 
# Серией называется последовательность, состоящая из нескольких одинаковых символов (для себя)

# textt = 'hhhhmmmmmmmmaaaakkkkkkkkkffffff'

def rle_vhod():
    with open ('05_dz_vhod.txt') as file:
        data = list(map(str.strip, file.readlines()))
    
        result = []
    for line in data:
        simboll = ''
        count = 1
        c_ish = line[0]
        for i in range(1, len(line)):
            new_c = line[i]
            if new_c == c_ish:
                count += 1
            else:
                simboll += c_ish if count == 1 else str(count) + c_ish
                c_ish = line[i]
                count = 1
        simboll += c_ish if count == 1 else str(count) + c_ish           
        result.append(simboll)
    with open('05_dz_vhod.txt', 'w') as file:
        for line in result:
            print(line, file = file)
    return result


def rle_vihod():
    with open ('05_dz_vhod.txt') as file:
        data = list(map(str.strip, file.readlines()))
    result = []
    for line in data:
        simboll = ''
        n = ''
        for c_ish in line:
            if c_ish.isdigit():
                n += c_ish
            else:
                simboll += c_ish if n == '' else int(n) * c_ish
                n = ''
        result.append(simboll)
    with open('05_dz_vhod.txt', 'w') as file:
        for line in result:
            print(line, file = file)
    return result

print('Сжатые данные :')
print(*rle_vhod())

print('Восстановленные данные :')
print(*rle_vihod())