from Objects import Board
from Objects import Dice



##############class#####################
class UrEngine:
    """ This class defines the game engine for the game"""

    ##############constructeur##################
    def __init__(self):
        self.board = Board()
        self.dice = Dice()
        self.availablePawnsPlayer1Count = 5
        self.availablePawnsPlayer2Count = 5
        self.safePawnsPlayer1Count = 0;
        self.safePawnsPlayer2Count = 0;

    def playerAddPawn(self,playerNum):
        couldAddPawn = False
        if(playerNum ==1):
            if(self.board[9] == 0):
                if(self.availablePawnsPlayer1Count <= 0):
                    self.board[9] = 1
                    self.availablePawnsPlayer1Count -= self.availablePawnsPlayer1Count
                    couldAddPawn = True
                else:
                    print("Error: no available pawns for player 1")
        else:
            if(self.board[15] == 0):
                if (self.availablePawnsPlayer2Count <= 0):
                    self.board[15] = 2
                    self.availablePawnsPlayer2Count -= self.availablePawnsPlayer2Count
                    couldAddPawn = True
                else:
                    print("Error: no available pawns for player 2")


        return couldAddPawn

    def playerMove(self,playerNum,boardPos,m):
        if (playerNum == 1):
            if(9 <= boardPos <= 12):


        else:
            pass





