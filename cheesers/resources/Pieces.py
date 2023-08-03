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
    def __init__(self, id, coordinates, player, captured):
        super().__init__(id, coordinates, player, captured)
        self.moved = False # Turns to true when pawn is initially moved (move two spaces at start, 1 for rest of game)
        self.travel = [(0, 1)] # 0 steps left & right, 1 step forward
        self.overtake = [(-1, 1), (1, 1)] # 1 step left (-1), 1 step forward; or 1 step right (1), 1 step forward

    def prisonerSwap(player, thisPiece, prisoner):
        # when a pawn reaches the other side, they get to swap for a piece that has been captured previously, grab the list of captured pieces
        # for this player, and let them choose which they want to exchange
        pass

class Rook(Pieces):
    def __init__(self, id, coordinates, player, captured):
        super().__init__(id, coordinates, player, captured)
        self.castle = False
        self.travel = [('x','y')] # rooks can move a variable distance, probably need to define a method for this
        self.overtake = [('x','y')] # see above
    def castling(player):
        # need to find out how this works in real chess, should be an option for the player if castle = False
        pass
    
class Knight(Pieces):
    def __init__(self, id, coordinates, player, captured):
        super().__init__(id, coordinates, player, captured)
        self.travel = [(-1, 3), (1, 3), (3, 1), (3, -1), (1, -3), (-1, -3), (-3, -1), (-3, 1)]
        self.overtake = [(-1, 3), (1, 3), (3, 1), (3, -1), (1, -3), (-1, -3), (-3, -1), (-3, 1)]

class Bishop(Pieces):
    def __init__(self, id, coordinates, player, captured):
        super().__init__(id, coordinates, player, captured)
        self.travel = [('x','y')] # see rooks
        self.overtake = [('x','y')] # see above

class Queen(Pieces):
    def __init__(self, id, coordinates, player, captured):
        super().__init__(id, coordinates, player, captured)
        self.travel = [('x','y')] # see rooks
        self.overtake = [('x','y')] # see above

class King(Pieces):
    def __init__(self, id, coordinates, player, captured):
        super().__init__(id, coordinates, player, captured)
        self.areYouSingle = False # Should the King be the only one standing, trigger a checkmate
        self.travel = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
        self.overtake = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
