def print_board(board):
    """
    Prints the Tic-Tac-Toe board in a human-readable format.
    
    Parameters:
        board (list of list): The 3x3 Tic-Tac-Toe board to display.
    
    Returns:
        None
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Avoid printing a line after the last row
            print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the Tic-Tac-Toe game.
    
    Parameters:
        board (list of list): The 3x3 Tic-Tac-Toe board to check for a winner.
    
    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the game is a draw (no more moves left and no winner).
    
    Parameters:
        board (list of list): The 3x3 Tic-Tac-Toe board to check for a draw.
    
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Runs the main game loop for Tic-Tac-Toe, alternating between players and checking for a winner.
    
    Returns:
        None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a row and column between 0 and 2.")
                continue
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                if check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                # Change player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    tic_tac_toe()
