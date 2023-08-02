import Square

theBoard = Square.theBoard

def printBoard(board):
    
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
