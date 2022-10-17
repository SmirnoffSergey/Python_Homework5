# Создайте программу для игры в 'Крестики-нолики'.


from random import randint

def check_input(data: str):
    while not data.isdigit() or not 1 <= int(data) <=9:
        data = input('You entered wrong value. Try again\n')
    return data

def another_game():
    if input('Play another game? y / n\n') == 'y':
        return True
    else:
        return False

def show_field(arr):
    print(f' {arr[0]} | {arr[1]} | {arr[2]}')
    print('--  --  --')
    print(f' {arr[3]} | {arr[4]} | {arr[5]}')
    print('--  --  --')
    print(f' {arr[6]} | {arr[7]} | {arr[8]}')
    print()

def check_field(arr):
    if arr[0] == 'X' and arr[1] == 'X' and arr[2] == 'X':
        return True
    elif arr[3] == 'X' and arr[4] == 'X' and arr[5] == 'X':
        return True
    elif arr[6] == 'X' and arr[7] == 'X' and arr[8] == 'X':
        return True
    elif arr[0] == 'X' and arr[3] == 'X' and arr[6] == 'X':
        return True
    elif arr[1] == 'X' and arr[4] == 'X' and arr[7] == 'X':
        return True
    elif arr[2] == 'X' and arr[5] == 'X' and arr[8] == 'X':
        return True
    elif arr[0] == 'X' and arr[4] == 'X' and arr[8] == 'X':
        return True
    elif arr[2] == 'X' and arr[4] == 'X' and arr[6] == 'X':
        return True
    elif arr[0] == '0' and arr[1] == '0' and arr[2] == '0':
        return True
    elif arr[3] == '0' and arr[4] == '0' and arr[5] == '0':
        return True
    elif arr[6] == '0' and arr[7] == '0' and arr[8] == '0':
        return True
    elif arr[0] == '0' and arr[3] == '0' and arr[6] == '0':
        return True
    elif arr[1] == '0' and arr[4] == '0' and arr[7] == '0':
        return True
    elif arr[2] == '0' and arr[5] == '0' and arr[8] == '0':
        return True
    elif arr[0] == '0' and arr[4] == '0' and arr[8] == '0':
        return True
    elif arr[2] == '0' and arr[4] == '0' and arr[6] == '0':
        return True
    else:
        return False


game_is_on = True
while game_is_on:
    cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    free_cells = 9
    print('Welcome to the cross-zero game!\nThe choice of move of which player is random.\nPlayer 1 - crosses. Player 2 - zeroes.\n')    
    
    game_mode = True    
    if game_mode:        
        coin = randint(1,2)
        if coin == 1:
            player1 = True
        else:
            player1 = False
        finish = False
        while not free_cells == 0 and not finish:

            if player1:
                print('Player 1 turn\n')
                show_field(cells)
                move = int(check_input(input('Choose the cell\n')))                
                while cells[move-1] == 'X' or cells[move-1] == '0':
                    move = int(check_input(input('Эта ячейка уже занята! Выберите другую\n')))
                cells[move-1] = 'X'
                player1 = False
                free_cells -= 1
                finish = check_field(cells)
            else:
                print('Player 2 turn\n')
                show_field(cells)
                move = int(check_input(input('Choose the cell\n')))                
                while cells[move-1] == 'X' or cells[move-1] == '0':
                    move = int(check_input(input('Эта ячейка уже занята! Выберите другую\n')))
                cells[move-1] = '0'
                player1 = True
                free_cells -= 1
                finish = check_field(cells)

        show_field(cells)
        if free_cells == 0:
            print('Nobody won!\n')
            game_is_on = another_game()
        
        elif player1:
            print('Player 2 wins!\n')
            game_is_on = another_game()
        
        else:
            print('Player 1 wins!\n')
            game_is_on = another_game()