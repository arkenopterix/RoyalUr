#File with the purpose of testing game mecanics

from Engine.UrEngine import *

game = UrEngine()
game.printGame()



print(game.playerAddPawn(1,1))
print(game.playerAddPawn(2,2))
game.printGame()
print(game.scopeThroughBoard(4,"forward", "A1", 1))
print(game.scopeThroughBoard(3,"forward", "B1", 2))