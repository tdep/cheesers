import resources.Pieces

blackPieces = resources.Pieces.blackPieces
whitePieces = resources.Pieces.whitePieces

allPieces = blackPieces + whitePieces


class Square:
    def __init__(self, coordinate, occupied, piece):
        self.coordinate = coordinate
        self.occupied = occupied
        self.piece = piece

    def populator(self, allPieces):
        # Populates the board according to the coordinates listed in theBoard 
        # object that is passed to it which updates every time a turn is over.
        for pieces in allPieces:
            if pieces.coordinates == self.coordinate:
                self.piece = pieces.id
                self.occupied = True
        

# Initializing all square instances
a8 = Square(("a", 8), False, None)
b8 = Square(("b", 8), False, None)
c8 = Square(("c", 8), False, None)
d8 = Square(("d", 8), False, None)
e8 = Square(("e", 8), False, None)
f8 = Square(("f", 8), False, None)
g8 = Square(("g", 8), False, None)
h8 = Square(("h", 8), False, None)

a7 = Square(("a", 7), False, None)
b7 = Square(("b", 7), False, None)
c7 = Square(("c", 7), False, None)
d7 = Square(("d", 7), False, None)
e7 = Square(("e", 7), False, None)
f7 = Square(("f", 7), False, None)
g7 = Square(("g", 7), False, None)
h7 = Square(("h", 7), False, None)

a6 = Square(("a", 6), False, None)
b6 = Square(("b", 6), False, None)
c6 = Square(("c", 6), False, None)
d6 = Square(("d", 6), False, None)
e6 = Square(("e", 6), False, None)
f6 = Square(("f", 6), False, None)
g6 = Square(("g", 6), False, None)
h6 = Square(("h", 6), False, None)

a5 = Square(("a", 5), False, None)
b5 = Square(("b", 5), False, None)
c5 = Square(("c", 5), False, None)
d5 = Square(("d", 5), False, None)
e5 = Square(("e", 5), False, None)
f5 = Square(("f", 5), False, None)
g5 = Square(("g", 5), False, None)
h5 = Square(("h", 5), False, None)

a4 = Square(("a", 4), False, None)
b4 = Square(("b", 4), False, None)
c4 = Square(("c", 4), False, None)
d4 = Square(("d", 4), False, None)
e4 = Square(("e", 4), False, None)
f4 = Square(("f", 4), False, None)
g4 = Square(("g", 4), False, None)
h4 = Square(("h", 4), False, None)

a3 = Square(("a", 3), False, None)
b3 = Square(("b", 3), False, None)
c3 = Square(("c", 3), False, None)
d3 = Square(("d", 3), False, None)
e3 = Square(("e", 3), False, None)
f3 = Square(("f", 3), False, None)
g3 = Square(("g", 3), False, None)
h3 = Square(("h", 3), False, None)

a2 = Square(("a", 2), False, None)
b2 = Square(("b", 2), False, None)
c2 = Square(("c", 2), False, None)
d2 = Square(("d", 2), False, None)
e2 = Square(("e", 2), False, None)
f2 = Square(("f", 2), False, None)
g2 = Square(("g", 2), False, None)
h2 = Square(("h", 2), False, None)

a1 = Square(("a", 1), False, None)
b1 = Square(("b", 1), False, None)
c1 = Square(("c", 1), False, None)
d1 = Square(("d", 1), False, None)
e1 = Square(("e", 1), False, None)
f1 = Square(("f", 1), False, None)
g1 = Square(("g", 1), False, None)
h1 = Square(("h", 1), False, None)


allSquares = [a8, b8, c8, d8, e8, f8, g8, h8,
              a7, b7, c7, d7, e7, f7, g7, h7,
              a6, b6, c6, d6, e6, f6, g6, h6,
              a5, b5, c5, d5, e5, f5, g5, h5,
              a4, b4, c4, d4, e4, f4, g4, h4,
              a3, b3, c3, d3, e3, f3, g3, h3,
              a2, b2, c2, d2, e2, f2, g2, h2,
              a1, b1, c1, d1, e1, f1, g1, h1]

# Setting the piece for each square
for square in allSquares:
    square.populator(allPieces)


# Creating the board which stores all square instances in a list of lists
theBoard = [[a8, b8, c8, d8, e8, f8, g8, h8],
            [a7, b7, c7, d7, e7, f7, g7, h7],
            [a6, b6, c6, d6, e6, f6, g6, h6],
            [a5, b5, c5, d5, e5, f5, g5, h5],
            [a4, b4, c4, d4, e4, f4, g4, h4],
            [a3, b3, c3, d3, e3, f3, g3, h3],
            [a2, b2, c2, d2, e2, f2, g2, h2],
            [a1, b1, c1, d1, e1, f1, g1, h1]]




