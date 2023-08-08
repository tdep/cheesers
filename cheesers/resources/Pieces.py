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
pawn_b1 = Pawn("b01", ('x','y'), "")
pawn_b2 = Pawn("b02", ('x','y'), "")
pawn_b3 = Pawn("b03", ('x','y'), "")
pawn_b4 = Pawn("b04", ('x','y'), "")
pawn_b5 = Pawn("b05", ('x','y'), "")
pawn_b6 = Pawn("b06", ('x','y'), "")
pawn_b7 = Pawn("b07", ('x','y'), "")
pawn_b8 = Pawn("b08", ('x','y'), "")

rook_b1 = Rook("b09", ('x','y'), "")
rook_b2 = Rook("b10", ('x','y'), "")

knight_b1 = Knight("b11", ('x','y'), "")
knight_b2 = Knight("b12", ('x','y'), "")

bishop_b1 = Bishop("b13", ('x','y'), "")
bishop_b2 = Bishop("b14", ('x','y'), "")

queen_b = Queen("b15", ('x','y'), "")
king_b = King("b16", ('x','y'), "")

# Black pieces
pawn_w1 = Pawn("w01", ('x','y'), "")
pawn_w2 = Pawn("w02", ('x','y'), "")
pawn_w3 = Pawn("w03", ('x','y'), "")
pawn_w4 = Pawn("w04", ('x','y'), "")
pawn_w5 = Pawn("w05", ('x','y'), "")
pawn_w6 = Pawn("w06", ('x','y'), "")
pawn_w7 = Pawn("w07", ('x','y'), "")
pawn_w8 = Pawn("w08", ('x','y'), "")

rook_w1 = Rook("w09", ('x','y'), "")
rook_w2 = Rook("w10", ('x','y'), "")

knight_w1 = Knight("w11", ('x','y'), "")
knight_w2 = Knight("w12", ('x','y'), "")

bishop_w1 = Bishop("w13", ('x','y'), "")
bishop_w2 = Bishop("w14", ('x','y'), "")

queen_w = Queen("w15", ('x','y'), "")
king_w = King("w16", ('x','y'), "")