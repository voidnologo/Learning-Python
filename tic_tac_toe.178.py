#Tic-Tac-Toe
#plays game of tic-tac-toe against human opponent
#pg 178

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Display game instructions"""
    print(
    """
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and the computer.

        Enter moves based on the grid below by entering the number 0-8.

                    0 | 1 | 2
                    ----------
                    3 | 4 | 5
                    ----------
                    6 | 7 | 8

           Prepare yourself, human.  The ultimate battle is about to begin!\n
     """)


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you want the first move? (y/n):")
    if go_first == 'y':
        human = X
        computer = O
    else:
        human = O
        computer = X
    return human, computer


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    question = "Where do you want to move? ({}):".format(legal)
    while move not in legal:
        move = ask_number(question, 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied.\n")
    print("Fine.")
    return move


def computer_move(board, computer, human):
    #make a copy to work with since function will be changing the list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Computer moves: ", end=" ")

    # if computer can win, take that spot
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # not winning position, try another move
        board[move] = EMPTY

    # if human would win, take that spot
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # not winning position, try another move
        board[move] = EMPTY

    # since no one can win, pick the best available spot
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):

    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("There was a TIE.")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


#start the program
main()
