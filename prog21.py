def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turns = 0

    while turns < 9:
        print_board(board)
        player = players[turns % 2]
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = player
            turns += 1
            if check_winner(board, player):
                print_board(board)
                print("Player", player, "wins!")
                return
        else:
            print("Cell already taken, try again.")
    print_board(board)
    print("It's a draw!")

tic_tac_toe()
