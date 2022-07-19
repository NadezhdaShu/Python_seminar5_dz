
#запись в файл
colors = ['red', 'blue', 'green']
data = open('file.txt', 'a')
data.writelines(colors)
data.close


with open('file.txt', 'a') as data:
    data.write('line\n')
    # не нужно data close


#чтение данных из файла
path = 'file.txt'
data = open(path, 'r') #открытие в режиме чтения
for line in data:
    print(line)
data.close()


#удаление последнего элемента списка
list1 = [1, 2, 3, 4, 5]
print(len(list1))
print(list1.pop())
print(list1)

#если нужно конкретный элемент удалить
list1 = [1, 2, 3, 4, 5]
print(list1.pop(2))
print(list1)

#вставить на нужную позицию элемент
list1 = [1, 2, 3, 4, 5]
print(list1.insert(2, 11)) #указываем номер индекса и потом значение элемента
print(list1)

#если в конец добавить элемент
print(list1.append(11))