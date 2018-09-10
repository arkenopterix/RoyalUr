from Objects.Board import *
from Objects.Dice import *



##############class#####################
class UrEngine:
    """ This class defines the game engine for the game"""

    ##############constructeur##################
    def __init__(self):
        self.board = Board()
        self.dice = Dice()
        self.availablePawnsPlayer1Count = 5
        self.availablePawnsPlayer2Count = 5
        self.safePawnsPlayer1Count = 0
        self.safePawnsPlayer2Count = 0

    def playerAddPawn(self,playerNum,moveValue):
        # function purpose: Function that adds a pawn on the board for the given player
        # input: - playerNum: player number
        #        - moveValue: number of squares the pawn will move
        # return: [couldAddPawn ; resultSquare]
        couldAddPawn = False
        if(playerNum ==1):
            if(self.availablePawnsPlayer1Count > 0):
                scopeResult = self.scopeThroughBoard(moveValue,"A1",1)
                if (scopeResult[0] == "MoveOK"):
                    self.board.placePawn(1,scopeResult[1])
                    self.availablePawnsPlayer1Count -= self.availablePawnsPlayer1Count
                    couldAddPawn = True
                elif (scopeResult[0] == "MoveKO"):
                    pass
                else:
                    print("could not add pawn: weird case after board scope")
            else:
                print("Error: no available pawns for player 1")
        else:
            if (self.availablePawnsPlayer2Count > 0):
                scopeResult = self.scopeThroughBoard(moveValue, "B1", 1)
                if (scopeResult[0] == "MoveOK"):
                    self.board.placePawn(2, scopeResult[1])
                    self.availablePawnsPlayer2Count -= self.availablePawnsPlayer2Count
                    couldAddPawn = True
                elif (scopeResult[0] == "MoveKO"):
                    pass
                else:
                    print("could not add pawn: weird case after board scope")
            else:
                print("Error: no available pawns for player 2")
        return couldAddPawn

    def movePlayerPawn(self,moveValue, pawnPosition, playerNum):
        # function purpose: Function that moves the player pawn around after checking if the pawn can make the move
        #  input: - moveValue: number of squares the pawn will move
        #        - pawnPosition: current position of the pawn on the board
        #        - playerNum: player number
        if ( playerNum ==1):
            pass
        else:
            pass



    def scopeThroughBoard(self,moveValue,direction, pawnPosition,playerNum):
        # function purpose: Function that iterates the moves of the pawn on the board to return which square it ends on and what is the outcome of the move
        # input: - moveValue: number of squares the pawn will move
        #        - direction: direction of the move, either "forward" or "backward"
        #        - pawnPosition: current position of the pawn on the board
        #        - playerNum: player number
        if(direction == "forward"):
            nextPawnPosition = self.board.boardDic[pawnPosition][1]

            if(moveValue == 1):
               if( nextPawnPosition == "Safe"): #Pawn can be placed off the board
                   return ["PawnSafe",""]
               else:
                  return self.scopeThroughBoard(moveValue-1,"forward",nextPawnPosition,playerNum)
            elif(moveValue == 0): #the pawn has finished moving
                if(self.board.boardDic[pawnPosition][0] == 0 ): #there is no pawn on the targeted square
                    return ["MoveOK",pawnPosition]
                elif(self.board.boardDic[pawnPosition][0] == playerNum ): # the square is already occupied by one of the players pawns
                    return ["MoveKO",""]
                else:
                    return  ["MoveReplace",pawnPosition]
            else: # if the pawn hasn't finished it's move, continue tu scope through the board
                if(nextPawnPosition == "Safe"):
                    return self.scopeThroughBoard(moveValue - 1,"backward", self.board.boardDic[pawnPosition][2], playerNum)
                else:
                    return self.scopeThroughBoard(moveValue - 1,"forward", nextPawnPosition,playerNum)
        elif(direction == "backward"):
            nextPawnPosition = self.board.boardDic[pawnPosition][2]
            if(moveValue == 0):
                if (self.board.boardDic[pawnPosition][0] == 0):  # there is no pawn on the targeted square
                    return ["MoveOK", pawnPosition]
                elif (self.board.boardDic[pawnPosition][
                          0] == playerNum):  # the square is already occupied by one of the players pawns
                    return ["MoveKO", ""]
                else:
                    return ["MoveReplace", pawnPosition]
            elif(moveValue > 0):
                return self.scopeThroughBoard(moveValue - 1,"backward", nextPawnPosition, playerNum)
            else:
                print("ERROR:scopeThroughBoard: incorrect move value")
        else:
            print("ERROR:scopeThroughBoard: incorrect direction value")


    def printGame(self):
        # function purpose: Minimal interface for the current game status
        # input: none
        print("######Game status######")
        print("Player 1 remaning pawns: %s" % (self.availablePawnsPlayer1Count))
        print("Player 1 points: %s" % (self.safePawnsPlayer1Count))
        print("Player 2 remaning pawns: %s" % (self.availablePawnsPlayer2Count))
        print("Player 2 points: %s" % (self.safePawnsPlayer2Count))
        self.board.show()

    #def player1Move(self,m,):