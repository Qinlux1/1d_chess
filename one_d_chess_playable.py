import random

def start_game():
    start_board = create_board()
    game_mechanics(start_board)

def start_game_with_bot():
    start_board = create_board()
    game_mechanics_bot(start_board)

def create_board():

    initial_board = ["WKi", "EMPTY", "WKn", 
                    "EMPTY", "EMPTY", "EMPTY", 
                    "BKn", "BKn", "BKi"]
    
    return initial_board

def printable_board(board):

    for index in range(0, 9):
        if board[index] == "EMPTY":
            board[index] = "   "

    print_board = "+-----------------------------------------------------+\n"
    print_board += "| {} ".format(board[0])
    print_board += "| {} ".format(board[1])
    print_board += "| {} ".format(board[2])
    print_board += "| {} ".format(board[3])
    print_board += "| {} ".format(board[4])
    print_board += "| {} ".format(board[5])
    print_board += "| {} ".format(board[6])
    print_board += "| {} ".format(board[7])
    print_board += "| {} |\n".format(board[8])
    print_board += "+-----------------------------------------------------+"
    return print_board

def is_valid_move(board, position, color):

    if int(position) < 0 or int(position) > 8:
        return False

    elif color == "WHITE":
        return board[position] == "WKi" or board[position] == "WKn"
    
    elif color == "BLACK":
        return board[position] == "BKi" or board[position] == "BKn"
    
    else:
        return False
    
def move_king(board, position, direction):
    
    if board[position] == "WKi":
        color = "WHITE"

    elif board[position] == "BKi":
        color = "BLACK"


    if direction == "RIGHT":
        index = position + 1
        while index <= 8:
            if board[index] != "EMPTY":
                board[index] = "KING"
                board[position] = "EMPTY"
                index = 9
            index += 1

    elif direction == "LEFT":
        index = position - 1
        while index >= 0:
            if board[index] != "EMPTY":
                board[index] = "KING"
                board[position] = "EMPTY"
                index = -1
            index -= 1

    for index in range(0, 9):
        if board[index] == "KING" and color == "WHITE":
            board[index] = "WKi"
        elif board[index] == "KING" and color == "BLACK":
            board[index] = "BKi"
    
    return board

def move_knight(board, position, direction):
    
    if board[position] == "WKn":
        color = "WHITE"

    elif board[position] == "BKn":
        color = "BLACK"


    if direction == "RIGHT" and position > 6:
        return board
    
    elif direction == "LEFT" and position < 2:
        return board
    
    if direction == "RIGHT":
        board[position] = "EMPTY"
        board[position + 2] = "KNIGHT"

    elif direction == "LEFT":
        board[position] = "EMPTY"
        board[position - 2] = "KNIGHT"

    for index in range(0, 9):
        if board[index] == "KNIGHT" and color == "WHITE":
            board[index] = "WKn"
        elif board[index] == "KNIGHT" and color == "BLACK":
            board[index] = "BKn"

    return board

def move(board, position, direction):

    if board[position] == "WKi" or board[position] == "BKi":
        board = move_king(board, position, direction)

    elif board[position] == "WKn" or board[position] == "BKn":
        board = move_knight(board, position, direction)

    return board

def is_game_over(board):
    
    if "BKi" in board and "WKi" in board:
        return False
    
    elif "WKi" in board and "BKi" not in board:
        return True
    
    elif "BKi" in board and "WKi" not in board:
        return True

def game_mechanics(board):

    quips = ["Good move." ,"Interesting move." ,"That doesn't seem like a good move." ,"Ooo."]

    print(printable_board(board))
    print("Start of Game! White Goes First.")

    color = "WHITE"
    while is_game_over(board) == False:
        if color == "WHITE":
            piece = input("What's the position of the piece you would like to move? ")
            direction  = input("What direction would you like to move? ")
            while is_valid_move(board, int(piece), color) == False:
                piece = input("Invalid move.\nWhat's the position of the piece you would like to move? ")
                direction  = input("What direction would you like to move? ")
            board = move(board, int(piece), direction)

            if is_game_over(board) == True:
                print(printable_board(board))
            else:
                print(printable_board(board))
                print(quips[random.randint(0,3)])
                print("\nBlack's turn!")
                color = "BLACK"

        elif color == "BLACK":
            piece = input("What's the position of the piece you would like to move? ")
            direction  = input("What direction would you like to move? ")
            while is_valid_move(board, int(piece), color) == False:
                piece = input("Invalid move.\nWhat's the position of the piece you would like to move? ")
                direction  = input("What direction would you like to move? ")
            board = move(board, int(piece), direction)

            if is_game_over(board) == True:
                print(printable_board(board))
            else:
                print(printable_board(board))
                print(quips[random.randint(0,3)])
                print("\nWhite's turn!")
                color = "WHITE"

def bot(board, color):

    int_board = board
    knight_counter = 0
    knight_index = []

    piece_type_num = random.randint(0,2)
    direction_num = random.randint(0,1)

    if piece_type_num == 2:
        piece_type = "KING"
    
    else:
        piece_type = "KNIGHT"

    if direction_num == 0:
        direction = "RIGHT"

    else:
        direction = "LEFT"


    if color == "WHITE":
            if piece_type == "KNIGHT" and "WKn" not in board:
                piece_type = "KING"
            elif piece_type == "KING" and "WKi" not in board:
                position = 0
                direction = "RESIGN"
                return None
            
            if piece_type == "KNIGHT":
                for index in range(0,9):
                    if board[index] == "WKn":
                        knight_counter += 1
                        knight_index.append(index)
                if knight_counter == 2:
                    position = knight_index[random.randint(0,1)]
                else:
                    position = knight_index[0]
                

            elif piece_type == "KING":
                for index in range(0,9):
                    if board[index] == "WKi":
                        position = index

            board = move(int_board, position, direction)

            if int_board == board and direction == "RIGHT":
                direction == "LEFT"
            
            elif int_board == board and direction == "LEFT":
                direction == "RIGHT"


    elif color == "BLACK":
            if piece_type == "KNIGHT" and "BKn" not in board:
                piece_type = "KING"
            elif piece_type == "KING" and "BKi" not in board:
                position = 0
                direction = "RESIGN"
                return None
            
            if piece_type == "KNIGHT":
                for index in range(0,9):
                    if board[index] == "BKn":
                        knight_counter += 1
                        knight_index.append(index)
                if knight_counter == 2:
                    position = knight_index[random.randint(0,1)]
                else:
                    position = knight_index[0]


            elif piece_type == "KING":
                for index in range(0,9):
                    if board[index] == "BKi":
                        position = index

            board = move(int_board, position, direction)

            if int_board == board and direction == "RIGHT":
                direction == "LEFT"
            
            elif int_board == board and direction == "LEFT":
                direction == "RIGHT"
    
    if is_game_over(board) == "True":
        direction = "WIN"

    return(position, direction)


def game_mechanics_bot(board):

    quips = ["Good move." ,"Interesting move." ,"That doesn't seem like a good move." ,"Ooo."]

    print("Start of game!")
    int_color = input("Do you want to play as white or as black?\n")

    if int_color == "White" or int_color == "white" or int_color == "WHITE":
        color = "WHITE"

    elif int_color == "Black" or int_color == "black" or int_color == "BLACK":
        color = "BLACK"

    print(printable_board(board))

    if color == "WHITE":
            while is_game_over(board) == False:
                bot_color = "BLACK"
                
                # user moves first
                piece = input("What's the position of the piece you would like to move? ")
                direction = input("What direction would you like to move? ")
                
                while is_valid_move(board, int(piece), color) == False:
                    piece = input("Invalid move.\nWhat's the position of the piece you would like to move? ")
                    direction = input("What direction would you like to move? ")
                
                board = move(board, int(piece), direction)

                if is_game_over(board) == True:
                    print(printable_board(board))
                    print("You win!")
                    return None
                else:
                    print(printable_board(board))
                    print(quips[random.randint(0,3)])
                
                # then, bot moves
                
                (position, direction) = bot(board, bot_color)

                if direction == "RESIGN":
                    print(printable_board(board))
                    print("You win!")
                    return None
                
                if direction == "WIN":
                    print(printable_board(board))
                    print("The bot wins!")
                    return None

                board = move(board, position, direction)

                if is_game_over(board) == True:
                    print(printable_board(board))
                    print("You win!")
                    return None

                print(printable_board(board))
                print("Your turn!")
                

    elif color == "BLACK":
            while is_game_over(board) == False:
                bot_color = "WHITE"
                
                # bot moves first
                
                (position, direction) = bot(board, bot_color)

                if direction == "RESIGN":
                    print(printable_board(board))
                    print("You win!")
                    return None
                
                if direction == "WIN":
                    print(printable_board(board))
                    print("The bot wins!")
                    return None
                
                board = move(board, position, direction)

                if is_game_over(board) == True:
                    print(printable_board(board))
                    print("You win!")
                    return None
                
                print(printable_board(board))
                print("Your turn!")
                
                # then, user moves
                piece = input("What's the position of the piece you would like to move? ")
                direction  = input("What direction would you like to move? ")
                while is_valid_move(board, int(piece), color) == False:
                    piece = input("Invalid move.\nWhat's the position of the piece you would like to move? ")
                    direction  = input("What direction would you like to move? ")

                board = move(board, int(piece), direction)

                if is_game_over(board) == True:
                    print(printable_board(board))
                    print("You win!")
                    return None
                else:
                    print(printable_board(board))
                    print(quips[random.randint(0,3)])

start_game()
#start_game_with_bot()
                    
