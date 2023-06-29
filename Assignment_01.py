board = ["-", "-", "-",
         "-","-","-",
         "-","-","-",]

currentPlayer = 'X'

winner = None

gameRunning = True


# print game board
def printBoard(board):
    print('| ' + board[0] + ' | ' + board[1] + ' | '  + board[2] + ' |')
    print("-"*13)
    print('| ' + board[3] + ' | ' + board[4] + ' | '  + board[5] + ' |')
    print("-"*13)
    print('| ' + board[6] + ' | ' + board[7] + ' | '  + board[8] + ' |')
      
#take player input
def playerInput():
    choice = int(input("Enter a number (1-9): "))
    if choice >= 1 and choice <=9 and board[choice - 1] == '-':
        board[choice - 1] = currentPlayer
    else:
        print("Please enter a valid input.")
        
        


#check for win or tie
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
       winner = board[0]
       return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
       winner = board[0]
       return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
       winner = board[0]
       return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie.")
        gameRunning = False

#switch the player

while gameRunning:
    printBoard(board)
    playerInput()
    # checkRow(board)
    # checkColumn(board)
    # checkDiagonal(board)
    # checkColumn(board)