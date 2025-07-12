
import math
def show_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None
def board_full(board):
    return all(cell != ' ' for row in board for cell in row)
def minimax(board, depth, is_ai_turn):
    winner = get_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif board_full(board):
        return 0

    if is_ai_turn:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score
def find_best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def start_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You're X, and I'll play as O.")
    show_board(board)

    while True:
        try:
            row, col = map(int, input("Your move (row and col, 0–2): ").split())
            if board[row][col] != ' ':
                print("Oops! That spot’s already taken.")
                continue
            board[row][col] = 'X'
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 2.")
            continue

        show_board(board)

        if get_winner(board):
            print(f"{get_winner(board)} wins!")
            break
        if board_full(board):
            print("Draw! Well played.")
            break

        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'O'
        print("My move:")
        show_board(board)

        if get_winner(board):
            print(f"{get_winner(board)} wins!")
            break
        if board_full(board):
            print("Draw! That was close.")
            break

start_game()