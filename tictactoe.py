import random

#EDUARD-IOAN IORDACHE

#function to display the board
def display_board(board):
	#trying to clear the board
	print('\n' * 10) 

	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print("-----------")
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print("-----------")
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

#defining player input
def player_input():
	'''
	OUTPUT = (Player 1 marker, Player 2 marker)
	'''

	marker = ''

	while not (marker == 'X' or marker == 'O'):
		marker = input('Player 1: Choose X or O: ').upper()

	if marker == 'X':
		return('X', 'O')
	else: 
		return('O', 'X')	

player_input()

#placing marker on the board
def place_marker(board, marker, position):
	board[position] = marker

place_marker(test_board,'$', 8)
display_board(test_board)

#check if a marker has won
def win_check(board,mark):
    
    #check ALL ROWS and see if they share the same marker
    #check ALL COLUMNS
    #check DIAGONALS
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

win_check(test_board,'X')

#function using random library to choose which player moves first
def choose_first():
	if random.randint(0, 1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

#check if there is space on the board
def space_check(board, position):
	#position is currently an empty string
	return board[position] == ' '

#check if the board is full
def full_board_check(board):
	for i in range(1, 10):
		if space_check(board, i):
			return False
	#board is full if we return True
	return True

#ask and check player next position
def player_choice(board):
	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
		position = int(input('Choose next position (1-9): '))

	return position

#play again function
def replay():
    choice = input('Play again? Enter Yes or No')

    return choice == 'Yes' or choice == 'yes' or choice == 'YES'



#GAME AND LOGIC FUNCTION
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

   	#Game play
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break    