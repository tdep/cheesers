import Square

theBoard = Square.theBoard

def populator():
    # Populates the board according to the coordinates listed in theBoard object that is passed to it which updates every time a turn is over.
    pass

def printBoard(board):
    # Prints the board to the screen
    r = 8
    for row in board:
        i = 0
        while i < 8:
            if row[i].piece != None:
                if row[i].coordinate[0] != "h":
                    print(row[i].piece, end=" | ")
                    i += 1
                else:
                    print(row[i].piece, end=" | ")
                    i += 1
            else:
                if row[i].coordinate[0] != "h":
                    print("   ", end=" | ")
                    i += 1
                else:
                    print("   " + " | " + str(r))
                    i += 1
        if r > 1:
            print(' -  +  -  +  -  +  -  +  -  +  -  +  -  +  -  |')
        r -= 1
    print('_____________________________________________ |')
    print(' A     B     C     D     E     F     G     H')

printBoard(theBoard)
