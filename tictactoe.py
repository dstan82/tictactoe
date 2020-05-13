# Tic Tac Toe Game
from os import system


# clear screen Function
def clear():
    '''
    DOCSTRING: Clear screen function
    '''
    system('clear')


# draw table function
def ttt_table():
    '''
    DOCSTRING: Function for printing the tic tac toe table
    '''
    print('   |   |   ')
    print(f" {positions[7]} | {positions[8]} | {positions[9]} ")
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f" {positions[4]} | {positions[5]} | {positions[6]} ")
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f" {positions[1]} | {positions[2]} | {positions[3]} ")
    print('   |   |   ')


# winning combinations
w1 = ['1', '2', '3']
w2 = ['4', '5', '6']
w3 = ['7', '8', '9']
w4 = ['1', '4', '7']
w5 = ['2', '5', '8']
w6 = ['3', '6', '9']
w7 = ['3', '5', '7']
w8 = ['1', '5', '9']
winning_list = [w1, w2, w3, w4, w5, w6, w7, w8]


# verify winning conditions and returns boolean (True/False)
def verify_win(player_moves, player):
    for win_comb in winning_list:
        if win_comb[0] in player_moves and win_comb[1] in player_moves and win_comb[2] in player_moves:
            print(f' Congratulations, player "{player}" won the game!')
            return True
        if len(player1_moves) + len(player2_moves) == 9:
            print(f" It's a tie!")
            return True


# calling first clear of the screen
clear()
print('Welcome to Tic Tac Toe!\n')

players = ['X', 'O']
first_player = ''
while first_player != 'X' and first_player != 'O':
    first_player = input('Do you want to be "x" or "o" ? ').upper()
print(f'\n\n Player {first_player} will go first. ', end='')
players.remove(first_player)
second_player = players[0]


play = ''
while play != 'y' and play != 'n':
    play = input('Are you ready to play ? (y/n):')

GAME_WON = False
while play == 'y':
    positions = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_moves = []
    player2_moves = []
    possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    clear()
    ttt_table()
    while not GAME_WON:
        # 1st player turn
        take_move = input(f' Player "{first_player}" turn, please enter a number (1-9):')
        while take_move not in possible_moves or take_move in player1_moves or take_move in player2_moves:
            take_move = input(f' Please enter a valid move, empty cell (1 to 9:)')
        positions[int(take_move)] = first_player
        player1_moves.append(take_move)
        clear()
        ttt_table()
        if verify_win(player1_moves, first_player):
            break
        # 2nd player turn
        take_move = input(f' Player "{second_player}" turn please enter a number (1-9):')
        while take_move not in possible_moves or take_move in player1_moves or take_move in player2_moves:
            take_move = input(f' Please enter a valid move, empty cell (1 to 9:)')
        positions[int(take_move)] = second_player
        player2_moves.append(take_move)
        clear()
        ttt_table()
        if verify_win(player2_moves, second_player):
            break

    play = input('\nDo you want to play again ? (y/n):')
print('Bye!')
