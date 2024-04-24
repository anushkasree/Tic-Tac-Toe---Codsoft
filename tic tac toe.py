import sys

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to get available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Minimax function with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_winner(board, 'X'):
        return -10 + depth
    elif check_winner(board, 'O'):
        return 10 - depth
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -sys.maxsize
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = sys.maxsize
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to get the best move for the AI player
def get_best_move(board):
    best_eval = -sys.maxsize
    best_move = None
    alpha = -sys.maxsize
    beta = sys.maxsize
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        eval = minimax(board, 0, False, alpha, beta)
        board[move[0]][move[1]] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Player's move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI's turn:")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

play_game()
