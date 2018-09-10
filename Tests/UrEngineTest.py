from Objects.Board import *
from Engine.UrEngine import *



game=UrEngine()
game.printGame()


print(game.playerAddPawn(1))
print(game.playerAddPawn(2))
game.printGame()

print(game.scopeThroughBoard(4,"A1",1))
print(game.scopeThroughBoard(3,"B1",2))