# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом"" - это не в моих силах....

from random import randint

def Hod_of_Player(count_of_candies, max_count):
    global last_step
    player_input = int(input("Сколько конфет берем? (возьми от 1 до 28 конфет): "))
    while not (0 < player_input <= max_count):
        if(player_input <= 0):
            print("Нужно взять хоть 1 конфету!")
            player_input = int(input("Сколько конфет берем?: "))
        elif player_input > max_count:
            print(f"Столько не можешь взять... Максимум можно взять {max_count} конфет")
            player_input = int(input("Сколько конфет берем? "))
    else:
        if player_input > count_of_candies:
            player_input = count_of_candies
    last_step = player_input
    return count_of_candies - player_input



def Ostatok(count_of_candies, max, last_round): #считаем число оставшихся конфет
    candi = max + 1 - last_round

    if count_of_candies > max and (1 < count_of_candies / max < 2):
        print(count_of_candies - (max + 1))
        candi = count_of_candies - (max + 1) 
    if candi > count_of_candies or count_of_candies <= max:
        candi = count_of_candies
    return candi

count_of_candies = 90 #для удобства проверки так, вместо 2021
max_count = 28

player = randint(0, 1)

last_step = 0

while(count_of_candies > 0):
    print(f"Ход игрока {player + 1}")
    if player == 0: 
        count_of_candies = Hod_of_Player(count_of_candies, max_count)
        if(count_of_candies > 0):
            player += 1
    else:
            count_of_candies = Hod_of_Player(count_of_candies, max_count)
            if(count_of_candies > 0):
                player -= 1    
    print(f"Конфет {count_of_candies} шт. осталось ")
else:
    print(f"Победил игрок {player + 1}!!!")