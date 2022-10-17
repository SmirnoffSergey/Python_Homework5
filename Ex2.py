# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 100 конфет. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать
# все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


from random import randint

def check_input(data: str):
    while not data.isdigit():
        data = input('You entered wrong value. Try again\n')
    return data

def another_game():
    if input('Play another game? y / n\n') == 'y':
        return True
    else:
        return False


game_is_on = True
while game_is_on:
    print('Правила игры следующие:\nНа столе лежит 100 конфет. Первый ход определяется жеребьёвкой.\n\
За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход игроку.')
    game_mode = input('Выберите режим игры: 1 - игрок против игрока, 2 - игрок против компьютера\n').lower()


        # Против друг друга



    if game_mode == '1':
        total = 100
        coin = randint(1, 2)
        if coin == 1:
            print('Player 1 has first turn.')
            player1 = True
        else:
            print('Player 2 has first turn.')
            player1 = False

        while total > 0:
            if player1:
                move = int(check_input(input('Player 1 turns.\nHow many candies will you take?\n')))
                if total > 28:
                    while not 0 <= move <= 28:
                        move = int(check_input(input('You cant take so many candies. Try again.\n')))
                elif total <= 28:
                    while not 0 <= move <= total:
                        move = int(check_input(input('You cant take so many candies. Try again.\n')))
                total -= move
                player1 = False
                print(f'Player 1 took {move} candies. The rest is {total}.')
            else:
                move = int(check_input(input('Player 2 turns.\nHow many candies will you take?\n')))
                if total > 28:
                    while not 0 <= move <= 28:
                        move = int(check_input(input('You cant take so many candies. Try again.\n')))
                elif total <= 28:
                    while not 0 <= move <= total:
                        move = int(check_input(input('You cant take so many candies. Try again.\n')))
                total -= move
                player1 = True
                print(f'Player 2 took {move} candies. The rest is {total}.')
        if player1:
            print('Player 2 has made the last turn, he got all the candies\nPlayer 2 won!!!')
        else:
            print('Player 1 has made the last turn, he got all the candies\nPlayer 1 won!!!')
        game_is_on = another_game()

    
    
        # Против компьютера


    elif game_mode == '2':
        total = 100
        coin = randint(1, 2)
        if coin == 1:
            player = True
            print('Player has first turn.')
        else:
            player = False
            print('Computer has first turn.')
        while total > 0:
            if player:
                move = int(check_input(input('Its your turn.\nHow many candies will you take?\n')))
                if total > 28:
                    while not 0 <= move <= 28:
                        move = int(check_input(input('You cant take so many candies. Try again.\n')))
                elif total <= 28:
                    while not 0 <= move <= total:
                        move = int(check_input(input('You cant take so many candies. Try again.\n')))
                total -= move
                player = False
                print(f'You took {move} candies. The rest is {total}.')
            else:
                if total > 28:
                    move = randint(1, 28)
                    total -= move
                    player = True
                    print(f'Computer took {move} candies. The rest is {total}.')
                elif total <= 28:
                    move = randint(1, total)
                    total -= move
                    player = True
                    print(f'Computer took {move} candies. The rest is {total}.')
        if player:
            print('Computer has made the last turn. He wins!!!')
        else:
            print('Congratulations!!! You won!!!')
        game_is_on = another_game()
