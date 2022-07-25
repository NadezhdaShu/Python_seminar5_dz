# Игра крестики нолики

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

#обычный код
for row in matrix:
    for item in row:
        ''.join('{:4}'.format(item))
    print('\n')
