# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

textt = 'Жил на свете абв крутой человабвек человек'.lower()

def del_words(textt):
    textt = list(filter(lambda x: 'абв' not in x, textt.split(' ')))
    return " ".join(textt)

textt = del_words(textt)
print (textt)


# ПЕРВОНАЧАЛЬНОЕ РЕШЕНИЕ
# words = textt.split(' ')
# slovo = 'абв'
# new_textt = []
# for word in words:
#      if slovo not in word:
#          new_textt.append(word)
# textt = ' '.join(new_textt)
# print (textt)



