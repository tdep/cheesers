class Player:
    def __init__(self, color, pieces, captures):
        self.color = color
        self.pieces = pieces
        self.captures = captures
        self.check = False

    def checkChecker():
        # See if king is captured, or if King is only piece left - if so, set check to True
        pass
    
    def colorPicker(player_1, player_2, choice):
        # Accept input from player to choose color
        print("Player 1, please choose a color: Black or White (b/w)?")

        picking = False

        while picking == False:
            choice = input()
            if choice == "b":
                player_1.color = "black"
                player_2.color = "white"
                picking = True
            elif choice == "w":
                player_1.color = "white"
                player_2.color = "black"
                picking = True
            else:
                print("Please enter only 'b' or 'w'.")
                print()
        print(f"Player 1, you are playing as: {player_1.color}")
        print(f"Player 2, you are playing as: {player_2.color}")