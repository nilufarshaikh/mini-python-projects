# function to display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# function to determine the winner
def check_winner(board, player):
    # Check the rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check the columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check the diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")

    for _ in range(9):
        print_board(board)

        # Add answers as row space column
        row, col = map(int, input(f"Player {player}, enter row and column (1-3): ").split())

        if board[row-1][col-1] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row-1][col-1] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
