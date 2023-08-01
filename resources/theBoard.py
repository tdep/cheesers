import Square


theBoard = Square.theBoard

for row in theBoard:
    i = 0
    while i < 8:
        if row[i].piece != None:
            if row[i].coordinate[0] != "h":
                print(row[i].coordinate, end="|")
                i += 1
            else:
                print(row[i].coordinate)
                i += 1
