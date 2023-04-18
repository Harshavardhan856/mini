def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i != 2:
            print("-" * 9)

def get_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_inputs:
            return user_input
        print("Invalid input. Please try again.")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def main():
    board = [[" " for i in range(3)] for j in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        row = int(get_input(f"{player}, enter row (1-3): ", ["1", "2", "3"])) - 1
        col = int(get_input(f"{player}, enter column (1-3): ", ["1", "2", "3"])) - 1
        if board[row][col] != " ":
            print("That cell is already filled. Please try again.")
        else:
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"Congratulations, {player} won!")
                break
            if turn == 8:
                print_board(board)
                print("The game is a tie.")
                break
            turn += 1

if __name__ == "__main__":
    main()
