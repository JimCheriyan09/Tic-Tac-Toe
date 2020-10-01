#Tic Tac Toe
# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_is_on = True

winner = None

current_player = "X"


def display_board():
    print(board[0]+' | '+board[1]+' | '+board[2]+ "     1 | 2 | 3")
    print(board[3]+' | '+board[4]+' | '+board[5]+ "     4 | 5 | 6")
    print(board[6]+' | '+board[7]+' | '+board[8]+ "     7 | 8 | 9")
    print('\n')


def play_game():
    display_board()

    while (game_is_on):
        handle_turn(current_player)

        check_game_over()

        flip_player()

    # The game has ended
    if winner == 'X' or winner == "O":
        print(winner+" is the winner.")
    elif winner == None:
        print("It's a Tie :(")


def handle_turn(player):
    print("It is "+player+"'s turn.")
    position = input("Choose a position from 1 to 9:")
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


def check_game_over():
    # check if win
    check_if_win()
    # check whether tie
    check_if_tie()


def check_if_win():
    global winner
    # check rows
    row_winner = check_rows()
    # check diagonals
    column_winner = check_columns()
    # check columns
    diagonal_winner = check_diagonals()

    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there is a winner
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
        # there is a winner
    else:
        winner = None


def check_rows():
    global game_is_on

    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_is_on = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_columns():
    global game_is_on
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1 or column2 or column3:
        game_is_on = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


def check_diagonals():
    global game_is_on
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        game_is_on = False
        # print(game_is_on)
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    else:
        return None


def check_if_tie():
    global game_is_on
  # If board is full
    if "-" not in board:
        game_is_on = False
        return True
  # Else there is no tie
    else:
        return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


play_game()
