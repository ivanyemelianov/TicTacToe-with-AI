# Creating a board with 10 empty strings ([0] is not counting for a position)
board = [' ' for x in range(10)]

# Function to insert a letter to a specific position on the board 
def insertLetter(letter, pos) :
    board[pos] = letter

# Function to check if the position on the board is not taken, returns T or F, comparing psotion with empty string
def spaceIsFree(pos) :
    return board[pos] == ' '

# Function just for printing board
def printBoard(board) :
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# Function checks if the game has a winner, takes in the board list and the letter O or X and checks if any of the winning combinations exist
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

# Function for players move logic
def playerMove():
    # Variable to store the turn
    run = True
    # While run is true
    while run:
        # Take a players input
        move = input('Select the position to place an X (1-9): ')
        # try except to validate players input
        try:
            # Turn the string from players input into integer
            move = int(move)
            # If players input is more then 0 and less then 10
            if move > 0 and move < 10:
                # And the space on the board is free
                if spaceIsFree(move):
                    # Finish the run
                    run = False
                    # And insert the letter X on the board
                    insertLetter('X', move)
                # If the space is not free, notify user and start the while loop again
                else:
                    print('Sorry, this place is occupied.')
            else:
                print('Please type a number within the range.')
        except:
            print('Please type a number.')

# AI moves logic
def compMove():
    # Checking for any free position on the board, creates a list of tuples
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main() :
    print('Welcome to game!')
    printBoard(board)

    while not (isBoardFull(board)) :
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie game')
            else:
                insertLetter('O', move)
                print('Computer place an O in position', move, ':')
                printBoard(board)

        else:
            print('X\'s won this time!')
            break


    if isBoardFull(board) :
        print('Tie game!')

main()