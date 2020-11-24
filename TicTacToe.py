def display_board(board):
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    
test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

display_board(test_board)

def player_input():
    
    marker = ''
    
    while (marker != 'X') and (marker != "O"): 
        marker = input('Player 1, choose X or O:').upper()

        print(f'Player 1 chose {marker}')
        if marker == 'X':
            print("Player 2 is O")
        elif marker == 'O':
            print("Player 2 is X")

        player1 = marker
    
        if (player1 == 'X'):
            player2 = 'O'
        else:
            player2 = 'X'
    return(player1, player2)  


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark)) 

import random
def choose_first():
    flip = random.randint(0 , 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' ' 

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True 
            

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    
    return position

def replay(): 
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'

print('Welcome to Tic TAC TOE')

while True:

    the_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Want to play? y or n')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        
            
        if turn == 'Player 1':

            #show de board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board, player1_marker, position)
                

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON!!!')
                game_on = False
            else:
                if full_board_check(the_board) == True:
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else: 
                    turn = 'Player 2'
        else:
            #show de board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board, player2_marker, position)
            

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else: 
                    turn = 'Player 1'
    if not replay():
        break
        

