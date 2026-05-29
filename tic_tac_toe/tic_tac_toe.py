import random

# create empty board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# show board
def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# check winner
def winner(mark):
    if (board[0] == mark and board[1] == mark and board[2] == mark) or \
       (board[3] == mark and board[4] == mark and board[5] == mark) or \
       (board[6] == mark and board[7] == mark and board[8] == mark) or \
       (board[0] == mark and board[3] == mark and board[6] == mark) or \
       (board[1] == mark and board[4] == mark and board[7] == mark) or \
       (board[2] == mark and board[5] == mark and board[8] == mark) or \
       (board[0] == mark and board[4] == mark and board[8] == mark) or \
       (board[2] == mark and board[4] == mark and board[6] == mark):
        return True
    return False

# check draw
def draw():
    return " " not in board

print("Welcome to Tic Tac Toe")
print("You are X and Computer is O")

while True:
    show_board()

    # player move
    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = "X"
    else:
        print("Already filled. Try again.")
        continue

    if winner("X"):
        show_board()
        print("You won!")
        break

    if draw():
        show_board()
        print("Match Draw")
        break

    # computer move
    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    comp = random.choice(empty)
    board[comp] = "O"

    if winner("O"):
        show_board()
        print("Computer won!")
        break

    if draw():
        show_board()
        print("Match Draw")
        break