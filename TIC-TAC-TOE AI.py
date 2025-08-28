# Tic-Tac-Toe with Unbeatable AI using Minimax

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    move = None
    best_score = -float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    
    while True:
        print_board(board)
        
        # Human move
        try:
            row, col = map(int, input("Enter your move (row and column 0-2): ").split())
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
            board[row][col] = "X"
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as 0 1 2.")
            continue
        
        if is_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print(f"AI moves at {ai_row}, {ai_col}")
        
        if is_winner(board, "O"):
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

# Start the game
tic_tac_toe()
