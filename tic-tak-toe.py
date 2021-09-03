board = ["0","1","2","3","4","5","6","7","8"]
Player1Turn=True
def clear_terminal(): 
    # can use "import os"
    # os.system("cls||clear")
    print("\033c", end="") # no dependencies


def has_winner():
    global board
    tested_player = Player1Turn ^ True
    if tested_player:
        turn = "X"
    else:
        turn = "O"

    if (board[0] == turn and board[1] == turn and board[2] == turn):
        return True
    if (board[0] == turn and board[3] == turn and board[6] == turn):
        return True
    if (board[0] == turn and board[4] == turn and board[8] == turn):
        return True
    if (board[1] == turn and board[4] == turn and board[7] == turn):
        return True
    if (board[2] == turn and board[4] == turn and board[6] == turn):
        return True
    if (board[2] == turn and board[5] == turn and board[8] == turn):
        return True
    if (board[3] == turn and board[4] == turn and board[5] == turn):
        return True
    if (board[6] == turn and board[7] == turn and board[8] == turn):
        return True
    return False
        


def DrawGame():
    global board
    print("""
   |   |   
 {} | {} | {}
   |   |
-----------
   |   |
 {} | {} | {}
   |   |
-----------
   |   |
 {} | {} | {}
   |   |
""".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))
    
def no_move_left():
    global board
    for item in range(9):
        if board[item] != "X" and board[item] != "O":
            return False
    return True
            
    
def get_int_input(text):
    try:
        return int(input(text))
    except:
        return get_int_input(text)
    
current_turn = -1
last_turn_error = None
def next_turn():
    clear_terminal()
    global board
    global Player1Turn
    global last_turn_error
    global current_turn

    if Player1Turn:
        print("Player 1 (X) Turn ")
    else:
        print("Player 2 (O) Turn")
        
    DrawGame()
    if last_turn_error:
        print(last_turn_error)
        last_turn_error = None
    current_turn = get_int_input("Please input your next move: ")

        
    if board.__contains__(str(current_turn)):
        if board[current_turn] != "X" and board[current_turn] != "O":
            if Player1Turn:
                board[current_turn] = "X"
            else:
                board[current_turn] = "O"
            Player1Turn ^= True
    else:
        last_turn_error= "invalid number"
    
while (no_move_left() == False and has_winner() == False):
    next_turn()

clear_terminal()
DrawGame()
if has_winner():
    winning_player = Player1Turn ^ True
    if winning_player:
        print("Winner: Player 1 (X)")
    else:
        print("Winner: Player 2 (O)")
else:
    print("Draw")