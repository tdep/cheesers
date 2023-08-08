class Pieces:
    def __init__(self, id, coordinates, player):
        self.id = id
        self.coordinates = coordinates
        self.player = player
        self.captured = False

# Piece methods
    def move(self, piece, newCoordinates):
        # when makeAMove is called, this runs to update the coordinates of a piece
        pass

    def capture(self, newPiece):
        # what happens when a piece is captured?
        pass

# Coordinates need to translate x direction to string from integer, maybe index of a list of letters? or a dictionary {0:'a', 1:'b, 2:'c'} or {'a':0,'b':1,'c':2}? 
# then each piece can track an x value and the coordinates add or subtract from them depending on the move
class Pawn(Pieces):
    def __init__(self, id, coordinates, player):
        super().__init__(id, coordinates, player)
        self.moved = False # Turns to true when pawn is initially moved (move two spaces at start, 1 for rest of game)
        self.travel = [(0, 1)] # 0 steps left & right, 1 step forward
        self.overtake = [(-1, 1), (1, 1)] # 1 step left (-1), 1 step forward; or 1 step right (1), 1 step forward

    def prisonerSwap(player, thisPiece, prisoner):
        # when a pawn reaches the other side, they get to swap for a piece that has been captured previously, grab the list of captured pieces
        # for this player, and let them choose which they want to exchange
        pass

class Rook(Pieces):
    def __init__(self, id, coordinates, player):
        super().__init__(id, coordinates, player)
        self.castle = False
        self.travel = [('x','y')] # rooks can move a variable distance, probably need to define a method for this
        self.overtake = [('x','y')] # see above
    def castling(player):
        # need to find out how this works in real chess, should be an option for the player if castle = False
        pass
    
class Knight(Pieces):
    def __init__(self, id, coordinates, player):
        super().__init__(id, coordinates, player)
        self.travel = [(-1, 3), (1, 3), (3, 1), (3, -1), (1, -3), (-1, -3), (-3, -1), (-3, 1)]
        self.overtake = [(-1, 3), (1, 3), (3, 1), (3, -1), (1, -3), (-1, -3), (-3, -1), (-3, 1)]

class Bishop(Pieces):
    def __init__(self, id, coordinates, player):
        super().__init__(id, coordinates, player)
        self.travel = [('x','y')] # see rooks
        self.overtake = [('x','y')] # see above

class Queen(Pieces):
    def __init__(self, id, coordinates, player):
        super().__init__(id, coordinates, player)
        self.travel = [('x','y')] # see rooks
        self.overtake = [('x','y')] # see above

class King(Pieces):
    def __init__(self, id, coordinates, player):
        super().__init__(id, coordinates, player)
        self.areYouSingle = False # Should the King be the only one standing, trigger a checkmate
        self.travel = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
        self.overtake = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]


# Initialize all piece instances

# Black pieces
pawn_b1 = Pawn("b01", ('a', 7), "")
pawn_b2 = Pawn("b02", ('b', 7), "")
pawn_b3 = Pawn("b03", ('c', 7), "")
pawn_b4 = Pawn("b04", ('d', 7), "")
pawn_b5 = Pawn("b05", ('e', 7), "")
pawn_b6 = Pawn("b06", ('f', 7), "")
pawn_b7 = Pawn("b07", ('g', 7), "")
pawn_b8 = Pawn("b08", ('h', 7), "")

rook_b1 = Rook("b09", ('a', 8), "")
rook_b2 = Rook("b10", ('h', 8), "")

knight_b1 = Knight("b11", ('b', 8), "")
knight_b2 = Knight("b12", ('g', 8), "")

bishop_b1 = Bishop("b13", ('c', 8), "")
bishop_b2 = Bishop("b14", ('f', 8), "")

queen_b = Queen("b15", ('d', 8), "")
king_b = King("b16", ('e', 8), "")

blackPieces = [pawn_b1, pawn_b2, pawn_b3, pawn_b4, pawn_b5, pawn_b6, pawn_b7, pawn_b8,
               rook_b1, knight_b1, bishop_b1, queen_b, king_b, bishop_b2, knight_b2, rook_b2]

# White pieces
pawn_w1 = Pawn("w01", ('a', 2), "")
pawn_w2 = Pawn("w02", ('b', 2), "")
pawn_w3 = Pawn("w03", ('c', 2), "")
pawn_w4 = Pawn("w04", ('d', 2), "")
pawn_w5 = Pawn("w05", ('e', 2), "")
pawn_w6 = Pawn("w06", ('f', 2), "")
pawn_w7 = Pawn("w07", ('g', 2), "")
pawn_w8 = Pawn("w08", ('h', 2), "")

rook_w1 = Rook("w09", ('a', 1), "")
rook_w2 = Rook("w10", ('h', 1), "")

knight_w1 = Knight("w11", ('b', 1), "")
knight_w2 = Knight("w12", ('g', 1), "")

bishop_w1 = Bishop("w13", ('c', 1), "")
bishop_w2 = Bishop("w14", ('f', 1), "")

queen_w = Queen("w15", ('d', 1), "")
king_w = King("w16", ('e', 1), "")

whitePieces = [pawn_w1, pawn_w2, pawn_w3, pawn_w4, pawn_w5, pawn_w6, pawn_w7, pawn_w8,
               rook_w1, knight_w1, bishop_w1, queen_w, king_w, bishop_w2, knight_w2, rook_w2]