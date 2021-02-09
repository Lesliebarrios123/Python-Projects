board = ["-","-","-","-","-","-","-","-","-"]


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


game_going_on = True
winner = None
current_player = "X"


def h_turns(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Spot taken. Go again!")
    board[position] = player
    display_board()


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def check_rows():
    global game_going_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_going_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_going_on
    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"
    if columns_1 or columns_2 or columns_3:
        game_going_on = False
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return


def check_diagonal():
    global game_going_on
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game_going_on = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def game_over():
    check_win()
    check_if_tie()


def check_if_tie():
    global game_going_on
    if "-" not in board:
        game_going_on = False
    return


def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def play_game():
    # Display initial board
    display_board()
    while game_going_on:
        h_turns(current_player)
        game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


play_game()