dictionary = {} #пустой словарь

#создание пар

dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }


print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличатьсяprint(dictionary) 

for k in dictionary.keys(): #будут напечатаны ключи up
    print(k)

for k in dictionary.values(): #будут напечатаны значения ↑...
    print(k)



print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →